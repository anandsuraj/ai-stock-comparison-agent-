# AI Investment Agent for Indian Stocks 📈🤖

A Streamlit-based application that compares two Indian stocks using fundamental analysis, market performance data, and analyst recommendations.

## Features

- Comparative analysis of any two Indian stocks listed on NSE/BSE
- Real-time market data including prices and 52-week ranges
- Fundamental metrics (P/E ratio, P/B ratio, EPS, Market Cap)
- Analyst recommendation trends
- Sector-specific insights
- Risk assessment for Indian market conditions
- Long-term growth potential analysis

## Installation

1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Obtain an [OpenAI API key](https://platform.openai.com/api-keys)
2. Run the application:
   ```bash
   streamlit run investment_agent.py
   ```
3. Enter your OpenAI API key in the app
4. Input two Indian stock symbols in NSE format (e.g., `RELIANCE.NS`, `TCS.NS`)

## Example Inputs

Popular Indian stocks to compare:

| Sector        | Example Stocks               |
|---------------|------------------------------|
| Banking       | `HDFCBANK.NS`, `ICICIBANK.NS`|
| IT            | `TCS.NS`, `INFY.NS`          |
| Energy        | `RELIANCE.NS`, `ONGC.NS`     |
| Automobile    | `MARUTI.NS`, `TATAMOTORS.NS` |

## Sample Output

The app generates a comprehensive report including:
- Current market performance comparison
- Fundamental analysis (valuation ratios, profitability)
- Analyst recommendation trends
- Sector-specific growth potential
- Indian market risk factors
- Long-term investment outlook

## Requirements

- Python 3.8+
- Streamlit
- agno package
- yfinance (via agno tools)
- OpenAI API access

## Limitations

- Data depends on Yahoo Finance's availability
- Indian stocks must use `.NS` (NSE) or `.BO` (BSE) suffix
- Analysis quality depends on OpenAI model capabilities

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.