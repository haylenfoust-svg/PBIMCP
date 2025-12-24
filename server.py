#!/usr/bin/env python3
"""
Power BI MCP Server
让 Claude Code 通过你的账号访问 Power BI
"""

import msal
import requests
import json
import sys
import os

from config import CLIENT_ID, TENANT_ID

# Power BI API 配置
API_BASE = "https://api.powerbi.com/v1.0/myorg"
SCOPES = ['https://analysis.windows.net/powerbi/api/.default']

# 令牌缓存文件
CACHE_FILE = os.path.join(os.path.dirname(__file__), ".token_cache.json")


def load_cache():
    """加载令牌缓存"""
    cache = msal.SerializableTokenCache()
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cache.deserialize(f.read())
    return cache


def save_cache(cache):
    """保存令牌缓存"""
    if cache.has_state_changed:
        with open(CACHE_FILE, "w") as f:
            f.write(cache.serialize())


def get_access_token() -> str:
    """获取访问令牌（优先使用缓存）"""
    cache = load_cache()

    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=f'https://login.microsoftonline.com/{TENANT_ID}',
        token_cache=cache
    )

    # 尝试从缓存获取
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result and "access_token" in result:
            save_cache(cache)
            return result["access_token"]

    # 需要交互式登录 - 使用 Device Code Flow
    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        raise Exception(f"无法创建设备流: {flow.get('error_description', 'Unknown error')}")

    # 输出登录提示到 stderr（这样 MCP 协议不会被干扰）
    print("\n" + "=" * 60, file=sys.stderr)
    print("Power BI 授权登录", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"请在浏览器中打开: {flow['verification_uri']}", file=sys.stderr)
    print(f"输入代码: {flow['user_code']}", file=sys.stderr)
    print("=" * 60 + "\n", file=sys.stderr)
    sys.stderr.flush()

    result = app.acquire_token_by_device_flow(flow)

    if "access_token" in result:
        save_cache(cache)
        return result["access_token"]
    else:
        raise Exception(f"认证失败: {result.get('error_description', 'Unknown error')}")


def api_get(endpoint: str) -> dict:
    """GET 请求"""
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_BASE}{endpoint}", headers=headers)
    if response.status_code == 200:
        return response.json()
    return {"error": response.status_code, "message": response.text}


def api_post(endpoint: str, data: dict = None) -> dict:
    """POST 请求"""
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(f"{API_BASE}{endpoint}", headers=headers, json=data)
    if response.status_code in [200, 202]:
        try:
            return response.json()
        except:
            return {"status": "success", "code": response.status_code}
    return {"error": response.status_code, "message": response.text}


# ============================================================
# MCP 工具实现
# ============================================================

def list_workspaces() -> str:
    """列出所有工作区"""
    result = api_get("/groups")
    workspaces = result.get("value", [])

    output = f"找到 {len(workspaces)} 个工作区:\n\n"
    for ws in workspaces:
        output += f"- **{ws['name']}**\n"
        output += f"  ID: `{ws['id']}`\n\n"

    if not workspaces:
        output += "(没有共享工作区，你可以使用个人工作区)\n"

    return output


def list_datasets(workspace_id: str = None) -> str:
    """列出数据集"""
    if workspace_id:
        endpoint = f"/groups/{workspace_id}/datasets"
        location = f"工作区 {workspace_id}"
    else:
        endpoint = "/datasets"
        location = "个人工作区"

    result = api_get(endpoint)
    datasets = result.get("value", [])

    output = f"在 {location} 找到 {len(datasets)} 个数据集:\n\n"
    for ds in datasets:
        output += f"- **{ds['name']}**\n"
        output += f"  ID: `{ds['id']}`\n"
        output += f"  Web URL: {ds.get('webUrl', 'N/A')}\n\n"

    return output


def list_reports(workspace_id: str = None) -> str:
    """列出报表"""
    if workspace_id:
        endpoint = f"/groups/{workspace_id}/reports"
        location = f"工作区 {workspace_id}"
    else:
        endpoint = "/reports"
        location = "个人工作区"

    result = api_get(endpoint)
    reports = result.get("value", [])

    output = f"在 {location} 找到 {len(reports)} 个报表:\n\n"
    for rpt in reports:
        output += f"- **{rpt['name']}**\n"
        output += f"  ID: `{rpt['id']}`\n"
        output += f"  数据集: `{rpt.get('datasetId', 'N/A')}`\n"
        output += f"  Web URL: {rpt.get('webUrl', 'N/A')}\n\n"

    return output


