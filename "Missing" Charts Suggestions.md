# 

## **Formatted for Power BI Implementation**

---

## **1. INFLATION DATA (8 Charts)**

### **Chart 1.1: Consumer Price Inflation Trends (2000-2023)**

**Chart Type:** Line Chart (Multi-Series)

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Inflation Rate (%)
- **Series 1:** WB Inflation (Primary Line)
- **Series 2:** IMF WEO Inflation (Dashed Line, validation)

**Indicators Needed:**

- `FP.CPI.TOTL.ZG` (WB) - Inflation, consumer prices (annual %)
- `PCPIPCH` (IMF WEO) - Inflation, average consumer prices (% change)

**PBI Specifics:**

- Add reference line at 5% (target lower bound)
- Add reference line at 8% (target upper bound)
- Color: Blue line for WB, Orange dashed for IMF
- Add data labels for peaks/troughs only

**Relationship Explored:** Examines price stability over time, identifying inflationary episodes and their correlation with external shocks (commodity price spikes, currency depreciation) or monetary policy changes.

---

### **Chart 1.2: Headline vs Core Inflation (2010-2023)**

**Chart Type:** Line Chart (Multi-Series with Area Fill)

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** Inflation Rate (%)
- **Series 1:** Headline CPI (Solid Blue Line)
- **Series 2:** Core Inflation (Solid Red Line)
- **Series 3:** Food CPI (Dashed Green Line)

**Indicators Needed:**

- `64...ZF...` (IMF IFS) - Consumer Price Index, All items
- `64X..ZF...` (IMF IFS) - Core Inflation Index (excluding food and energy)
- `64...ZF...` (IMF IFS) - CPI Food component

**PBI Specifics:**

- Shaded area between headline and core (light gray) to highlight volatility gap
- Legend positioned top-right
- Tooltip: Show spread between headline and core

**Relationship Explored:** Distinguishes between persistent underlying inflation pressures (core) and volatile food/energy price shocks, informing whether inflation is demand-driven or supply-driven.

---

### **Chart 1.3: Inflation vs GDP Growth (Scatter Plot 2000-2023)**

**Chart Type:** Scatter Plot with Trend Line

- **X-Axis:** Real GDP Growth (%)
- **Y-Axis:** Inflation Rate (%)
- **Bubbles:** Each point = 1 year
- **Size:** Fixed size for all bubbles
- **Color:** Gradient by year (2000=dark blue, 2023=light blue)

**Indicators Needed:**

- `FP.CPI.TOTL.ZG` (WB) - Inflation, consumer prices (annual %)
- `NY.GDP.MKTP.KD.ZG` (WB) - GDP growth (annual %)

**PBI Specifics:**

- Add linear trend line with equation and R²
- Add quadrant lines at median GDP growth and median inflation
- Data labels: Show year for outlier points only
- Tooltip: Year, GDP growth, Inflation rate

**Relationship Explored:** Tests whether there's a Phillips Curve relationship (trade-off between growth and inflation) or stagflation patterns (high inflation with low growth) indicating supply-side constraints.

---

### **Chart 1.4: CPI Food vs Non-Food Inflation (2010-2023)**

**Chart Type:** Clustered Column Chart with Line Overlay

- **X-Axis:** Year (2010-2023)
- **Y-Axis (Primary):** Inflation Rate (%)
- **Y-Axis (Secondary):** Inflation Rate (%)
- **Columns:** Food Inflation (Blue), Non-Food Inflation (Orange)
- **Line:** Headline Inflation (Red line on secondary axis)

**Indicators Needed:**

- `64...ZF...` (IMF IFS) - CPI Food (convert to % change)
- `64...ZF...` (IMF IFS) - CPI Non-Food (convert to % change)
- `FP.CPI.TOTL.ZG` (WB) - Headline inflation

**PBI Specifics:**

- Column width: 70%
- Data labels on columns
- Secondary axis scaled identically to primary
- Add reference band at 5-8% (target range)

**Relationship Explored:** Identifies whether inflation is driven by agricultural supply shocks (food) or broader demand pressures (non-food), crucial for targeting policy responses.

---

### **Chart 1.5: Inflation and Exchange Rate Depreciation (2010-2023)**

**Chart Type:** Dual-Axis Line Chart

- **X-Axis:** Year (2010-2023)
- **Y-Axis (Primary):** Inflation Rate (%)
- **Y-Axis (Secondary):** Exchange Rate Depreciation (% change, inverted scale)
- **Series 1:** Inflation (Solid Blue Line, primary axis)
- **Series 2:** Exchange Rate % Change (Dashed Red Line, secondary axis)

**Indicators Needed:**

- `FP.CPI.TOTL.ZG` (WB) - Inflation, consumer prices (annual %)
- `PA.NUS.FCRF` (WB) - Official exchange rate (LCU per US$, period average)
- Calculate: Year-over-year % change in exchange rate

**PBI Specifics:**

- Secondary axis inverted (appreciation up, depreciation down)
- Add correlation coefficient in text box
- Synchronized zeros on both axes
- Color-code periods: Green background = appreciation, Red = depreciation

**Relationship Explored:** Assesses pass-through from exchange rate depreciation to domestic prices, indicating degree of import dependence and pricing power in the economy.

---

### **Chart 1.6: GDP Deflator vs CPI Inflation (2000-2023)**

**Chart Type:** Line Chart (Multi-Series) with Shaded Area

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Inflation Rate (%)
- **Series 1:** GDP Deflator (Blue Line)
- **Series 2:** CPI Inflation (Orange Line)
- **Shaded Area:** Between lines (light gray fill)

**Indicators Needed:**

- `NY.GDP.DEFL.KD.ZG` (WB) - Inflation, GDP deflator (annual %)
- `FP.CPI.TOTL.ZG` (WB) - Inflation, consumer prices (annual %)

**PBI Specifics:**

- Add reference line at 0%
- Tooltip: Show spread (Deflator - CPI) = Terms of Trade effect
- Data labels for maximum spread points
- Legend: Explain deflator includes export prices

**Relationship Explored:** Compares broad price changes in domestic production (deflator) versus consumer basket (CPI), revealing terms of trade effects and whether export price changes affect domestic inflation.

---

### **Chart 1.7: Inflation Actual vs Regional Average (2015-2023)**

**Chart Type:** Line Chart with Reference Band

- **X-Axis:** Year (2015-2023)
- **Y-Axis:** Inflation Rate (%)
- **Series 1:** Zambia Inflation (Bold Red Line)
- **Series 2:** Regional Average (Blue Line)
- **Band:** Regional Min-Max (Light blue shaded area)

**Indicators Needed:**

- `FP.CPI.TOTL.ZG` (WB) - Zambia inflation
- Same indicator for: Tanzania, Malawi, Zimbabwe, Botswana, South Africa, Mozambique, DRC
- Calculate: Regional average, min, max

**PBI Specifics:**

- Line thickness: Zambia = 3pt, Regional avg = 2pt
- Shaded area: 30% transparency
- Add annotations for Zambia peaks above regional average
- Conditional formatting: Red when Zambia > Regional avg + 2 std dev

**Relationship Explored:** Benchmarks Zambia's inflation performance against regional peers, identifying whether high inflation is Zambia-specific (policy-driven) or regional (common shocks).

---

### **Chart 1.8: Inflation Heatmap (2015-2023, Monthly if Available)**

**Chart Type:** Matrix/Heatmap

- **Rows:** Year (2015-2023)
- **Columns:** Month (Jan-Dec) OR Quarter (Q1-Q4)
- **Color Scale:** Green (low, <5%) → Yellow (target, 5-8%) → Red (high, >8%)
- **Values:** Monthly/Quarterly inflation rate

**Indicators Needed:**

- `FP.CPI.TOTL.ZG` (WB) - Annual inflation (or monthly if available)
- Country source: Bank of Zambia monthly CPI

**PBI Specifics:**

- Conditional formatting:
    - Green: 0-5%
    - Yellow: 5-8%
    - Orange: 8-12%
    - Red: >12%
- Show values in cells
- Total row: Annual average inflation
- Grand total: Period average

**Relationship Explored:** Visualizes inflation seasonality and intensity over time, identifying persistent high-inflation periods versus temporary spikes, informing monetary policy response timing.

---

## **2. FISCAL BALANCE AND PUBLIC DEBT (12 Charts)**

### **Chart 2.1: Fiscal Balance (% GDP) 2000-2023**

**Chart Type:** Area Chart with Reference Line

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Fiscal Balance (% GDP)
- **Area:** Color-coded by surplus (green) vs deficit (red)
- **Reference Line:** 0% (break-even)

**Indicators Needed:**

- `GGXONLB_NGDP` (IMF WEO) - General government overall balance (% GDP)
- `GC.BAL.CASH.GD.ZS` (WB) - Cash surplus/deficit (% GDP)

**PBI Specifics:**

- Conditional formatting: Positive values = Green fill, Negative = Red fill
- Add reference line at -3% (IMF fiscal sustainability benchmark)
- Data labels for peak surplus and largest deficit
- Add election year markers (vertical dashed lines)

