#!/usr/bin/env python3
"""测试 Power BI 连接并保存令牌缓存"""

import os
from config import CLIENT_ID, TENANT_ID
import msal
import requests

SCOPES = ['https://analysis.windows.net/powerbi/api/.default']
CACHE_FILE = os.path.join(os.path.dirname(__file__), ".token_cache.json")

def load_cache():
    cache = msal.SerializableTokenCache()
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cache.deserialize(f.read())
    return cache

def save_cache(cache):
    if cache.has_state_changed:
        with open(CACHE_FILE, "w") as f:
            f.write(cache.serialize())

print("=" * 60)
print("Power BI 连接测试")
print("=" * 60)

cache = load_cache()
app = msal.PublicClientApplication(
    CLIENT_ID,
    authority=f'https://login.microsoftonline.com/{TENANT_ID}',
    token_cache=cache
)

# 尝试从缓存获取令牌
accounts = app.get_accounts()
result = None

if accounts:
    print("发现缓存的账户，尝试静默获取令牌...")
    result = app.acquire_token_silent(SCOPES, account=accounts[0])

if not result or "access_token" not in result:
    # 使用 Device Code Flow
    flow = app.initiate_device_flow(scopes=SCOPES)
    print(f"\n请在浏览器中打开: {flow['verification_uri']}")
    print(f"输入代码: {flow['user_code']}\n")
    print("等待登录...")
    result = app.acquire_token_by_device_flow(flow)

if 'access_token' in result:
    save_cache(cache)
    print("\n✓ 登录成功！令牌已缓存。正在获取 Power BI 数据...\n")

    token = result['access_token']
    headers = {"Authorization": f"Bearer {token}"}

    # 获取数据
    datasets = requests.get("https://api.powerbi.com/v1.0/myorg/datasets", headers=headers).json()
    reports = requests.get("https://api.powerbi.com/v1.0/myorg/reports", headers=headers).json()
    workspaces = requests.get("https://api.powerbi.com/v1.0/myorg/groups", headers=headers).json()

    print("=" * 60)
    print("Power BI 概览")
    print("=" * 60)

    print(f"\n共享工作区: {len(workspaces.get('value', []))} 个")
    for ws in workspaces.get('value', []):
        print(f"   - {ws['name']} (ID: {ws['id']})")

        # 获取工作区内容
        ws_datasets = requests.get(f"https://api.powerbi.com/v1.0/myorg/groups/{ws['id']}/datasets", headers=headers).json()
        ws_reports = requests.get(f"https://api.powerbi.com/v1.0/myorg/groups/{ws['id']}/reports", headers=headers).json()

        print(f"     数据集: {len(ws_datasets.get('value', []))} 个")
        for ds in ws_datasets.get('value', []):
            print(f"       - {ds['name']} (ID: {ds['id'][:8]}...)")

        print(f"     报表: {len(ws_reports.get('value', []))} 个")
        for rpt in ws_reports.get('value', []):
            print(f"       - {rpt['name']}")

    print(f"\n个人工作区数据集: {len(datasets.get('value', []))} 个")
    for ds in datasets.get('value', []):
        print(f"   - {ds['name']} (ID: {ds['id'][:8]}...)")

    print(f"\n个人工作区报表: {len(reports.get('value', []))} 个")
    for rpt in reports.get('value', []):
        print(f"   - {rpt['name']}")

    print("\n" + "=" * 60)
    print("✓ Power BI 连接测试成功！令牌已保存。")
    print("  现在 Claude Code 的 MCP 可以直接使用缓存的令牌。")
    print("=" * 60)
else:
    print(f"\n✗ 登录失败: {result.get('error_description', 'Unknown error')}")