def list_dashboards(workspace_id: str = None) -> str:
    """列出仪表板"""
    if workspace_id:
        endpoint = f"/groups/{workspace_id}/dashboards"
        location = f"工作区 {workspace_id}"
    else:
        endpoint = "/dashboards"
        location = "个人工作区"

    result = api_get(endpoint)
    dashboards = result.get("value", [])

    output = f"在 {location} 找到 {len(dashboards)} 个仪表板:\n\n"
    for db in dashboards:
        output += f"- **{db['displayName']}**\n"
        output += f"  ID: `{db['id']}`\n\n"

    return output


def get_dataset_tables(dataset_id: str, workspace_id: str = None) -> str:
    """获取数据集的表结构"""
    if workspace_id:
        endpoint = f"/groups/{workspace_id}/datasets/{dataset_id}/tables"
    else:
        endpoint = f"/datasets/{dataset_id}/tables"

    result = api_get(endpoint)

    if "error" in result:
        return f"错误: {result}"

    tables = result.get("value", [])
    output = f"数据集包含 {len(tables)} 个表:\n\n"

    for table in tables:
        output += f"### {table['name']}\n"
        if "columns" in table:
            for col in table["columns"]:
                output += f"  - {col['name']} ({col.get('dataType', 'unknown')})\n"
        output += "\n"

    return output


def execute_dax(dataset_id: str, query: str, workspace_id: str = None) -> str:
    """执行 DAX 查询"""
    if workspace_id:
        endpoint = f"/groups/{workspace_id}/datasets/{dataset_id}/executeQueries"
    else:
        endpoint = f"/datasets/{dataset_id}/executeQueries"

    payload = {
        "queries": [{"query": query}],
        "serializerSettings": {"includeNulls": True}
    }

    result = api_post(endpoint, payload)

    if "error" in result:
        return f"查询错误: {result}"

    if "results" in result and result["results"]:
        tables = result["results"][0].get("tables", [])
        if tables and "rows" in tables[0]:
            rows = tables[0]["rows"]
            output = f"查询返回 {len(rows)} 行:\n\n```json\n"
            output += json.dumps(rows[:50], indent=2, ensure_ascii=False)
            if len(rows) > 50:
                output += f"\n... 还有 {len(rows) - 50} 行"
            output += "\n```"
            return output

    return f"查询结果: {json.dumps(result, indent=2)}"


def refresh_dataset(dataset_id: str, workspace_id: str = None) -> str:
    """刷新数据集"""
    if workspace_id:
        endpoint = f"/groups/{workspace_id}/datasets/{dataset_id}/refreshes"
    else:
        endpoint = f"/datasets/{dataset_id}/refreshes"

    result = api_post(endpoint)
    return f"刷新触发结果: {result}"


def get_overview() -> str:
    """获取 Power BI 完整概览"""
    output = "# Power BI 概览\n\n"

    # 个人工作区
    output += "## 个人工作区 (My Workspace)\n\n"

    my_datasets = api_get("/datasets").get("value", [])
    my_reports = api_get("/reports").get("value", [])
    my_dashboards = api_get("/dashboards").get("value", [])

    output += f"- 数据集: {len(my_datasets)} 个\n"
    output += f"- 报表: {len(my_reports)} 个\n"
    output += f"- 仪表板: {len(my_dashboards)} 个\n\n"

    if my_datasets:
        output += "### 数据集列表:\n"
        for ds in my_datasets:
            output += f"- {ds['name']} (`{ds['id']}`)\n"
        output += "\n"

    if my_reports:
        output += "### 报表列表:\n"
        for rpt in my_reports:
            output += f"- {rpt['name']} (`{rpt['id']}`)\n"
        output += "\n"

    # 共享工作区
    workspaces = api_get("/groups").get("value", [])

    if workspaces:
        output += f"## 共享工作区 ({len(workspaces)} 个)\n\n"
        for ws in workspaces:
            output += f"### {ws['name']}\n"
            output += f"ID: `{ws['id']}`\n\n"

            ws_datasets = api_get(f"/groups/{ws['id']}/datasets").get("value", [])
            ws_reports = api_get(f"/groups/{ws['id']}/reports").get("value", [])

            output += f"- 数据集: {len(ws_datasets)} 个\n"
            if ws_datasets:
                for ds in ws_datasets:
                    output += f"  - {ds['name']} (`{ds['id']}`)\n"

            output += f"- 报表: {len(ws_reports)} 个\n"
            if ws_reports:
                for rpt in ws_reports:
                    output += f"  - {rpt['name']} (`{rpt['id']}`)\n"
            output += "\n"

    return output