**Relationship Explored:** Tracks fiscal sustainability over time, identifying periods of fiscal consolidation versus expansion and correlation with electoral cycles or commodity price booms/busts.

---

### **Chart 2.2: Government Revenue and Expenditure (% GDP) 2000-2023**

**Chart Type:** Dual-Axis Line Chart with Area Fill

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Percentage of GDP (%)
- **Series 1:** Total Revenue (Blue Line with blue area below)
- **Series 2:** Total Expenditure (Red Line with red area below)
- **Gap:** Shaded deficit area between lines (gray)

**Indicators Needed:**

- `GGR` (IMF WEO) - General government revenue (% GDP)
- `GGX` (IMF WEO) - General government total expenditure (% GDP)

**PBI Specifics:**

- Area transparency: 30%
- Add DAX measure: Fiscal Balance = Revenue - Expenditure
- Tooltip: Show balance amount
- Reference line at 20% (minimum revenue target)
- Reference line at 30% (expenditure ceiling)

**Relationship Explored:** Examines fiscal space evolution, whether deficits arise from revenue shortfalls or expenditure expansion, and sustainability of fiscal trajectory.

---

### **Chart 2.3: Tax Revenue Composition (Most Recent Year)**

**Chart Type:** Donut Chart with Labels

- **Slices:** Different tax types
- **Center:** Total tax revenue (% GDP)
- **Labels:** Outside with percentage and amount

**Indicators Needed:**

- `GR_G111` (IMF GFS) - Taxes on income, profits, and capital gains
- `GR_G1141` (IMF GFS) - VAT/General taxes on goods and services
- `GR_G1142` (IMF GFS) - Excises
- `GR_G115` (IMF GFS) - Taxes on international trade
- `GR_G116` (IMF GFS) - Other taxes

**PBI Specifics:**

- Color scheme: Blue gradient (darkest for largest slice)
- Explode largest slice by 10%
- Show % of total in labels
- Detail labels: Show both % and absolute amount (US$ millions)
- Center value: Total tax revenue as % of GDP

**Relationship Explored:** Reveals tax system structure and dependence on specific bases, indicating vulnerability to economic shocks and potential for revenue mobilization.

---

### **Chart 2.4: Tax-to-GDP Ratio Trends with Regional Comparison (2000-2023)**

**Chart Type:** Line Chart with Reference Band

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Tax Revenue (% GDP)
- **Series 1:** Zambia (Bold Red Line)
- **Series 2:** Regional Average (Blue Line)
- **Series 3:** SADC Average (Green Line)
- **Band:** Regional Min-Max (light gray shaded area)

**Indicators Needed:**

- `GC.TAX.TOTL.GD.ZS` (WB) - Zambia tax revenue (% of GDP)
- Same indicator for: Tanzania, Malawi, Botswana, South Africa, Namibia, Mozambique
- Calculate: SADC average, Regional average, min-max band

**PBI Specifics:**

- Line thickness: Zambia = 3pt, others = 2pt
- Add reference line at 15% (minimum for development needs)
- Data labels: Zambia values only, at key turning points
- Conditional formatting: Highlight periods where Zambia < Regional avg

**Relationship Explored:** Assesses revenue mobilization effort over time and compares to peer countries and tax potential benchmarks, indicating fiscal capacity for development spending.

---

### **Chart 2.5: Government Expenditure by Economic Classification (Most Recent Year)**

**Chart Type:** 100% Stacked Bar Chart (Horizontal)

- **Y-Axis:** Single bar
- **X-Axis:** Percentage (0-100%)
- **Segments:** Different expenditure categories
- **Labels:** Inside each segment with % and amount

**Indicators Needed:**

- `GE_G21` (IMF GFS) - Compensation of employees
- `GE_G22` (IMF GFS) - Use of goods and services
- `GE_G24` (IMF GFS) - Interest payments
- `GE_G25` (IMF GFS) - Subsidies
- `GE_G27` (IMF GFS) - Social benefits
- `GE_G28` (IMF GFS) - Other expense

**PBI Specifics:**

- Color scheme: Sequential (dark to light)
- Highlight: Wages (Blue), Interest (Red), Others (Gray scale)
- Data labels: % for segments >5%, hidden for smaller segments
- Add benchmark comparison bar below (regional average composition)
- Tooltip: Show absolute values and regional comparison

**Relationship Explored:** Examines expenditure rigidity (wage bill, interest) versus discretionary spending, revealing fiscal space for development priorities and vulnerability to interest rate shocks.

---

### **Chart 2.6: Government Expenditure by Function (Most Recent Year)**

**Chart Type:** Treemap

- **Rectangles:** Sized by expenditure amount
- **Color:** By function category
- **Labels:** Function name and % of total

**Indicators Needed:**

- `GE_G704` (IMF GFS) - Economic affairs
- `GE_G707` (IMF GFS) - Health
- `GE_G709` (IMF GFS) - Education
- `GE_G710` (IMF GFS) - Social protection
- `GE_G701` (IMF GFS) - General public services
- `GE_G702` (IMF GFS) - Defense
- Other COFOG categories

**PBI Specifics:**

- Color coding:
    - Blue: Economic affairs (infrastructure)
    - Green: Health
    - Purple: Education
    - Orange: Social protection
    - Gray: General services
    - Red: Defense
- Labels: Show function name, % of total, absolute amount
- Tooltip: Add regional comparison and SDG benchmark

**Relationship Explored:** Reveals government priorities and social spending adequacy, comparing allocations to SDG benchmarks and peer countries.

---

### **Chart 2.7: Public Debt (% GDP) 2000-2023**

**Chart Type:** Area Chart with Threshold Bands

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Public Debt (% GDP)
- **Area:** Gradient fill (green to red as debt increases)
- **Reference Bands:**
    - 0-40%: Green (sustainable)
    - 40-60%: Yellow (elevated)
    - 60%+: Red (high risk)

**Indicators Needed:**

- `GGXWDG_NGDP` (IMF WEO) - General government gross debt (% GDP)
- `GC.DOD.TOTL.GD.ZS` (WB) - Central government debt, total (% GDP)

**PBI Specifics:**

- Conditional formatting by value:
    - <40%: Green area
    - 40-60%: Yellow area
    - > 60%: Red area
        
- Add annotations for HIPC completion point, debt restructuring events
- Data labels: Show values at key turning points
- Add forecast line (dashed) for projections if available

**Relationship Explored:** Tracks debt accumulation trajectory and sustainability, identifying whether debt is stabilizing or on explosive path requiring fiscal adjustment.

---

### **Chart 2.8: External vs Domestic Debt Composition (2000-2023)**

**Chart Type:** 100% Stacked Area Chart

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Debt Composition (% of Total)
- **Area 1:** External Debt (Blue)
- **Area 2:** Domestic Debt (Orange)
- **Line Overlay:** Total Debt (% GDP, secondary axis)

**Indicators Needed:**

- `DT.DOD.DECT.CD` (WB IDS) - External debt stocks, total
- Domestic debt (calculated as: Total debt minus external debt)
- `GGXWDG_NGDP` (IMF WEO) - Total debt (% GDP) for line overlay

**PBI Specifics:**

- Primary axis: 0-100% (composition)
- Secondary axis: 0-100% (debt-to-GDP ratio)
- Area transparency: 0% (solid colors)
- Add reference line on secondary axis at 60% (debt threshold)
- Tooltip: Show both composition % and absolute amounts
- Data label: External debt % at latest year

**Relationship Explored:** Assesses currency risk exposure and vulnerability to exchange rate depreciation, which increases local-currency value of external debt.

---

### **Chart 2.9: Debt by Creditor Type (Most Recent Year)**

**Chart Type:** Clustered Column Chart

- **X-Axis:** Creditor Type
- **Y-Axis:** Debt Amount (US$ millions)
- **Columns:** Grouped by: Concessional vs Non-Concessional
- **Colors:** Blue (Concessional), Red (Non-Concessional)

**Indicators Needed:**

- `DT.DOD.MLAT.CD` (WB IDS) - Multilateral debt
- `DT.DOD.BLAT.CD` (WB IDS) - Bilateral debt
- `DT.DOD.PRVT.CD` (WB IDS) - Private creditor debt
- `DT.DOD.ALLC.CD` (WB IDS) - Concessional debt (for overlay classification)

**PBI Specifics:**

- X-axis categories: Multilateral, Bilateral, Private
- Each category has 2 columns: Concessional (blue), Non-concessional (red)
- Data labels on columns
- Add average interest rate as data label above each column
- Tooltip: Show maturity profile, interest rate, principal creditors
- Total line at top showing sum

**Relationship Explored:** Reveals debt structure and refinancing risk, as commercial debt has shorter maturity and higher interest rates than concessional multilateral/bilateral debt.

---

### **Chart 2.10: Interest Payments (% Revenue and % GDP) 2000-2023**

**Chart Type:** Dual-Axis Line Chart with Area Fill

- **X-Axis:** Year (2000-2023)
- **Y-Axis (Primary):** Interest (% Revenue)
- **Y-Axis (Secondary):** Interest (% GDP)
- **Series 1:** Interest/Revenue (Orange Line with area fill)
- **Series 2:** Interest/GDP (Blue Line)

