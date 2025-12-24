# Power BI 完整学习指南

> 适合初学者的 Power BI 术语和概念大全

---

## 目录

1. [核心概念入门](#一核心概念入门)
2. [数据获取与转换（Power Query）](#二数据获取与转换power-query--m语言)
3. [数据建模](#三数据建模)
4. [DAX 语言](#四dax-语言)
5. [可视化与报表](#五可视化与报表)
6. [Power BI 服务（云端）](#六power-bi-服务云端)
7. [安全与权限](#七安全与权限)
8. [性能与优化](#八性能与优化)
9. [高级功能](#九高级功能)
10. [文件类型与许可证](#十文件类型与许可证)

---

## 一、核心概念入门

### 1.1 什么是 DAX？

**DAX (Data Analysis Expressions)** 是 Power BI、Power Pivot 和 Analysis Services 中使用的公式语言，用于定义计算逻辑。

#### DAX 的两种主要用途

**用途一：创建计算（最常用）**

在数据模型中定义度量值或计算列：

```dax
// 度量值示例
Total Sales = SUM(Sales[Amount])

Revenue YoY Growth = 
DIVIDE(
    [Total Sales] - CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Date[Date])),
    CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Date[Date]))
)

// 计算列示例
Profit Margin = Sales[Revenue] - Sales[Cost]
```

**用途二：DAX Query（查询语言）**

DAX 也可以作为独立的查询语言，返回表格结果：

```dax
EVALUATE
SUMMARIZECOLUMNS(
    Product[Category],
    Date[Year],
    "Total Sales", [Total Sales],
    "Order Count", COUNTROWS(Sales)
)
ORDER BY Date[Year] DESC
```

#### DAX 公式 vs DAX Query 对比

| 方面 | DAX 公式（度量值/计算列） | DAX Query |
|------|-------------------------|-----------|
| 用途 | 定义可复用的计算逻辑 | 即席查询，返回数据表 |
| 关键字 | 无特殊开头 | 必须以 `EVALUATE` 开头 |
| 返回值 | 标量值或列 | 表格 |
| 使用场景 | 报表中的动态计算 | 调试、数据导出、性能分析 |
| 工具 | Power BI Desktop 模型 | DAX Studio、SSMS、Performance Analyzer |

---

### 1.2 什么是度量值（Measure）？

#### 一句话定义

> **度量值是一个"计算公式"，它不存储具体数字，而是根据你当前看的范围动态计算结果。**

#### 生活化比喻

假设你开了一家奶茶店，有这样的销售数据：

| 订单ID | 日期 | 产品 | 数量 | 单价 | 金额 |
|--------|------|------|------|------|------|
| 001 | 1月1日 | 珍珠奶茶 | 2 | 15 | 30 |
| 002 | 1月1日 | 柠檬茶 | 1 | 12 | 12 |
| 003 | 1月2日 | 珍珠奶茶 | 3 | 15 | 45 |
| 004 | 1月2日 | 果茶 | 2 | 18 | 36 |
| 005 | 1月3日 | 柠檬茶 | 4 | 12 | 48 |

想象度量值是一个**聪明的计算器**：

- 你问它："总销售额是多少？" → 它算出 171（30+12+45+36+48）
- 你问它："1月1日卖了多少？" → 它只算那天的，得出 42
- 你问它："珍珠奶茶卖了多少？" → 它只算珍珠奶茶，得出 75

**同一个公式，不同的问法，不同的答案。** 这就是度量值的核心特点。

#### 创建度量值

```dax
总销售额 = SUM(销售表[金额])
```

这行代码的意思是：
- `总销售额` — 度量值的名字
- `=` — 定义符号
- `SUM()` — 求和函数
- `销售表[金额]` — 对"销售表"中的"金额"列求和

---

### 1.3 关键概念：筛选上下文（Filter Context）

> **筛选上下文 = 当前计算时，数据被哪些条件筛选了**

#### 场景示例

**场景1：放在卡片上（无筛选）**
```
总销售额 = 171  （计算全部5行）
```

**场景2：按日期分组的表格**

| 日期 | 总销售额 |
|------|----------|
| 1月1日 | 42 |
| 1月2日 | 81 |
| 1月3日 | 48 |

同一个公式 `SUM(销售表[金额])`，但每一行的**筛选上下文不同**。

**场景3：按产品分组的表格**

| 产品 | 总销售额 |
|------|----------|
| 珍珠奶茶 | 75 |
| 柠檬茶 | 60 |
| 果茶 | 36 |

---

### 1.4 度量值 vs 计算列

| 对比项 | 度量值 (Measure) | 计算列 (Calculated Column) |
|--------|------------------|---------------------------|
| **存储** | 不存储数据，实时计算 | 存储在表中，占用内存 |
| **计算时机** | 用户查看报表时 | 数据刷新时 |
| **结果** | 根据筛选上下文变化 | 每行一个固定值 |
| **用途** | 聚合计算（求和、平均、计数等） | 行级别计算 |

**计算列示例**（逐行计算，结果固定）：
```dax
利润 = 销售表[金额] - 销售表[成本]
```

**度量值示例**（动态聚合）：
```dax
总利润 = SUM(销售表[利润])
```

---

### 1.5 常用度量值示例

#### 基础聚合

```dax
总销售额 = SUM(销售表[金额])           // 求和
订单数量 = COUNT(销售表[订单ID])       // 计数
平均单价 = AVERAGE(销售表[单价])       // 平均值
最高单笔 = MAX(销售表[金额])           // 最大值
最低单笔 = MIN(销售表[金额])           // 最小值
产品种类数 = DISTINCTCOUNT(销售表[产品]) // 去重计数
```

#### 带条件的计算

```dax
珍珠奶茶销售额 = CALCULATE(
    SUM(销售表[金额]),
    销售表[产品] = "珍珠奶茶"
)
```

#### 比例计算

```dax
销售占比 = DIVIDE(
    SUM(销售表[金额]),
    CALCULATE(SUM(销售表[金额]), ALL(销售表[产品]))
)
```

---

## 二、数据获取与转换（Power Query / M语言）

### 2.1 基础概念

| 术语 | 英文 | 解释 |
|------|------|------|
| Power Query | Power Query | 数据获取和清洗的引擎，有独立的编辑器 |
| M语言 | M Language | Power Query 背后的函数式编程语言 |
| 查询 | Query | 从数据源获取并处理数据的一组步骤 |
| 应用的步骤 | Applied Steps | 右侧显示的数据处理步骤列表 |
| 数据源 | Data Source | 数据来源（Excel、SQL、API、网页等） |
| 连接器 | Connector | 连接特定数据源的组件 |

### 2.2 数据处理操作

| 术语 | 英文 | 解释 |
|------|------|------|
| 追加查询 | Append Queries | 把两个表上下合并（类似 SQL 的 UNION） |
| 合并查询 | Merge Queries | 把两个表左右合并（类似 SQL 的 JOIN） |
| 分组依据 | Group By | 按某列分组并聚合 |
| 透视列 | Pivot Column | 把行转成列 |
| 逆透视列 | Unpivot Column | 把列转成行 |
| 拆分列 | Split Column | 按分隔符或字符数拆分一列为多列 |
| 填充 | Fill | 用上方或下方的值填充空单元格 |
| 替换值 | Replace Values | 替换特定值 |
| 更改类型 | Change Type | 更改列的数据类型 |
| 删除重复项 | Remove Duplicates | 删除重复行 |
| 筛选行 | Filter Rows | 按条件筛选数据 |
| 添加列 | Add Column | 添加自定义列、条件列、索引列等 |
| 条件列 | Conditional Column | 基于 if-then 逻辑创建的新列 |
| 自定义列 | Custom Column | 用 M 公式创建的新列 |
| 索引列 | Index Column | 添加行号列 |
| 参数 | Parameter | 可复用的变量（如文件路径、服务器名） |
| 函数 | Function | 可复用的查询逻辑 |

### 2.3 加载模式

| 术语 | 英文 | 解释 |
|------|------|------|
| 导入模式 | Import Mode | 数据复制到 Power BI 文件中（默认） |
| DirectQuery | DirectQuery | 不导入数据，实时查询数据源 |
| 实时连接 | Live Connection | 连接到已有的 Analysis Services 模型 |
| 复合模型 | Composite Model | 混合使用导入和 DirectQuery |
| 仅连接 | Connection Only | 只创建查询但不加载到模型 |
| 增量刷新 | Incremental Refresh | 只刷新新增/变化的数据 |

---

## 三、数据建模

### 3.1 表类型

| 术语 | 英文 | 解释 |
|------|------|------|
| 事实表 | Fact Table | 存储业务事件/交易数据的表（如销售记录） |
| 维度表 | Dimension Table | 存储描述性信息的表（如产品、客户、时间） |
| 日期表 | Date Table | 专门的时间维度表，用于时间智能计算 |
| 桥接表 | Bridge Table | 处理多对多关系的中间表 |
| 查找表 | Lookup Table | 维度表的另一种叫法 |
| 计算表 | Calculated Table | 用 DAX 创建的虚拟表 |

### 3.2 架构模式

| 术语 | 英文 | 解释 |
|------|------|------|
| 星型架构 | Star Schema | 一个事实表连接多个维度表（推荐） |
| 雪花架构 | Snowflake Schema | 维度表进一步规范化拆分 |
| 扁平表 | Flat Table | 所有数据放在一张宽表里（不推荐） |

### 3.3 关系

| 术语 | 英文 | 解释 |
|------|------|------|
| 关系 | Relationship | 表与表之间的连接 |
| 基数 | Cardinality | 关系的类型：一对多、一对一、多对多 |
| 一对多 | One-to-Many (1:*) | 最常见的关系 |
| 多对多 | Many-to-Many (*:*) | 两边都可以有重复值 |
| 交叉筛选方向 | Cross Filter Direction | 筛选传递的方向：单向或双向 |
| 单向筛选 | Single Direction | 筛选只从"一"端传递到"多"端 |
| 双向筛选 | Both Directions | 筛选双向传递（谨慎使用） |
| 活动关系 | Active Relationship | 默认生效的关系 |
| 非活动关系 | Inactive Relationship | 需要用 USERELATIONSHIP 激活 |
| 主键 | Primary Key | 表中唯一标识每行的列 |
| 外键 | Foreign Key | 引用另一个表主键的列 |
| 歧义关系 | Ambiguous Relationship | 多条路径连接两表 |

### 3.4 列与属性

| 术语 | 英文 | 解释 |
|------|------|------|
| 数据类型 | Data Type | 列的类型（文本、整数、小数、日期等） |
| 格式 | Format | 显示格式（如货币、百分比） |
| 数据类别 | Data Category | 特殊标记（如地理位置、URL） |
| 排序依据列 | Sort by Column | 让一列按另一列排序 |
| 默认汇总 | Default Summarization | 字段默认的聚合方式 |
| 隐藏 | Hide | 对报表用户隐藏列/表 |
| 数据组 | Data Group | 将列值分组 |
| 层次结构 | Hierarchy | 多列组成的钻取路径 |
| 显示文件夹 | Display Folder | 把度量值或列组织到文件夹 |

---

## 四、DAX 语言

### 4.1 核心概念

| 术语 | 英文 | 解释 |
|------|------|------|
| DAX | Data Analysis Expressions | Power BI 的公式语言 |
| 度量值 | Measure | 动态聚合计算的公式 |
| 计算列 | Calculated Column | 逐行计算并存储的列 |
| 计算表 | Calculated Table | 用 DAX 生成的表 |
| 筛选上下文 | Filter Context | 当前影响计算的所有筛选条件 |
| 行上下文 | Row Context | 迭代时"当前行"的概念 |
| 上下文转换 | Context Transition | CALCULATE 把行上下文转为筛选上下文 |
| 隐式度量值 | Implicit Measure | 拖字段时自动创建的聚合 |
| 显式度量值 | Explicit Measure | 自己写的度量值 |
| 变量 | Variable (VAR) | DAX 中定义的临时变量 |

### 4.2 函数分类

| 类别 | 代表函数 | 用途 |
|------|----------|------|
| 聚合函数 | SUM, AVERAGE, COUNT, MIN, MAX | 基础汇总 |
| 迭代函数 | SUMX, AVERAGEX, COUNTX, MAXX | 逐行计算后聚合 |
| 筛选函数 | CALCULATE, FILTER, ALL, ALLEXCEPT | 修改筛选上下文 |
| 时间智能函数 | DATEADD, SAMEPERIODLASTYEAR, DATESYTD | 时间比较计算 |
| 表函数 | SUMMARIZE, ADDCOLUMNS, SELECTCOLUMNS | 返回表的函数 |
| 关系函数 | RELATED, RELATEDTABLE, USERELATIONSHIP | 跨表取值 |
| 逻辑函数 | IF, SWITCH, AND, OR | 条件判断 |
| 文本函数 | CONCATENATE, LEFT, RIGHT, FORMAT | 文本处理 |
| 信息函数 | ISBLANK, ISERROR, HASONEVALUE | 检测数据状态 |
| 数学函数 | DIVIDE, ROUND, ABS, POWER | 数学计算 |

### 4.3 重要函数详解

| 函数 | 解释 | 示例 |
|------|------|------|
| CALCULATE | 在修改后的筛选上下文中计算 | `CALCULATE(SUM(Sales[Amount]), Product[Category]="A")` |
| FILTER | 返回筛选后的表 | `FILTER(Product, Product[Price]>100)` |
| ALL | 移除筛选 | `ALL(Product)` |
| ALLEXCEPT | 移除除指定列外的所有筛选 | `ALLEXCEPT(Sales, Sales[Region])` |
| RELATED | 从相关表取值（多端取一端） | `RELATED(Product[Category])` |
| RELATEDTABLE | 获取相关表的行（一端取多端） | `RELATEDTABLE(Sales)` |
| DISTINCTCOUNT | 去重计数 | `DISTINCTCOUNT(Sales[CustomerID])` |
| DIVIDE | 安全除法 | `DIVIDE([Sales], [Cost], 0)` |
| BLANK | 返回空值 | `IF(condition, value, BLANK())` |
| VALUES | 返回列的唯一值 | `VALUES(Product[Category])` |
| SELECTEDVALUE | 返回单选值 | `SELECTEDVALUE(Product[Name], "多选")` |
| HASONEVALUE | 检测是否只有一个值 | `HASONEVALUE(Product[Category])` |
| EARLIER | 在嵌套行上下文中引用外层 | 用于复杂计算列 |
| RANKX | 排名 | `RANKX(ALL(Product), [Sales])` |

### 4.4 时间智能函数

| 函数 | 解释 |
|------|------|
| DATEADD | 日期偏移（如去年同期） |
| SAMEPERIODLASTYEAR | 去年同期 |
| PREVIOUSMONTH / PREVIOUSYEAR | 上月/上年 |
| DATESYTD / DATESMTD / DATESQTD | 年/月/季至今 |
| TOTALYTD / TOTALMTD / TOTALQTD | 年/月/季累计 |
| DATESBETWEEN | 日期范围 |
| PARALLELPERIOD | 平行期间 |
| FIRSTDATE / LASTDATE | 第一天/最后一天 |

---

## 五、可视化与报表

### 5.1 报表结构

| 术语 | 英文 | 解释 |
|------|------|------|
| 报表 | Report | 包含多页的可视化文件 |
| 页面 | Page | 报表中的单个画布 |
| 视觉对象 | Visual | 图表、表格等展示组件 |
| 画布 | Canvas | 放置视觉对象的区域 |
| 主题 | Theme | 统一的颜色和格式设置 |
| 模板 | Template (.pbit) | 可复用的报表模板 |

### 5.2 视觉对象类型

| 类型 | 包含 |
|------|------|
| 图表 | 柱状图、条形图、折线图、面积图、饼图、环形图、散点图、瀑布图、漏斗图、树状图、旋风图 |
| 表格类 | 表、矩阵（交叉表）、卡片、多行卡 |
| 地图类 | 地图、填充地图、形状地图、ArcGIS 地图 |
| 切片器 | 列表切片器、下拉切片器、日期切片器、范围切片器 |
| 其他 | KPI、仪表、R/Python 视觉对象、自定义视觉对象 |

### 5.3 交互与导航

| 术语 | 英文 | 解释 |
|------|------|------|
| 切片器 | Slicer | 筛选控件 |
| 交叉筛选 | Cross-filtering | 点击一个视觉对象筛选其他对象 |
| 交叉突出显示 | Cross-highlighting | 点击后突出相关数据 |
| 钻取 | Drill-through | 跳转到详情页 |
| 向下钻取 | Drill-down | 在层次结构中向下展开 |
| 向上钻取 | Drill-up | 在层次结构中向上返回 |
| 展开到下一级别 | Expand to Next Level | 展开所有项到下一层级 |
| 书签 | Bookmark | 保存的报表状态快照 |
| 按钮 | Button | 可点击的导航/操作元素 |
| 页面导航 | Page Navigation | 页面之间的跳转 |
| 工具提示 | Tooltip | 悬停显示的详细信息 |
| 报表页工具提示 | Report Page Tooltip | 把整个页面作为工具提示 |
| 同步切片器 | Sync Slicers | 跨页面同步切片器选择 |
| 编辑交互 | Edit Interactions | 自定义视觉对象之间的筛选行为 |

### 5.4 字段配置

| 术语 | 英文 | 解释 |
|------|------|------|
| 值 | Values | 放度量值或需聚合的字段 |
| 轴 | Axis | X轴或Y轴字段 |
| 图例 | Legend | 分类着色的字段 |
| 详细信息 | Details | 增加数据粒度的字段 |
| 工具提示 | Tooltips | 悬停时显示的额外字段 |
| 小型多图 | Small Multiples | 按某字段拆分成多个小图 |
| 条件格式 | Conditional Formatting | 根据值改变颜色/图标 |

### 5.5 格式化

| 术语 | 英文 | 解释 |
|------|------|------|
| 数据标签 | Data Labels | 显示在图表上的数值 |
| 图例 | Legend | 颜色/形状的说明 |
| 标题 | Title | 视觉对象的标题 |
| 背景 | Background | 视觉对象的背景色 |
| 边框 | Border | 视觉对象的边框 |
| 网格线 | Gridlines | 图表背景的参考线 |
| 参考线 | Reference Line | 标记特定值的线（如目标线） |
| 数据颜色 | Data Colors | 数据系列的颜色 |
| 响应式布局 | Responsive | 根据大小自动调整 |

---

## 六、Power BI 服务（云端）

### 6.1 基础概念

| 术语 | 英文 | 解释 |
|------|------|------|
| Power BI 服务 | Power BI Service | 云端的 app.powerbi.com |
| Power BI Desktop | Power BI Desktop | 本地的开发工具 |
| 工作区 | Workspace | 内容的协作容器 |
| 我的工作区 | My Workspace | 个人工作区 |
| 应用 | App | 打包发布的报表集合 |
| 数据集 | Dataset | 发布到服务的数据模型 |
| 数据流 | Dataflow | 云端的 Power Query（ETL） |
| 数据集市 | Datamart | 自助式关系数据库 |

### 6.2 仪表板

| 术语 | 英文 | 解释 |
|------|------|------|
| 仪表板 | Dashboard | 固定在单页的磁贴集合 |
| 磁贴 | Tile | 仪表板上的单个元素 |
| 固定 | Pin | 把视觉对象固定到仪表板 |
| 实时磁贴 | Live Tile | 实时更新的磁贴 |
| 特色仪表板 | Featured Dashboard | 默认显示的仪表板 |

### 6.3 数据刷新

| 术语 | 英文 | 解释 |
|------|------|------|
| 计划刷新 | Scheduled Refresh | 定时刷新数据 |
| 按需刷新 | On-demand Refresh | 手动触发刷新 |
| 增量刷新 | Incremental Refresh | 只刷新增量数据 |
| 网关 | Gateway | 连接本地数据源的桥梁 |
| 个人网关 | Personal Gateway | 个人使用的网关 |
| 企业网关 | Enterprise Gateway | 组织共享的网关 |
| 数据源凭据 | Data Source Credentials | 连接数据源的账号密码 |

### 6.4 共享与协作

| 术语 | 英文 | 解释 |
|------|------|------|
| 共享 | Share | 把报表共享给特定用户 |
| 发布 | Publish | 从 Desktop 发布到服务 |
| 订阅 | Subscribe | 定期收到报表快照邮件 |
| 评论 | Comments | 在报表上添加评论 |
| 认可 | Endorsement | 标记为"已认证"或"已推广" |
| 已认证 | Certified | 经过审核的可信内容 |
| 已推广 | Promoted | 推荐使用的内容 |
| 数据世系 | Data Lineage | 数据流向的可视化 |
| 影响分析 | Impact Analysis | 查看修改影响哪些内容 |

---

## 七、安全与权限

### 7.1 访问控制

| 术语 | 英文 | 解释 |
|------|------|------|
| 工作区角色 | Workspace Role | 管理员、成员、参与者、查看者 |
| 应用权限 | App Permissions | 应用的访问权限 |
| 共享权限 | Sharing Permissions | 允许再次共享、构建权限等 |
| 构建权限 | Build Permission | 允许基于数据集创建报表 |

### 7.2 行级安全性（RLS）

| 术语 | 英文 | 解释 |
|------|------|------|
| 行级安全性 | Row-Level Security (RLS) | 限制用户看到的数据行 |
| 角色 | Role | RLS 中定义的安全角色 |
| DAX 筛选器 | DAX Filter | 定义角色的筛选表达式 |
| 动态 RLS | Dynamic RLS | 基于 `USERNAME()` 或 `USERPRINCIPALNAME()` |
| 静态 RLS | Static RLS | 硬编码的筛选条件 |

### 7.3 对象级安全性

| 术语 | 英文 | 解释 |
|------|------|------|
| 对象级安全性 | Object-Level Security (OLS) | 隐藏特定表或列 |

---

## 八、性能与优化

### 8.1 性能概念

| 术语 | 英文 | 解释 |
|------|------|------|
| VertiPaq | VertiPaq | Power BI 的内存列式存储引擎 |
| 列式存储 | Columnar Storage | 按列存储数据（压缩效率高） |
| 压缩 | Compression | 减少数据存储大小 |
| 基数 | Cardinality | 列中唯一值的数量（越低越好压缩） |
| 数据模型大小 | Model Size | .pbix 文件中数据模型的大小 |

### 8.2 分析工具

| 术语 | 英文 | 解释 |
|------|------|------|
| 性能分析器 | Performance Analyzer | Desktop 中的查询时间分析工具 |
| DAX Studio | DAX Studio | 外部 DAX 查询和优化工具 |
| Tabular Editor | Tabular Editor | 外部模型编辑工具 |
| VertiPaq Analyzer | VertiPaq Analyzer | 分析模型大小和结构 |
| 查询计划 | Query Plan | DAX 查询的执行计划 |
| 存储引擎查询 | Storage Engine Query | 从存储读取数据的查询 |
| 公式引擎查询 | Formula Engine Query | 计算逻辑的查询 |

### 8.3 优化技术

| 术语 | 英文 | 解释 |
|------|------|------|
| 聚合表 | Aggregation Table | 预聚合的汇总表加速查询 |
| 用户定义聚合 | User-defined Aggregations | 手动配置的聚合 |
| 自动聚合 | Automatic Aggregations | 系统自动创建的聚合 |
| 分区 | Partition | 把大表拆分成多个部分 |
| 查询折叠 | Query Folding | Power Query 把操作推送到数据源执行 |

---

## 九、高级功能

### 9.1 分析功能

| 术语 | 英文 | 解释 |
|------|------|------|
| 快速见解 | Quick Insights | 自动发现数据中的模式 |
| 问答 | Q&A | 自然语言提问 |
| 智能叙述 | Smart Narrative | 自动生成文字说明 |
| 异常检测 | Anomaly Detection | 自动检测数据异常点 |
| 预测 | Forecasting | 基于历史数据预测趋势 |
| 分解树 | Decomposition Tree | 交互式根因分析 |
| 关键影响因素 | Key Influencers | 分析影响某指标的因素 |
| 聚类 | Clustering | 自动分组相似数据 |

### 9.2 AI 功能

| 术语 | 英文 | 解释 |
|------|------|------|
| AI 视觉对象 | AI Visuals | 内置 AI 能力的视觉对象 |
| 认知服务 | Cognitive Services | Azure AI 服务集成 |
| 文本分析 | Text Analytics | 情感分析、关键词提取 |
| 视觉识别 | Vision | 图像标记 |
| Azure ML 集成 | Azure ML Integration | 调用机器学习模型 |

### 9.3 开发者功能

| 术语 | 英文 | 解释 |
|------|------|------|
| 自定义视觉对象 | Custom Visual | 第三方或自建的视觉对象 |
| Power BI Embedded | Power BI Embedded | 把报表嵌入应用程序 |
| REST API | REST API | 编程接口 |
| 推送数据集 | Push Dataset | 通过 API 推送实时数据 |
| XMLA 端点 | XMLA Endpoint | 高级数据集管理接口 |
| 外部工具 | External Tools | Desktop 中集成的第三方工具 |

### 9.4 企业功能

| 术语 | 英文 | 解释 |
|------|------|------|
| 部署管道 | Deployment Pipeline | 开发/测试/生产环境管理 |
| 高级容量 | Premium Capacity | 专用计算资源 |
| 每用户高级版 | Premium Per User (PPU) | 按用户付费的高级版 |
| 多地理位置 | Multi-Geo | 数据存储在指定地区 |
| BYOK | Bring Your Own Key | 自带加密密钥 |
| 敏感度标签 | Sensitivity Labels | 数据分类标签 |
| 审计日志 | Audit Logs | 活动追踪记录 |
| 使用指标 | Usage Metrics | 报表使用情况统计 |

---

## 十、文件类型与许可证

### 10.1 文件类型

| 扩展名 | 名称 | 用途 |
|--------|------|------|
| .pbix | Power BI 文件 | 包含数据和报表的完整文件 |
| .pbit | Power BI 模板 | 只有结构没有数据的模板 |
| .pbids | 数据源文件 | 数据源连接信息 |
| .json | 主题文件 | 报表主题定义 |
| .svg / .png | 自定义图标 | 按钮或视觉对象图标 |

### 10.2 许可证类型

| 许可证 | 说明 |
|--------|------|
| Power BI Free | 个人使用，不能共享 |
| Power BI Pro | 可共享和协作 |
| Power BI Premium Per User (PPU) | 个人高级功能 |
| Power BI Premium (P1-P5) | 组织级专用容量 |
| Power BI Embedded (A/EM SKU) | 嵌入式应用 |

---

## 附录：快速参考卡片

### DAX 常用公式模板

```dax
// 基础汇总
Total Sales = SUM(Sales[Amount])

// 去年同期
Sales LY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Date[Date]))

// 同比增长率
YoY Growth = DIVIDE([Total Sales] - [Sales LY], [Sales LY])

// 年累计
Sales YTD = TOTALYTD([Total Sales], Date[Date])

// 占比
Sales % = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Product)))

// 排名
Product Rank = RANKX(ALL(Product[Name]), [Total Sales], , DESC, DENSE)

// 动态标题
Dynamic Title = "Sales as of " & FORMAT(MAX(Date[Date]), "YYYY-MM-DD")
```

### 学习资源推荐

- **官方文档**: docs.microsoft.com/power-bi
- **DAX Guide**: dax.guide（函数参考）
- **SQLBI**: sqlbi.com（DAX 深度教程）
- **DAX Studio**: daxstudio.org（免费工具）
- **Tabular Editor**: tabulareditor.com

---

*文档版本：1.0 | 更新日期：2025年*