# ============================================================
# MCP 协议处理
# ============================================================

TOOLS = {
    "pbi_overview": {
        "description": "获取你的 Power BI 完整概览（所有工作区、数据集、报表）",
        "inputSchema": {"type": "object", "properties": {}, "required": []},
        "handler": lambda args: get_overview()
    },
    "pbi_list_workspaces": {
        "description": "列出你有权限访问的所有工作区",
        "inputSchema": {"type": "object", "properties": {}, "required": []},
        "handler": lambda args: list_workspaces()
    },
    "pbi_list_datasets": {
        "description": "列出数据集。不传 workspace_id 则列出个人工作区的数据集",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace_id": {"type": "string", "description": "工作区 ID（可选）"}
            },
            "required": []
        },
        "handler": lambda args: list_datasets(args.get("workspace_id"))
    },
    "pbi_list_reports": {
        "description": "列出报表。不传 workspace_id 则列出个人工作区的报表",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace_id": {"type": "string", "description": "工作区 ID（可选）"}
            },
            "required": []
        },
        "handler": lambda args: list_reports(args.get("workspace_id"))
    },
    "pbi_list_dashboards": {
        "description": "列出仪表板",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace_id": {"type": "string", "description": "工作区 ID（可选）"}
            },
            "required": []
        },
        "handler": lambda args: list_dashboards(args.get("workspace_id"))
    },
    "pbi_get_tables": {
        "description": "获取数据集的表和列结构",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dataset_id": {"type": "string", "description": "数据集 ID"},
                "workspace_id": {"type": "string", "description": "工作区 ID（可选）"}
            },
            "required": ["dataset_id"]
        },
        "handler": lambda args: get_dataset_tables(args["dataset_id"], args.get("workspace_id"))
    },
    "pbi_execute_dax": {
        "description": "在数据集上执行 DAX 查询",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dataset_id": {"type": "string", "description": "数据集 ID"},
                "query": {"type": "string", "description": "DAX 查询，如 EVALUATE TOPN(10, 'Sales')"},
                "workspace_id": {"type": "string", "description": "工作区 ID（可选）"}
            },
            "required": ["dataset_id", "query"]
        },
        "handler": lambda args: execute_dax(args["dataset_id"], args["query"], args.get("workspace_id"))
    },
    "pbi_refresh": {
        "description": "刷新数据集",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dataset_id": {"type": "string", "description": "数据集 ID"},
                "workspace_id": {"type": "string", "description": "工作区 ID（可选）"}
            },
            "required": ["dataset_id"]
        },
        "handler": lambda args: refresh_dataset(args["dataset_id"], args.get("workspace_id"))
    }
}


def handle_request(request: dict) -> dict:
    """处理 MCP 请求"""
    method = request.get("method", "")
    req_id = request.get("id")
    params = request.get("params", {})

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "powerbi-mcp", "version": "1.0.0"}
            }
        }

    elif method == "notifications/initialized":
        return None

    elif method == "tools/list":
        tools_list = []
        for name, tool in TOOLS.items():
            tools_list.append({
                "name": name,
                "description": tool["description"],
                "inputSchema": tool["inputSchema"]
            })
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"tools": tools_list}
        }

    elif method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})

        if tool_name in TOOLS:
            try:
                result = TOOLS[tool_name]["handler"](tool_args)
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": result}]
                    }
                }
            except Exception as e:
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": f"错误: {str(e)}"}],
                        "isError": True
                    }
                }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"}
            }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"}
    }


def main():
    """主循环 - 处理 stdio MCP 协议"""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break

            request = json.loads(line.strip())
            response = handle_request(request)

            if response:
                print(json.dumps(response), flush=True)

        except json.JSONDecodeError:
            continue
        except Exception as e:
            print(json.dumps({
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": str(e)}
            }), flush=True)


if __name__ == "__main__":
    main()