**Indicators Needed:**

- `GE_G24` (IMF GFS) - Interest payments
- `GGR` (IMF WEO) - General government revenue
- `NGDP_D` (IMF WEO) - Nominal GDP
- Calculate: Interest/Revenue %, Interest/GDP %

**PBI Specifics:**

- Primary axis range: 0-30%
- Secondary axis range: 0-10%
- Add reference line at 15% on primary axis (high burden threshold)
- Add reference line at 5% on secondary axis
- Shaded area under interest/revenue line: Orange, 30% transparency
- Data labels: Show values for latest year
- Conditional formatting: Red when Interest/Revenue >15%

**Relationship Explored:** Measures debt service burden crowding out development spending, critical for assessing fiscal sustainability and debt distress risk.

---

### **Chart 2.11: Primary Balance vs Overall Balance (2000-2023)**

**Chart Type:** Clustered Column Chart with Zero Line

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Balance (% GDP)
- **Column 1:** Overall Balance (Blue)
- **Column 2:** Primary Balance (Orange)
- **Reference Line:** 0% (break-even)

**Indicators Needed:**

- `GGXONLB_NGDP` (IMF WEO) - Overall balance (% GDP)
- `GGXCNL` (IMF WEO) - Primary balance (% GDP), or calculate: Overall balance + Interest payments

**PBI Specifics:**

- Columns side-by-side (not stacked)
- Column width: 80%
- Conditional formatting:
    - Positive values: Green
    - Negative values: Red
- Add reference line at -3% (deficit threshold)
- Gap between columns represents interest burden
- Tooltip: Show interest burden = Overall - Primary
- Data labels for significant divergences

**Relationship Explored:** Distinguishes structural fiscal effort (primary balance) from debt service burden (interest), showing whether deficits stem from discretionary spending or legacy debt.

---

### **Chart 2.12: Fiscal Balance vs Copper Prices (2000-2023)**

**Chart Type:** Dual-Axis Combo Chart (Line + Column)

- **X-Axis:** Year (2000-2023)
- **Y-Axis (Primary):** Fiscal Balance (% GDP)
- **Y-Axis (Secondary):** Copper Price ($/mt or index)
- **Columns:** Fiscal Balance (Green=surplus, Red=deficit, primary axis)
- **Line:** Copper Price (Brown line with markers, secondary axis)

**Indicators Needed:**

- `GGXONLB_NGDP` (IMF WEO) - Fiscal balance (% GDP)
- World Bank commodity price data - Copper prices ($/mt or index 2010=100)

**PBI Specifics:**

- Columns: Conditional color by sign
- Line: Thick brown line (3pt)
- Secondary axis scaled to show correlation clearly
- Add correlation coefficient in text box (r value)
- Highlight periods: Gray shaded boxes for copper boom periods
- Tooltip: Show both values + copper revenue contribution if available
- Data labels: Fiscal balance values only

**Relationship Explored:** Tests correlation between commodity export revenues and fiscal position, revealing procyclical fiscal policy and vulnerability to copper price volatility.

---

## **3. BALANCE OF PAYMENTS COMPREHENSIVE (10 Charts)**

### **Chart 3.1: Current Account Balance (% GDP) 2000-2023**

**Chart Type:** Area Chart with Reference Line

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Current Account Balance (% GDP)
- **Area:** Conditional color (Green=surplus, Red=deficit)
- **Reference Line:** 0% and -5% (warning threshold)

**Indicators Needed:**

- `BCA_NGDPD` (IMF WEO) - Current account balance (% GDP)
- `BN.CAB.XOKA.GD.ZS` (WB) - Current account balance (% GDP)

**PBI Specifics:**

- Conditional area fill:
    - Above 0: Green (surplus)
    - 0 to -5%: Yellow (moderate deficit)
    - Below -5%: Red (large deficit)
- Add reference band: -3% to -5% (manageable deficit zone)
- Data labels at peaks and troughs
- Add annotations for major BOP crisis events
- Tooltip: Show absolute value in US$ millions

**Relationship Explored:** Tracks external balance sustainability, identifying persistent deficits indicating external borrowing needs or surpluses indicating savings available for foreign investment.

---

### **Chart 3.2: Current Account Components (Stacked Bar, 2010-2023)**

**Chart Type:** Waterfall Chart OR Stacked Bar Chart

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** Current Account Component (US$ millions)
- **Bars (Stacked):**
    - Trade Balance (Blue)
    - Services Balance (Orange)
    - Primary Income (Red)
    - Secondary Income (Green)
    - **Total:** Current Account Balance (Dark line overlay)

**Indicators Needed:**

- `BXG` (IMF BOPS) - Goods exports
- `BMG` (IMF BOPS) - Goods imports (negative)
- `BXS` (IMF BOPS) - Services exports
- `BMS` (IMF BOPS) - Services imports (negative)
- `BPRI` (IMF BOPS) - Primary income (net)
- `BSEC` (IMF BOPS) - Secondary income (net)

**PBI Specifics:**

- Calculate: Trade Balance = Exports - Imports
- Stacked bars with negative values below axis
- Color scheme:
    - Blue: Trade balance (usually positive)
    - Red: Primary income (usually negative - profit repatriation)
    - Green: Secondary income (remittances, usually positive)
- Black line overlay: Total current account
- Data labels: Show totals at top
- Tooltip: Show all component values

**Relationship Explored:** Decomposes current account to identify whether deficits stem from trade imbalances, profit repatriation (primary income), or remittances (secondary income).

---

### **Chart 3.3: Trade Balance (% GDP) 2000-2023**

**Chart Type:** Line Chart with Area Fill

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Trade Balance (% GDP)
- **Area:** Green (surplus) or Red (deficit)
- **Reference Line:** 0%

**Indicators Needed:**

- `BX.GSR.GNFS.CD` (WB) - Exports of goods and services
- `BM.GSR.GNFS.CD` (WB) - Imports of goods and services
- `NY.GDP.MKTP.CD` (WB) - GDP current US$
- Calculate: (Exports - Imports) / GDP * 100

**PBI Specifics:**

- Conditional area color by value
- Add reference line at 0%
- Data labels: Show values for peaks and valleys
- Add copper price annotation (when trade balance peaks)
- Tooltip: Show exports, imports, and trade balance values
- Secondary series (optional): Export/Import coverage ratio

**Relationship Explored:** Assesses trade performance and import coverage by exports, revealing whether country earns enough foreign exchange to finance imports or requires capital inflows.

---

### **Chart 3.4: Financial Account Components (2010-2023)**

**Chart Type:** Stacked Area Chart

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** Financial Flows (US$ millions)
- **Areas:**
    - FDI (Blue, bottom)
    - Portfolio Investment (Orange)
    - Other Investment (Gray)
    - Reserve Assets (Red, top)
- **Line:** Total Financial Account (Black line)

**Indicators Needed:**

- `BFDIR` (IMF BOPS) - Direct investment (net)
- `BFPI` (IMF BOPS) - Portfolio investment (net)
- `BFOI` (IMF BOPS) - Other investment (net)
- `BFRA` (IMF BOPS) - Reserve assets (negative = accumulation)

**PBI Specifics:**

- Stacked areas: 100% transparency on edges, 70% fill
- Distinguish between stable (FDI) and volatile (Portfolio) flows
- Reserve assets: Plot as negative when accumulating (show downward)
- Add reference line at 0
- Tooltip: Show composition % and absolute values
- Legend: Explain FDI=stable, Portfolio=volatile

**Relationship Explored:** Shows how current account deficits are financed—through stable FDI versus volatile portfolio flows versus reserve drawdown—indicating external vulnerability.

---

### **Chart 3.5: Foreign Direct Investment (Net Inflows, US$ millions) 2000-2023**

**Chart Type:** Column Chart with Trend Line

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** FDI Net Inflows (US$ millions)
- **Columns:** FDI inflows (Blue)
- **Line:** 3-year moving average (Red dashed line)

**Indicators Needed:**

- `BX.KLT.DINV.CD.WD` (WB) - FDI net inflows (BoP, current US$)
- `BFDIL` (IMF BOPS) - FDI liabilities (net incurrence)

**PBI Specifics:**

- Column color: Gradient blue (darker = higher values)
- Add 3-year moving average line
- Data labels: Show values for peak years
- Add annotation boxes for major FDI projects (mining investments)
- Tooltip: Show FDI as % GDP also
- Reference line: Regional average FDI inflow

**Relationship Explored:** Tracks long-term capital inflows for productive investment, distinguishing boom periods (mining investment) from slowdowns, and correlation with copper prices.

---

### **Chart 3.6: Remittances (US$ millions and % GDP) 2000-2023**

**Chart Type:** Dual-Axis Combo Chart (Column + Line)

- **X-Axis:** Year (2000-2023)
- **Y-Axis (Primary):** Remittances (US$ millions)
- **Y-Axis (Secondary):** Remittances (% GDP)
- **Columns:** Remittances amount (Green, primary axis)
- **Line:** Remittances % GDP (Orange line, secondary axis)

**Indicators Needed:**

