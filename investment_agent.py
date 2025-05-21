import os
import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

st.title("AI Investment Agent for Indian Stocks 📈")
st.caption("This app allows you to compare the performance of two Indian stocks and generate detailed reports.")

openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    assistant = Agent(
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        tools=[
            YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)
        ],
        show_tool_calls=True,
        description="You are an investment analyst specializing in Indian equities that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=[
            "Format your response using markdown and use tables to display data where possible.",
            "Focus on metrics relevant to Indian market investors.",
            "Include sector-specific analysis for Indian industries ."
        ],
    )

    st.info("For Indian stocks, use NSE symbols with .NS suffix (e.g., RELIANCE.NS, TCS.NS)")
    
    col1, col2 = st.columns(2)
    with col1:
        stock1 = st.text_input("Enter first Indian stock symbol (e.g. RELIANCE.NS)")
    with col2:
        stock2 = st.text_input("Enter second Indian stock symbol (e.g. TCS.NS)")

    if stock1 and stock2:
        with st.spinner(f"Analyzing {stock1} and {stock2}..."):
            query = f"""Compare both the Indian stocks - {stock1} and {stock2} and make a detailed report including:
            - Current market performance
            - Fundamental analysis (P/E, P/B, ROE, etc.)
            - Analyst recommendations
            - Sector comparison
            - Risk factors specific to Indian market
            - Long-term growth potential in Indian context"""
            response = assistant.run(query, stream=False)
            st.markdown(response.content)