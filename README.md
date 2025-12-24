# PBIMCP - Power BI MCP Server

A Model Context Protocol (MCP) server that enables Claude Code to interact with Microsoft Power BI through natural language.

## Features

- **List Workspaces** - View all Power BI workspaces you have access to
- **List Datasets** - Browse datasets in any workspace
- **List Reports** - View reports and their metadata
- **List Dashboards** - Access dashboard information
- **Execute DAX Queries** - Run DAX queries against datasets
- **Refresh Datasets** - Trigger dataset refreshes
- **Get Table Schema** - Inspect table and column structures

## Prerequisites

- Python 3.10+
- Power BI account (Pro or Premium Per User license recommended)
- Azure AD App Registration with delegated permissions

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/haylenfoust-svg/PBIMCP.git
cd PBIMCP
```

### 2. Create virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Azure AD App

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to Microsoft Entra ID → App registrations → New registration
3. Name your app (e.g., `Claude-PowerBI-MCP`)
4. Set Redirect URI to `http://localhost` (Public client/native)
5. Add delegated permissions for Power BI Service:
   - `Dataset.Read.All`
   - `Dataset.ReadWrite.All`
   - `Report.Read.All`
   - `Workspace.Read.All`
   - `Workspace.ReadWrite.All`
6. Enable "Allow public client flows" in Authentication settings

### 4. Update config.py

```python
CLIENT_ID = "your-application-client-id"
TENANT_ID = "your-directory-tenant-id"
```

### 5. Add to Claude Code

```bash
claude mcp add powerbi-mcp -s user -- /path/to/PBIMCP/venv/bin/python /path/to/PBIMCP/server.py
```

## Usage

After restarting Claude Code, you can use natural language commands:

```
# Get an overview of your Power BI environment
"Show me my Power BI overview"

# List all datasets
"List my Power BI datasets"

# Execute a DAX query
"Run DAX query on dataset xxx: EVALUATE TOPN(10, 'Sales')"

# Refresh a dataset
"Refresh dataset xxx"
```

## Available MCP Tools

| Tool | Description |
|------|-------------|
| `pbi_overview` | Get complete overview of all workspaces, datasets, and reports |
| `pbi_list_workspaces` | List all accessible workspaces |
| `pbi_list_datasets` | List datasets in a workspace |
| `pbi_list_reports` | List reports in a workspace |
| `pbi_list_dashboards` | List dashboards in a workspace |
| `pbi_get_tables` | Get table and column schema of a dataset |
| `pbi_execute_dax` | Execute DAX query on a dataset |
| `pbi_refresh` | Trigger dataset refresh |

## Authentication Flow

This server uses OAuth 2.0 Device Code Flow:

1. First run displays a code and URL
2. Open the URL in browser and enter the code
3. Sign in with your Power BI account
4. Authorize the application
5. Token is cached for subsequent requests

## Security

- Uses delegated permissions (acts on behalf of the signed-in user)
- Only accesses data the user has permission to view
- No passwords stored - uses OAuth 2.0 tokens
- Tokens are cached in memory only

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