- `BX.TRF.PWKR.CD.DT` (WB) - Personal remittances received (current US$)
- `NY.GDP.MKTP.CD` (WB) - GDP current US$
- Calculate: Remittances as % GDP

**PBI Specifics:**

- Columns: Green with data labels
- Line: Orange with markers
- Secondary axis: 0-10% range
- Add regional comparison line (dashed blue)
- Tooltip: Show per capita remittance value
- Growth % annotation for significant changes

**Relationship Explored:** Assesses importance of diaspora transfers for foreign exchange and household income, providing counter-cyclical buffer during economic downturns.

---

### **Chart 3.7: Primary Income (Investment Income Flows) 2010-2023**

**Chart Type:** Waterfall Chart

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** Primary Income (US$ millions)
- **Bars:**
    - Starting value: Credits/Receipts (Green)
    - Decrease: Debits/Payments (Red)
    - Ending value: Net Primary Income (Blue)

**Indicators Needed:**

- `BPRIC` (IMF BOPS) - Primary income, credit (receipts)
- `BPRID` (IMF BOPS) - Primary income, debit (payments)
- `BPRI` (IMF BOPS) - Primary income, net

**PBI Specifics:**

- Waterfall showing: Credits (up, green) → Debits (down, red) → Net (blue)
- Data labels on all bars
- Connector lines between bars
- Tooltip: Breakdown of credits (dividends received, wages) and debits (profit repatriation, interest)
- Add % of exports annotation for debits

**Relationship Explored:** Reveals profit repatriation by foreign investors (especially mining companies), showing surplus drain and whether FDI generates net positive foreign exchange after profit outflows.

---

### **Chart 3.8: Reserve Accumulation vs Current Account (2000-2023)**

**Chart Type:** Dual-Axis Line Chart with Markers

- **X-Axis:** Year (2000-2023)
- **Y-Axis (Primary):** Reserves (US$ billions)
- **Y-Axis (Secondary):** Current Account Balance (US$ millions)
- **Series 1:** Reserves (Blue line with filled area, primary axis)
- **Series 2:** Current Account (Orange line with markers, secondary axis)

**Indicators Needed:**

- `FI.RES.TOTL.CD` (WB) - Total reserves (current US$, billions)
- `BN.CAB.XOKA.CD` (WB) - Current account balance (current US$, millions)

**PBI Specifics:**

- Primary axis: 0-5 billion range (adjust as needed)
- Secondary axis: Centered at 0 (show positive and negative CA)
- Blue area fill under reserves line (30% transparency)
- Add reference line on primary axis: 3 months of imports
- Markers on CA line: Circle (surplus), Triangle down (deficit)
- Tooltip: Show both absolute and months of import cover
- Shading: Gray boxes for reserve depletion periods

**Relationship Explored:** Tests whether reserves increase during surplus periods and deplete during deficits, or whether capital inflows enable reserve buildup despite deficits.

---

### **Chart 3.9: Balance of Payments Summary Table (Most Recent 3 Years)**

**Chart Type:** Matrix Table with Conditional Formatting

- **Rows:** BOP Components
    - Current Account
        - Goods Balance
        - Services Balance
        - Primary Income
        - Secondary Income
    - Capital Account
    - Financial Account
        - FDI
        - Portfolio Investment
        - Other Investment
        - Reserve Assets
    - Errors & Omissions
- **Columns:** Year N-2, Year N-1, Year N, Change N vs N-1
- **Values:** US$ millions

**Indicators Needed:**

- `BCA` (IMF BOPS) - Current account balance
- `BKA` (IMF BOPS) - Capital account balance
- `BFA` (IMF BOPS) - Financial account balance
- All sub-components from BOPS
- Calculate: Errors and omissions = BCA + BKA - BFA

**PBI Specifics:**

- Conditional formatting:
    - Positive values: Green text
    - Negative values: Red text
    - Errors >5% of CA: Yellow highlight
- Subtotals in bold
- Grand total row for overall BOP
- Data bars in "Change" column
- Indent sub-items
- Number format: US$ millions, 1 decimal place

**Relationship Explored:** Comprehensive BOP accounting check showing whether current and capital accounts are financed by financial flows, with errors/omissions indicating measurement issues or illicit flows.

---

### **Chart 3.10: Exports and Imports (% GDP) 2000-2023**

**Chart Type:** Area Chart (Stacked) with Line Overlay

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Trade (% GDP)
- **Area 1:** Exports (% GDP, Blue)
- **Area 2:** Imports (% GDP, Red, stacked)
- **Line:** Trade Openness = (Exports+Imports) % GDP (Black dashed line)

**Indicators Needed:**

- `NE.EXP.GNFS.ZS` (WB) - Exports of goods and services (% GDP)
- `NE.IMP.GNFS.ZS` (WB) - Imports of goods and services (% GDP)
- Calculate: Trade Openness = Exports + Imports

**PBI Specifics:**

- Stacked area (not 100%)
- Export area: Blue, 50% transparency
- Import area: Red, 50% transparency
- Gap between represents trade balance
- Line overlay for total openness: Black dashed, 3pt
- Data labels: Show openness ratio at key years
- Tooltip: Show exports, imports, balance, and openness separately
- Add regional average openness as reference line

**Relationship Explored:** Measures trade openness and structural trends (increasing/decreasing integration), revealing whether growth is export-led or domestic demand-led.

---

## **4. FOREIGN EXCHANGE RESERVES (6 Charts)**

### **Chart 4.1: Gross International Reserves (US$ billions) 2000-2023**

**Chart Type:** Area Chart with Milestone Markers

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Reserves (US$ billions)
- **Area:** Blue gradient fill
- **Markers:** Circle markers for peak/trough years

**Indicators Needed:**

- `FI.RES.TOTL.CD` (WB) - Total reserves including gold (current US$)
- `1L.DZF...` (IMF IFS) - Total reserves including gold

**PBI Specifics:**

- Area fill: Gradient blue (dark at bottom, light at top)
- Add milestone markers with data labels for:
    - Peak reserves
    - Significant drops (>20%)
    - HIPC completion point
- Add annotations for major events (debt relief, copper boom, crisis)
- Reference line: 2 billion (critical minimum)
- Tooltip: Show reserves + months of import cover + % change YoY
- Growth rate annotation (% change from prior year)

**Relationship Explored:** Tracks reserve accumulation/depletion over time, identifying periods of external strength (reserve buildup) versus stress (reserve losses during BOP crises).

---

### **Chart 4.2: Reserves in Months of Imports (2000-2023)**

**Chart Type:** Line Chart with Threshold Bands

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Months of Import Cover
- **Line:** Reserves in months (Blue line, bold)
- **Reference Bands:**
    - 0-3 months: Red zone (critical)
    - 3-6 months: Yellow zone (adequate)
    - 6+ months: Green zone (comfortable)

**Indicators Needed:**

- `FI.RES.TOTL.MO` (WB) - Total reserves in months of imports

**PBI Specifics:**

- Background color bands:
    - <3 months: Red, 30% transparency
    - 3-6 months: Yellow, 30% transparency
    - > 6 months: Green, 30% transparency
        
- Line: Blue, 3pt thickness
- Data labels at critical points (<3 months)
- Add reference line at 3 months (IMF minimum)
- Add reference line at 6 months (comfortable level)
- Tooltip: Show months + absolute reserve value + annual imports
- Conditional data point color: Red when <3, Green when >6

**Relationship Explored:** Assesses reserve adequacy using standard metric (3 months minimum), indicating ability to weather temporary BOP shocks without crisis.

---

### **Chart 4.3: Reserves (% of External Debt) 2000-2023**

**Chart Type:** Dual-Axis Line Chart

- **X-Axis:** Year (2000-2023)
- **Y-Axis (Primary):** Reserves (% External Debt)
- **Y-Axis (Secondary):** External Debt (US$ billions)
- **Series 1:** Reserves/External Debt % (Blue line, primary)
- **Series 2:** External Debt (Red line with area, secondary)

**Indicators Needed:**

- `FI.RES.TOTL.CD` (WB) - Total reserves
- `DT.DOD.DECT.CD` (WB IDS) - External debt stocks
- `FI.RES.TOTL.DT.ZS` (WB) - Reserves (% of external debt)

**PBI Specifics:**

- Primary axis: 0-200% range
- Secondary axis: Debt in US$ billions
- Add reference line at 100% on primary axis (adequate coverage)
- Blue line thickness: 3pt
- Red area fill: 30% transparency
- Data labels: Show % at key years
- Tooltip: Show all three values (reserves, debt, ratio)
- Conditional formatting: Highlight periods when ratio <50% (red marker)

**Relationship Explored:** Tests whether reserves are sufficient to cover short-term external debt, critical for avoiding liquidity crises when debt must be rolled over.

---

### **Chart 4.4: Reserve Coverage Ratios (Most Recent Year)**

**Chart Type:** Gauge Chart / Bullet Chart (Multiple)

- **4 Separate Gauges in 2x2 Grid:**
    1. Months of Import Cover
    2. % of External Debt
    3. % of Short-term Debt
    4. % of Broad Money (M3)
- **Each Gauge:**
    - Red zone (inadequate)
    - Yellow zone (adequate)
    - Green zone (comfortable)
    - Needle showing actual value

**Indicators Needed:**

- `FI.RES.TOTL.MO` (WB) - Months of import cover
- `FI.RES.TOTL.DT.ZS` (WB) - Reserves (% external debt)
- `DT.DOD.DSTC.CD` (WB IDS) - Short-term external debt
- M3 money supply (from country sources or IMF IFS)
- Calculate: Reserve/Short-term debt ratio, Reserve/M3 ratio

**PBI Specifics:**

- Gauge 1 (Import Cover):
    - Red: 0-3 months
    - Yellow: 3-6 months
    - Green: 6+ months
    - Target: 6 months
- Gauge 2 (External Debt):
    - Red: 0-50%
    - Yellow: 50-100%
    - Green: 100%+
    - Target: 100%
- Gauge 3 (Short-term Debt):
    - Red: 0-100%
    - Yellow: 100-150%
    - Green: 150%+
    - Target: 100%
- Gauge 4 (Broad Money):
    - Red: 0-10%
    - Yellow: 10-20%
    - Green: 20%+
    - Target: 20%
- Add title above grid: "Reserve Adequacy Dashboard - [Year]"
- Use traffic light colors consistently

**Relationship Explored:** Multi-metric reserve adequacy assessment comparing to IMF benchmarks (3 months imports, 100% short-term debt, 20% broad money for emerging markets).

---

### **Chart 4.5: Reserves vs Exchange Rate Movements (2010-2023)**

**Chart Type:** Scatter Plot with Dual Axis (Reserves on Y1, Exchange Rate on Y2) OR Dual-Axis Line Chart

- **X-Axis:** Year (2010-2023)
- **Y-Axis (Primary):** Reserves (US$ billions)
- **Y-Axis (Secondary):** Exchange Rate (LCU per US$, inverted)
- **Series 1:** Reserves (Blue line/area, primary)
- **Series 2:** Exchange Rate (Red line, secondary inverted)

**Indicators Needed:**

- `FI.RES.TOTL.CD` (WB) - Reserves (billions)
- `PA.NUS.FCRF` (WB) - Exchange rate (LCU per US$)

**PBI Specifics:**

- Primary axis: Reserves in billions
- Secondary axis: **Inverted scale** (appreciation up, depreciation down)
- Blue area under reserves line: 30% transparency
- Red exchange rate line: 2pt
- Add correlation annotation
- Highlight periods: Gray shading when reserves falling AND currency depreciating
- Tooltip: Show % change YoY for both
- Data labels: Mark major intervention episodes

**Relationship Explored:** Tests whether central bank intervenes to stabilize currency (reserve losses during depreciation pressures), or whether it allows free float.

---

### **Chart 4.6: Reserve Composition (Most Recent Year)**

**Chart Type:** Donut Chart OR Waterfall Chart

- **Slices/Bars:**
    1. Foreign Currency Reserves (largest, blue)
    2. Gold (gold color)
    3. SDR Holdings (green)
    4. Reserve Position in IMF (orange)
- **Center (if donut):** Total Reserves value

**Indicators Needed:**

- `1L.D.ZF...` (IMF IFS) - Reserves excluding gold
- `1LAGD.ZF` (IMF IFS) - Gold (national valuation)
- `1LXGS.ZF` (IMF IFS) - Reserve position in IMF
- `1LDSD.ZF` (IMF IFS) - SDR holdings

**PBI Specifics:**

- Color scheme:
    - Blue: Foreign currency (largest slice)
    - Gold: #FFD700
    - Green: SDR holdings
    - Orange: IMF position
- Labels: Outside with component name, % and absolute value
- Center value (donut): Total reserves
- Add legend explaining liquidity:
    - High liquidity: Foreign currency
    - Medium: SDRs, IMF position
    - Low: Gold (requires selling)
- Tooltip: Show each component's liquidity rating

**Relationship Explored:** Shows reserve diversification and liquid versus illiquid components, with gold and SDRs less liquid than foreign currency reserves for intervention.

---

## **5. POVERTY RATES (6 Charts)**

### **Chart 5.1: Poverty Headcount Ratio (Multiple Thresholds) 2000-2023**

**Chart Type:** Line Chart (Multi-Series)

- **X-Axis:** Year (available survey years only)
- **Y-Axis:** Poverty Rate (% Population)
- **Series 1:** Extreme Poverty $2.15/day (Red line)
- **Series 2:** Moderate Poverty $3.65/day (Orange line)
- **Series 3:** Upper-middle Poverty $6.85/day (Blue line)

**Indicators Needed:**

- `SI.POV.DDAY` (WB) - Poverty at $2.15/day (2017 PPP)
- `SI.POV.UMIC` (WB) - Poverty at $3.65/day (2017 PPP)
- `SI.POV.LMIC` (WB) - Poverty at $6.85/day (2017 PPP)

**PBI Specifics:**

- Lines: Different thickness (Extreme = thickest, 4pt)
- Markers: Circle markers at data points (surveys are not annual)
- Connect only actual survey years, not interpolated
- Data labels: Show values at each survey point
- Add trend lines (dashed) for each series
- Reference line: SDG Target 1.1 (eradicate extreme poverty)
- Tooltip: Show all three poverty rates + survey year
- Note: Add footnote about survey years vs interpolated years

**Relationship Explored:** Tracks extreme and moderate poverty trends over time, assessing whether growth is inclusive and poverty-reducing or whether inequality increases despite GDP growth.

---

### **Chart 5.2: National Poverty Line (Urban vs Rural) Most Recent**

**Chart Type:** Clustered Column Chart with National Average Line

- **X-Axis:** Location (Urban, Rural, National)
- **Y-Axis:** Poverty Rate (%)
- **Columns:** Poverty headcount for each location
- **Line:** National average (horizontal reference line)
- **Colors:** Blue (Urban), Green (Rural), Red (National)

**Indicators Needed:**

- `SI.POV.NAHC` (WB) - National poverty headcount (%)
- `SI.POV.RUHC` (WB) - Rural poverty headcount (%)
- `SI.POV.URHC` (WB) - Urban poverty headcount (%)

**PBI Specifics:**

- Column width: 70%
- Data labels on top of each column
- Add data labels showing absolute number of poor (millions) inside columns
- National average: Thick red horizontal line
- Add annotation: Urban-rural gap = X percentage points
- Conditional formatting: Highlight column with highest poverty in red
- Add secondary chart below: Population share by location (for context)
- Tooltip: Show poverty rate, # of poor, % of total poor population

**Relationship Explored:** Reveals spatial inequality in living standards, showing whether poverty is predominantly rural phenomenon or also significant urban problem requiring different policy responses.

---

### **Chart 5.3: Poverty vs GDP Per Capita Growth (Scatter, Survey Years)**

**Chart Type:** Scatter Plot with Trend Line and Quadrants

- **X-Axis:** GDP Per Capita Growth (% annual)
- **Y-Axis:** Change in Poverty Rate (percentage points)
- **Bubbles:** Each point = survey year
- **Size:** Fixed bubble size
- **Color:** Gradient by year (older = darker)
- **Trend Line:** Linear regression (dashed)

**Indicators Needed:**

- `SI.POV.DDAY` (WB) - Poverty headcount (for change calculation)
- `NY.GDP.PCAP.KD` (WB) - GDP per capita constant US$
- Calculate:
    - Change in poverty between survey periods
    - Annual GDP per capita growth between survey periods

**PBI Specifics:**

- Quadrant lines at median values
- Quadrants labeled:
    - Top-right: High growth, poverty increased (bad)
    - Top-left: Low growth, poverty increased (worst)
    - Bottom-right: High growth, poverty decreased (best, pro-poor growth)
    - Bottom-left: Low growth, poverty decreased (good)
- Trend line with equation and R²
- Data labels: Show survey years
- Tooltip: Survey period, growth rate, poverty change, elasticity
- Add text box: "Growth elasticity of poverty = [calculated value]"

**Relationship Explored:** Tests growth elasticity of poverty reduction—how much GDP per capita growth is needed to reduce poverty by 1 percentage point—revealing inclusiveness of growth.

---

### **Chart 5.4: Poverty Gap and Severity (Most Recent)**

**Chart Type:** Clustered Bar Chart (Horizontal)

- **Y-Axis:** Poverty Measure
    1. Headcount (% poor)
    2. Poverty Gap (% shortfall)
    3. Squared Poverty Gap (severity)
- **X-Axis:** Percentage Value
- **Bars:** All at $2.15/day threshold
- **Colors:** Blue (Headcount), Orange (Gap), Red (Severity)

**Indicators Needed:**

- `SI.POV.DDAY` (WB) - Poverty headcount at $2.15 (%)
- `SI.POV.GAPS` (WB) - Poverty gap at $2.15 (%)
- `SI.POV.GAP2` (WB) - Squared poverty gap (severity) at $2.15

**PBI Specifics:**

- Bars: Horizontal orientation, sorted descending
- Data labels: Inside bars (white text) showing exact values
- Add comparison bars (lighter shade) for regional average
- Annotation: Explain meaning
    - Headcount = % of people below poverty line
    - Gap = Average % shortfall below poverty line
    - Severity = Weighted gap (emphasizes poorest)
- Add calculation in text box: Total poverty gap = Headcount × Gap = resources needed to eliminate poverty
- Tooltip: Show absolute amounts and regional comparison

**Relationship Explored:** Measures depth and severity of poverty beyond headcount, showing whether poor are just below poverty line (gap small) or far below (gap large, requiring major transfers).

---

### **Chart 5.5: Poverty and Inequality Trends (Survey Years)**

**Chart Type:** Dual-Axis Line Chart with Markers

- **X-Axis:** Year (survey years only)
- **Y-Axis (Primary):** Poverty Rate (%)
- **Y-Axis (Secondary):** Gini Coefficient (0-100 scale)
- **Series 1:** Poverty headcount (Blue line, primary)
- **Series 2:** Gini coefficient (Red line, secondary)

**Indicators Needed:**

- `SI.POV.NAHC` (WB) - National poverty headcount
- `SI.POV.GINI` (WB) - Gini index
- Or use country household survey data

**PBI Specifics:**

- Both lines with circle markers at data points
- Primary axis: 0-100% (poverty)
- Secondary axis: 30-70 (typical Gini range)
- Different colors: Blue (poverty), Red (inequality)
- Add quadrant shading:
    - Good zone: Decreasing poverty + decreasing inequality (green)
    - Bad zone: Increasing poverty + increasing inequality (red)
- Data labels at each survey point
- Annotation: Periods of "shared prosperity" vs "unequal growth"
- Tooltip: Show both values + GDP per capita for context

**Relationship Explored:** Tests whether poverty reduction accompanied by falling inequality (shared prosperity) or rising inequality (growth benefiting rich disproportionately).

---

### **Chart 5.6: Regional Poverty Comparison (Most Recent Year)**

**Chart Type:** Bar Chart (Horizontal) with Ranking

- **Y-Axis:** Country names
- **X-Axis:** Poverty Rate at $2.15/day (%)
- **Bars:** Color-coded by performance
    - Green: Below regional average
    - Red: Above regional average
- **Reference Line:** Regional average (vertical)

**Indicators Needed:**

- `SI.POV.DDAY` (WB) - Poverty at $2.15/day for:
    - Zambia
    - Tanzania
    - Malawi
    - Zimbabwe
    - Botswana
    - Mozambique
    - South Africa
    - DRC
    - Calculate: Regional average

**PBI Specifics:**

- Bars: Sorted descending (highest poverty at top)
- Conditional formatting:
    - Above regional avg: Red bars
    - Below regional avg: Green bars
- Data labels: Show exact poverty rate at end of bar
- Zambia bar: Highlighted with bold border
- Add regional average line (dashed vertical)
- Annotation: Zambia's rank (e.g., "4th highest out of 8")
- Tooltip: Show poverty rate + rank + distance from regional avg
- Add year of data in subtitle (surveys may be different years)

**Relationship Explored:** Benchmarks Zambia's poverty performance against regional peers, identifying whether high poverty reflects country-specific factors or broader regional challenges.

---

## **6. DEBT SUSTAINABILITY METRICS (8 Charts)**

### **Chart 6.1: Present Value of Debt-to-GDP Ratio (2015-2023 + Projections to 2029)**

**Chart Type:** Line Chart with Forecast Cone

- **X-Axis:** Year (2015-2029)
- **Y-Axis:** PV Debt-to-GDP (%)
- **Series 1:** Historical PV Debt (Solid blue line)
- **Series 2:** Baseline Projection (Dashed blue line)
- **Forecast Cone:** Shaded area showing uncertainty (light blue)
- **Threshold:** Reference line at 40% (LIC DSF threshold for strong policies)

**Indicators Needed:**

- `PV_Debt_GDP` (IMF DSA) - PV debt-to-GDP ratio
- Or calculate: Discount future debt service using concessional terms
- IMF WEO debt projections

**PBI Specifics:**

- Solid line (2015-2023): Historical, bold 3pt
- Dashed line (2024-2029): Projections, 2pt
- Forecast cone: ±1 standard deviation band, 20% transparency
- Reference lines:
    - 40%: Green (sustainable for strong policy)
    - 55%: Yellow (sustainable for medium policy)
    - 70%: Red (high risk even with strong policy)
- Vertical line at present year (separating history from projection)
- Data labels: Show values at present year and end-year projection
- Tooltip: Show PV debt, nominal debt, discount factor
- Annotation: Policy performance category (Strong/Medium/Weak)

**Relationship Explored:** Assesses long-term debt sustainability by accounting for concessional terms (low-interest loans have lower PV than face value), critical for HIPC/MDRI eligible countries.

---

### **Chart 6.2: PV Debt-to-Exports Ratio (2015-2023)**

**Chart Type:** Area Chart with Threshold Bands

- **X-Axis:** Year (2015-2023)
- **Y-Axis:** PV Debt-to-Exports (%)
- **Area:** Blue gradient fill
- **Threshold Bands:** Background shading
    - Green zone: 0-140%
    - Yellow zone: 140-180%
    - Red zone: 180%+

**Indicators Needed:**

- `DT.DOD.DECT.EX.ZS` (WB IDS) - External debt (% exports)
- Apply PV adjustment using grant element of loans (from DSA)
- Or use IMF DSA indicator if available

**PBI Specifics:**

- Background color bands:
    - <140%: Light green, 20% transparency (low risk)
    - 140-180%: Yellow, 20% transparency (moderate risk)
    - > 180%: Light red, 20% transparency (high risk for debt distress)
        
- Area fill: Blue gradient
- Reference line at 180% (LIC DSF threshold)
- Data labels at peaks and latest year
- Add annotation for major debt relief (HIPC, MDRI) showing drop
- Tooltip: Show PV debt, exports, and ratio
- Add copper price overlay (small line) to show correlation

**Relationship Explored:** Tests whether export earnings are sufficient to service external debt, with threshold of 180% indicating elevated risk of debt distress (IMF/WB LIC DSF).

---

### **Chart 6.3: Debt Service-to-Revenue Ratio (2000-2023)**

**Chart Type:** Column Chart with Threshold Line

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Debt Service-to-Revenue (%)
- **Columns:** Color-coded by threshold
    - Green: <14%
    - Yellow: 14-18%
    - Red: >18%
- **Reference Line:** 18% threshold (LIC DSF)

**Indicators Needed:**

- `DT.AMT.DLXF.CD` (WB IDS) - Principal repayments
- `DT.INT.DLXF.CD` (WB IDS) - Interest payments
- `GC.REV.XGRT.GD.ZS` (WB) - Government revenue (% GDP)
- `NY.GDP.MKTP.CD` (WB) - GDP
- Calculate: (Principal + Interest) / Revenue * 100

**PBI Specifics:**

- Conditional column colors:
    - <14%: Green (low risk)
    - 14-18%: Yellow (moderate risk)
    - > 18%: Red (high risk, debt service crowding out spending)
        
- Data labels on columns
- Reference line at 18% (dashed red)
- Add annotation: "Fiscal space" = Revenue available after debt service
- Tooltip: Show debt service absolute, revenue, ratio, and remaining fiscal space
- Add callout for HIPC completion point (should show drop)

**Relationship Explored:** Measures fiscal burden of debt service crowding out development spending, with 18% threshold indicating fiscal stress (IMF/WB LIC DSF).

---

### **Chart 6.4: Debt Service-to-Exports Ratio (2000-2023)**

**Chart Type:** Line Chart with Area Fill and Threshold

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Debt Service-to-Exports (%)
- **Line:** Red line with markers
- **Area:** Red fill below line (30% transparency)
- **Reference Line:** 15% threshold

**Indicators Needed:**

- `DT.TDS.DECT.EX.ZS` (WB IDS) - Total debt service (% exports)

**PBI Specifics:**

- Line: Red, 3pt thickness
- Area fill: Red gradient, 30% transparency
- Reference lines:
    - 15%: Dashed yellow (moderate risk)
    - 20%: Dashed red (high risk)
- Data labels at peaks and latest year
- Conditional marker colors: Green (<15%), Yellow (15-20%), Red (>20%)
- Annotation: Periods above 15% highlighted
- Tooltip: Show debt service, exports, and remaining foreign exchange after service
- Add export volatility note (showing copper price correlation)

**Relationship Explored:** Tests whether export earnings can service external debt while maintaining import capacity, with 15% threshold indicating external liquidity stress.

---

### **Chart 6.5: External Debt by Maturity (Short-term vs Long-term)**

**Chart Type:** 100% Stacked Area Chart

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Debt Composition (%)
- **Area 1:** Short-term Debt (Red, bottom)
- **Area 2:** Long-term Debt (Blue, top)
- **Line Overlay:** Total External Debt (% GDP, secondary axis)

**Indicators Needed:**

- `DT.DOD.DSTC.CD` (WB IDS) - Short-term external debt
- `DT.DOD.DLTC.CD` (WB IDS) - Long-term external debt
- `DT.DOD.DECT.GN.ZS` (WB IDS) - Total external debt (% GNI) for line

**PBI Specifics:**

- Primary axis: 0-100% (composition)
- Secondary axis: 0-100% (debt-to-GDP)
- Area colors: Red (short-term, concerning), Blue (long-term, safer)
- Line: Black dashed, 2pt
- Add reference line on secondary axis: 60% (debt threshold)
- Tooltip: Show composition %, absolute amounts, average maturity
- Data labels: Short-term debt % at key years
- Annotation: Highlight when short-term >30% (refinancing risk)

**Relationship Explored:** Assesses rollover risk, as short-term debt must be refinanced frequently, creating vulnerability to sudden stops in capital flows or rising interest rates.

---

### **Chart 6.6: Concessional vs Non-Concessional Debt (2000-2023)**

**Chart Type:** 100% Stacked Column Chart

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Debt Composition (%)
- **Segment 1:** Concessional Debt (Blue)
- **Segment 2:** Non-Concessional Debt (Red)

**Indicators Needed:**

- `DT.DOD.ALLC.CD` (WB IDS) - Concessional debt
- `DT.DOD.DECT.CD` (WB IDS) - Total external debt
- Calculate: Non-concessional = Total - Concessional

**PBI Specifics:**

- Columns: 100% stacked, width 90%
- Colors: Blue (concessional, good), Red (non-concessional, expensive)
- Data labels: Show % for both segments
- Add line overlay: Average interest rate (secondary axis, line chart)
- Tooltip: Show composition, absolute amounts, avg interest for each type
- Annotation: Highlight shift from concessional to commercial
- Add callout: "Graduation" from concessional lending (if applicable)
- Note: Explain concessional = grant element >25%

**Relationship Explored:** Tracks shift from concessional (low-interest, long-maturity) multilateral/bilateral loans to expensive commercial debt, increasing debt service burden.

---

### **Chart 6.7: Interest Payments (% Exports and % Revenue) 2000-2023**

**Chart Type:** Dual-Axis Line Chart

- **X-Axis:** Year (2000-2023)
- **Y-Axis (Primary):** Interest (% Revenue)
- **Y-Axis (Secondary):** Interest (% Exports)
- **Series 1:** Interest/Revenue (Red line, primary)
- **Series 2:** Interest/Exports (Blue line, secondary)

**Indicators Needed:**

- `DT.INT.DECT.EX.ZS` (WB IDS) - Interest (% exports)
- `DT.INT.DECT.GN.ZS` (WB IDS) - Interest (% GNI)
- Government revenue data to calculate Interest/Revenue

**PBI Specifics:**

- Both axes: 0-15% range
- Line thickness: 3pt for both
- Reference lines:
    - Primary axis: 5% (elevated), 10% (high)
    - Secondary axis: 3% (elevated), 5% (high)
- Markers at data points
- Tooltip: Show interest absolute, revenue, exports, both ratios
- Annotation: Periods of high burden (>10% revenue) highlighted
- Add average interest rate as text annotation

**Relationship Explored:** Isolates interest burden from principal repayments, showing whether debt service problem is interest rates versus amortization schedule.

---

### **Chart 6.8: Debt Distress Signal Dashboard (Most Recent Year)**

**Chart Type:** Gauge Chart Array (2x2 Grid) OR Traffic Light Matrix

- **4 Gauges:**
    1. PV Debt-to-GDP
    2. PV Debt-to-Exports
    3. Debt Service-to-Revenue
    4. Debt Service-to-Exports
- Each showing: Green/Yellow/Red zones with needle at actual value

**Indicators Needed:**

- `PV_Debt_GDP` (calculated or IMF DSA)
- PV Debt-to-Exports (calculated)
- Debt Service-to-Revenue (calculated from WB IDS + GFS)
- `DT.TDS.DECT.EX.ZS` (WB IDS) - DS-to-Exports

**PBI Specifics:**

**Gauge 1 - PV Debt-to-GDP:**

- Green: 0-40% (sustainable)
- Yellow: 40-55% (elevated)
- Red: 55%+ (high risk)
- Threshold: 40% for strong policy, 55% for medium

**Gauge 2 - PV Debt-to-Exports:**

- Green: 0-140%
- Yellow: 140-180%
- Red: 180%+
- Threshold: 180%

**Gauge 3 - DS-to-Revenue:**

- Green: 0-14%
- Yellow: 14-18%
- Red: 18%+
- Threshold: 18%

**Gauge 4 - DS-to-Exports:**

- Green: 0-12%
    
- Yellow: 12-15%
    
- Red: 15%+
    
- Threshold: 15%
    
- Add overall risk rating text box: "DEBT DISTRESS RISK: [LOW/MODERATE/HIGH]"
    
- Color-code based on number of indicators in red zone
    
- Add year label
    
- Tooltip: Show threshold values and Zambia's distance from threshold
    
- Add footnote: LIC DSF framework thresholds
    

**Relationship Explored:** Multi-indicator risk dashboard comparing all sustainability metrics to IMF/WB thresholds to assess overall debt distress risk.

---

## **7. BANKING SECTOR SOUNDNESS (7 Charts)**

### **Chart 7.1: Capital Adequacy Ratio (2010-2023)**

**Chart Type:** Line Chart with Threshold Band

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** Capital Adequacy Ratio (%)
- **Line:** Blue line with markers
- **Threshold Bands:**
    - Red zone: 0-8% (below Basel minimum)
    - Yellow zone: 8-10.5%
    - Green zone: 10.5%+ (well-capitalized)

**Indicators Needed:**

- `FSIB1_PT` (IMF FSI) - Regulatory capital to risk-weighted assets (%)
- `FB.BNK.CAPA.ZS` (WB) - Bank capital to assets ratio (%)

**PBI Specifics:**

- Background shading:
    - <8%: Red, 30% transparency (undercapitalized)
    - 8-10.5%: Yellow, 30% transparency (adequately capitalized)
    - > 10.5%: Green, 30% transparency (well-capitalized)
        
- Line: Blue, 3pt thickness, with circle markers
- Reference lines:
    - 8%: Basel III minimum (dashed red)
    - 10.5%: Well-capitalized (dashed green)
- Data labels at key years and latest value
- Tooltip: Show CAR, Tier 1 ratio if available, and Basel requirement
- Add annotation for regulatory changes or banking crises

**Relationship Explored:** Assesses banking system solvency and ability to absorb losses, with Basel III minimum 8% for capital/RWA, higher indicating greater safety buffer.

---

### **Chart 7.2: Non-Performing Loans Ratio (2010-2023)**

**Chart Type:** Area Chart with Threshold Line

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** NPL Ratio (%)
- **Area:** Red gradient fill (intensity increases with NPL level)
- **Reference Lines:**
    - 5%: Yellow (elevated)
    - 10%: Red (problematic)

**Indicators Needed:**

- `FSIB4_PT` (IMF FSI) - NPLs to total gross loans (%)
- `FB.AST.NPER.ZS` (WB) - NPLs to total loans (%)

**PBI Specifics:**

- Area fill: Conditional color intensity
    - <5%: Light orange
    - 5-10%: Orange
    - > 10%: Dark red
        
- Reference lines:
    - 5%: Dashed yellow (watch level)
    - 10%: Dashed red (crisis level)
- Data labels at peaks and latest year
- Markers: Circle at each data point
- Tooltip: Show NPL ratio, absolute NPL amount, provision coverage ratio
- Add economic recession shading (gray boxes) to show correlation
- Annotation: Sectoral NPL breakdown if available

**Relationship Explored:** Tracks asset quality deterioration indicating economic stress or weak credit underwriting, with NPL>10% signaling significant problems.

---

### **Chart 7.3: Return on Assets and Return on Equity (2010-2023)**

**Chart Type:** Dual-Axis Line Chart

- **X-Axis:** Year (2010-2023)
- **Y-Axis (Primary):** ROA (%)
- **Y-Axis (Secondary):** ROE (%)
- **Series 1:** ROA (Blue line, primary)
- **Series 2:** ROE (Orange line, secondary)

**Indicators Needed:**

- `FSIB7_PT` (IMF FSI) - Return on assets (%)
- `FSIB8_PT` (IMF FSI) - Return on equity (%)

**PBI Specifics:**

- Primary axis: -2% to 5% (ROA typically lower)
- Secondary axis: -10% to 30% (ROE typically higher)
- Lines: Both 3pt thickness with markers
- Reference lines:
    - ROA: 1% (minimum acceptable, primary axis)
    - ROE: 15% (competitive, secondary axis)
- Data labels at latest year
- Conditional formatting: Red markers when negative
- Tooltip: Show both profitability metrics + efficiency ratio
- Add regional average lines (dashed) for comparison
- Annotation: Highlight periods of low/negative profitability

**Relationship Explored:** Measures banking sector profitability and efficiency, with declining ROA/ROE indicating deteriorating earnings capacity threatening capital adequacy.

---

### **Chart 7.4: NPLs Net of Provisions to Capital (2010-2023)**

**Chart Type:** Column Chart with Threshold Line

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** NPL Net of Provisions to Capital (%)
- **Columns:** Color-coded by threshold
    - Green: <30%
    - Yellow: 30-100%
    - Red: >100% (capital impairment)

**Indicators Needed:**

- `FSIB5_GDP` (IMF FSI) - NPLs net of provisions to capital (%)

**PBI Specifics:**

- Conditional column colors:
    - <30%: Green (healthy)
    - 30-100%: Yellow (stressed)
    - > 100%: Red (technically insolvent if all NPLs written off)
        
- Reference lines:
    - 50%: Yellow dashed (watch level)
    - 100%: Red dashed (insolvency threshold)
- Data labels on all columns
- Add provision coverage ratio as secondary data label
- Tooltip: Show NPLs gross, provisions, capital, and ratio
- Annotation: Explain "If all NPLs written off today, bank would lose X% of capital"

**Relationship Explored:** Tests whether banks have adequate capital to absorb losses from bad loans after provisions, with ratio >100% indicating insolvency if all NPLs written off.

---

### **Chart 7.5: Liquid Assets to Total Assets (2010-2023)**

**Chart Type:** Area Chart with Dual Reference Lines

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** Liquidity Ratio (%)
- **Area:** Blue gradient fill
- **Reference Lines:**
    - 20%: Minimum (red dashed)
    - 30%: Comfortable (green dashed)

**Indicators Needed:**

- `FSIB11_PT` (IMF FSI) - Liquid assets to total assets (%)
- `FSIB12_PT` (IMF FSI) - Liquid assets to short-term liabilities (%)

**PBI Specifics:**

- Area fill: Conditional gradient
    - <20%: Light red gradient
    - 20-30%: Yellow gradient
    - > 30%: Green gradient
        
- Reference lines:
    - 20%: Red dashed (minimum prudential)
    - 30%: Green dashed (comfortable buffer)
- Data labels at key points and latest year
- Add second series (line): Liquid assets to short-term liabilities (secondary axis)
- Tooltip: Show both liquidity metrics + loan-to-deposit ratio
- Annotation: Highlight liquidity stress periods

**Relationship Explored:** Assesses banking system liquidity and ability to meet deposit withdrawals, with low ratios indicating vulnerability to bank runs.

---

### **Chart 7.6: Domestic Credit to Private Sector (% GDP) 2000-2023**

**Chart Type:** Area Chart with Benchmark Comparison

- **X-Axis:** Year (2000-2023)
- **Y-Axis:** Credit to Private Sector (% GDP)
- **Area:** Blue gradient fill (Zambia)
- **Line Overlay:** Regional average (dashed orange)
- **Reference Line:** 30% (financial deepening threshold)

**Indicators Needed:**

- `FS.AST.PRVT.GD.ZS` (WB) - Domestic credit to private sector (% GDP)
- `FD.AST.PRVT.GD.ZS` (WB) - Credit to private sector by banks (% GDP)
- Same indicators for regional countries for average

**PBI Specifics:**

- Zambia area: Blue gradient, 50% transparency
- Regional average line: Orange dashed, 2pt
- Reference lines:
    - 30%: Green (minimum for development)
    - 50%: Blue (emerging market average)
- Data labels: Zambia values at key years
- Tooltip: Show credit-to-GDP, gap to regional average, credit growth rate
- Annotation: Periods of credit boom/bust
- Add secondary chart: Credit growth rate (% YoY) as small line

**Relationship Explored:** Measures financial deepening and credit availability for private investment, with low ratios (<20% GDP) indicating financial underdevelopment constraining growth.

---

### **Chart 7.7: Interest Rate Spread (Lending minus Deposit Rate) 2010-2023**

**Chart Type:** Area Chart with Efficiency Benchmark

- **X-Axis:** Year (2010-2023)
- **Y-Axis:** Interest Rate (%)
- **Area 1:** Lending Rate (Red, upper bound)
- **Area 2:** Deposit Rate (Blue, lower bound)
- **Spread:** Shaded area between (yellow/orange)

**Indicators Needed:**

- `FR.INR.LEND` (WB) - Lending interest rate (%)
- `FR.INR.DPST` (WB) - Deposit interest rate (%)
- Calculate: Spread = Lending - Deposit

**PBI Specifics:**

- Two area charts:
    - Top area: Lending rate (red line with red area above)
    - Bottom area: Deposit rate (blue line with blue area below)
    - Between: Spread (shaded yellow/orange, the key focus)
- Reference line: 10 percentage points (high spread threshold)
- Data labels: Show spread value at each year
- Tooltip: Show lending rate, deposit rate, spread, and regional comparison
- Add regional average spread as dashed line
- Conditional shading: Spread area intensity based on value
    - <5 pp: Light yellow (efficient)
    - 5-10 pp: Orange (moderate inefficiency)
    - > 10 pp: Red (high inefficiency)
        
- Annotation: Label periods with specific drivers (e.g., NPL spike, monetary tightening)

**Relationship Explored:** Assesses banking efficiency and competitiveness, with high spreads (>10 percentage points) indicating monopolistic pricing, high risk premiums, or operational inefficiency.

---

## **SUMMARY TABLE OF ALL 77 CHARTS**

|**Section**|**Charts**|**Primary Chart Types**|
|---|---|---|
|**1. Inflation (8)**|1.1-1.8|Line (4), Scatter (1), Dual-axis (2), Heatmap (1)|
|**2. Fiscal (12)**|2.1-2.12|Line (4), Area (3), Donut (1), Stacked Bar (2), Column (2)|
|**3. Balance of Payments (10)**|3.1-3.10|Area (4), Line (2), Waterfall (2), Stacked (2), Table (1)|
|**4. Reserves (6)**|4.1-4.6|Area (2), Line (2), Dual-axis (1), Gauge (1), Donut (1)|
|**5. Poverty (6)**|5.1-5.6|Line (2), Column (1), Scatter (1), Bar (2)|
|**6. Debt Sustainability (8)**|6.1-6.8|Line (2), Area (3), Column (1), Stacked (2), Gauge (1)|
|**7. Banking (7)**|7.1-7.7|Line (2), Area (5), Dual-axis (2), Column (1)|
|**9. Projections (10)**|9.1-9.10|Line (8), Fan Chart (1), Gauge/Scenario (2)|
|**10. Fiscal Composition (10)**|10.1-10.10|Donut (1), Line (3), Column (3), Stacked (2), Treemap (1), Matrix (1)|



## **Database Summary**

| **Database**        | **Total Indicators** | **% of Total** | **Charts Primarily Using** | **Notes**                                             |
| ------------------- | -------------------- | -------------- | -------------------------- | ----------------------------------------------------- |
| **IMF WEO**         | 45                   | 22%            | 25 charts                  | **WE HAVE**<br>Includes projections; macro aggregates |
| **IMF GFS**         | 50                   | 25%            | 15 charts                  | Fiscal revenue/expenditure detail                     |
| **IMF BOPS**        | 30                   | 15%            | 10 charts                  | **MIGHT HAVE Balance** of payments components         |
| **IMF IFS**         | 20                   | 10%            | 8 charts                   | **WE HAVE**  Monetary, inflation, reserves            |
| **IMF FSI**         | 13                   | 6%             | 7 charts                   | Banking sector soundness                              |
| **WB WDI**          | 35                   | 17%            | 30 charts                  | **WE HAVE** cross-cutting indicators                  |
| **WB IDS**          | 25                   | 12%            | 12 charts                  | **WE HAVE** Debt statistics                           |
| **WB Poverty**      | 9                    | 4%             | 6 charts                   | Poverty data                                          |
| **IMF DSA**         | 5                    | 2%             | 3 charts                   | Debt sustainability custom                            |
| **Country Sources** | ~10                  | 5%             | Variable                   | Gaps, real-time data                                  |

---

## **POWER BI IMPLEMENTATION NOTES**

### **General PBI Best Practices for All Charts:**

1. **Date Table:** Create calendar table for time-based charts
2. **Measures:** Create DAX measures for all calculated ratios
3. **Tooltips:** Custom tooltips showing multiple related metrics
4. **Drill-through:** Enable drill-through from summary to detail charts
5. **Bookmarks:** Create bookmarks for different views (historical vs projected)
6. **Slicers:** Add year range slicers for user control
7. **Conditional Formatting:** Use rules-based formatting for thresholds
8. **Reference Lines:** Use analytics pane for threshold lines
9. **Annotations:** Use text boxes or callouts for context
10. **Color Consistency:** Maintain color scheme across all charts (Blue=positive/assets, Red=negative/liabilities, Green=thresholds met)

### **Specific PBI Features to Utilize:**

- **Forecast:** Use PBI built-in forecasting for projection charts
- **Clustering:** For scatter plots, enable automatic clustering
- **Hierarchies:** Create year→quarter→month hierarchy for drill-down
- **Parameters:** What-if parameters for scenario analysis
- **R/Python Visuals:** For advanced statistical charts (regression, fan charts)
- **Key Influencers:** To analyze drivers of changes
- **Decomposition Tree:** For fiscal composition analysis
- **Smart Narratives:** Auto-generated insights for each page

This comprehensive specification provides everything needed to implement all 77 Tier 1 charts in Power BI with professional quality suitable for IMF-level reporting.