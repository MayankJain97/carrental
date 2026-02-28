import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random
from datetime import datetime

# ─── Sample Data ─────────────────────────────────────────────────────────────
SAMPLE_DATA = {
    "sales": pd.DataFrame({
        "customer_id": range(1, 101),
        "customer_name": [f"Customer_{i}" for i in range(1, 101)],
        "region": np.random.choice(["North", "South", "East", "West"], 100),
        "product": np.random.choice(["Product A", "Product B", "Product C", "Product D"], 100),
        "sale_amount": np.random.uniform(100, 50000, 100).round(2),
        "quantity": np.random.randint(1, 100, 100),
        "sale_date": pd.date_range("2024-01-01", periods=100, freq="3D").strftime("%Y-%m-%d"),
    }),
    "customers": pd.DataFrame({
        "customer_id": range(1, 51),
        "name": [f"Customer_{i}" for i in range(1, 51)],
        "segment": np.random.choice(["Enterprise", "SMB", "Startup"], 50),
        "country": np.random.choice(["USA", "UK", "Germany", "India", "Australia"], 50),
        "lifetime_value": np.random.uniform(5000, 500000, 50).round(2),
        "churn_risk": np.random.choice(["Low", "Medium", "High"], 50),
    }),
    "finance": pd.DataFrame({
        "month": pd.date_range("2024-01-01", periods=12, freq="MS").strftime("%Y-%m"),
        "revenue": np.random.uniform(3000000, 6000000, 12).round(2),
        "expenses": np.random.uniform(2000000, 4000000, 12).round(2),
        "profit": np.random.uniform(500000, 2000000, 12).round(2),
        "department": np.random.choice(["Sales", "Ops", "HR", "IT"], 12),
    }),
}

# ─── NL2SQL Engine ────────────────────────────────────────────────────────────
NL2SQL_RESPONSES = {
    "total sales": {
        "sql": "SELECT SUM(sale_amount) AS total_sales, COUNT(*) AS total_orders\nFROM sales_transactions\nWHERE sale_date >= '2024-01-01';",
        "insight": "💡 **AI Insight**: Total sales are **$2.47M** across **100 transactions**. The average order value is **$24,700**. Sales are trending **+12.4%** vs last period.",
        "data_key": "sales",
        "chart_type": "bar",
        "chart_col": "region",
        "chart_val": "sale_amount",
    },
    "top customers": {
        "sql": "SELECT customer_name, SUM(sale_amount) AS total_revenue,\n       COUNT(*) AS orders\nFROM sales_transactions\nGROUP BY customer_name\nORDER BY total_revenue DESC\nLIMIT 10;",
        "insight": "💡 **AI Insight**: Top 10 customers contribute **38%** of total revenue. Customer concentration risk is **Medium**. Recommend loyalty program for top 5.",
        "data_key": "customers",
        "chart_type": "bar",
        "chart_col": "name",
        "chart_val": "lifetime_value",
    },
    "revenue by region": {
        "sql": "SELECT region, SUM(sale_amount) AS revenue,\n       COUNT(*) AS transactions,\n       AVG(sale_amount) AS avg_order_value\nFROM sales_transactions\nGROUP BY region\nORDER BY revenue DESC;",
        "insight": "💡 **AI Insight**: **North region** leads with 32% of revenue. **West region** shows fastest growth at +18% QoQ. Recommend increasing sales headcount in West.",
        "data_key": "sales",
        "chart_type": "pie",
        "chart_col": "region",
        "chart_val": "sale_amount",
    },
    "monthly revenue": {
        "sql": "SELECT DATE_TRUNC('month', sale_date) AS month,\n       SUM(sale_amount) AS monthly_revenue,\n       COUNT(*) AS orders\nFROM sales_transactions\nGROUP BY month\nORDER BY month;",
        "insight": "💡 **AI Insight**: Revenue shows **seasonal pattern** with peaks in Q4. **December** is historically the strongest month (+34% vs average). Plan inventory accordingly.",
        "data_key": "finance",
        "chart_type": "line",
        "chart_col": "month",
        "chart_val": "revenue",
    },
    "churn risk": {
        "sql": "SELECT churn_risk, COUNT(*) AS customers,\n       AVG(lifetime_value) AS avg_ltv\nFROM customer_master\nGROUP BY churn_risk\nORDER BY CASE churn_risk WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END;",
        "insight": "💡 **AI Insight**: **23% of customers** are at High churn risk, representing **$4.2M** in at-risk revenue. Immediate retention campaign recommended for High-risk segment.",
        "data_key": "customers",
        "chart_type": "bar",
        "chart_col": "churn_risk",
        "chart_val": "lifetime_value",
    },
    "profit margin": {
        "sql": "SELECT department,\n       SUM(revenue) AS total_revenue,\n       SUM(expenses) AS total_expenses,\n       SUM(profit) AS total_profit,\n       ROUND(SUM(profit)/SUM(revenue)*100, 2) AS profit_margin_pct\nFROM finance_gl\nGROUP BY department\nORDER BY profit_margin_pct DESC;",
        "insight": "💡 **AI Insight**: Overall profit margin is **28.4%**, above industry average of 22%. **Sales dept** has highest margin at 34%. Recommend cost optimization in IT dept (margin: 18%).",
        "data_key": "finance",
        "chart_type": "bar",
        "chart_col": "month",
        "chart_val": "profit",
    },
}

def get_nl2sql_response(question):
    question_lower = question.lower()
    for key, response in NL2SQL_RESPONSES.items():
        if any(word in question_lower for word in key.split()):
            return response
    # Default response
    return {
        "sql": f"-- AI-Generated SQL for: {question}\nSELECT *\nFROM data_platform.analytics\nWHERE created_date >= CURRENT_DATE - INTERVAL '30 days'\nLIMIT 1000;",
        "insight": f"💡 **AI Insight**: Query generated for '{question}'. The platform analyzed your request and identified relevant data sources. Results show interesting patterns worth investigating further.",
        "data_key": "sales",
        "chart_type": "bar",
        "chart_col": "region",
        "chart_val": "sale_amount",
    }

def render_chart(response):
    data = SAMPLE_DATA[response["data_key"]]
    chart_type = response["chart_type"]
    col = response["chart_col"]
    val = response["chart_val"]
    
    if col not in data.columns or val not in data.columns:
        return None
    
    grouped = data.groupby(col)[val].sum().reset_index()
    
    if chart_type == "bar":
        fig = go.Figure(go.Bar(
            x=grouped[col], y=grouped[val],
            marker=dict(color=grouped[val], colorscale=[[0, '#0f3460'], [1, '#00d4ff']], showscale=False),
            text=[f'${v:,.0f}' if v > 1000 else str(v) for v in grouped[val]],
            textposition='outside',
            textfont=dict(color='#aabbcc', size=10),
        ))
    elif chart_type == "pie":
        fig = go.Figure(go.Pie(
            labels=grouped[col], values=grouped[val],
            hole=0.4,
            marker=dict(colors=['#00d4ff', '#00ff88', '#ff6b6b', '#ffd700', '#ff88ff']),
        ))
    elif chart_type == "line":
        fig = go.Figure(go.Scatter(
            x=grouped[col], y=grouped[val],
            line=dict(color='#00d4ff', width=3),
            fill='tozeroy', fillcolor='rgba(0,212,255,0.1)',
            mode='lines+markers',
            marker=dict(color='#00d4ff', size=8),
        ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#aabbcc'),
        xaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
        yaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
        margin=dict(l=0, r=0, t=10, b=0),
        height=280,
    )
    return fig

# ─── Main Page ────────────────────────────────────────────────────────────────
def show():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #533483, #0f3460); border-radius:16px; padding:24px; margin-bottom:24px;'>
        <div style='font-size:1.8rem; font-weight:800; color:white;'>🤖 AI Data Chatbot</div>
        <div style='color:#ccddff; margin-top:6px;'>Natural Language → SQL → Insights | Ask anything about your data</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Chat Interface
        st.markdown('<div class="section-header">💬 Chat with Your Data</div>', unsafe_allow_html=True)
        
        # Initialize chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                {
                    "role": "bot",
                    "content": "👋 Hello! I'm your **AI Data Assistant**. I can help you:\n\n• 📊 Query your data in plain English\n• 🔍 Generate SQL automatically\n• 📈 Create instant visualizations\n• 💡 Provide AI-powered insights\n\nTry asking: *'Show me total sales by region'* or *'Which customers have high churn risk?'*"
                }
            ]
        
        # Display chat history
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-user">
                        <strong>👤 You</strong><br>{msg["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-bot">
                        <strong>🤖 AI Assistant</strong><br>{msg["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if "sql" in msg:
                        with st.expander("📝 Generated SQL", expanded=False):
                            st.code(msg["sql"], language="sql")
                    
                    if "chart" in msg and msg["chart"] is not None:
                        st.plotly_chart(msg["chart"], use_container_width=True)
                    
                    if "dataframe" in msg:
                        st.dataframe(msg["dataframe"].head(8), use_container_width=True, hide_index=True)
        
        # Input
        st.markdown("---")
        
        # Quick question buttons
        st.markdown("**💡 Quick Questions:**")
        quick_cols = st.columns(3)
        quick_questions = [
            "Show total sales by region",
            "Who are the top customers?",
            "What is the monthly revenue trend?",
            "Show churn risk analysis",
            "Revenue by product",
            "Profit margin by department",
        ]
        
        for i, q in enumerate(quick_questions):
            with quick_cols[i % 3]:
                if st.button(f"💬 {q}", key=f"quick_{i}", use_container_width=True):
                    st.session_state.pending_question = q
        
        # Text input
        user_input = st.text_input(
            "Ask your data question...",
            placeholder="e.g., Show me total sales by region for last quarter",
            key="chat_input",
            label_visibility="collapsed"
        )
        
        col_send, col_clear = st.columns([3, 1])
        with col_send:
            send_btn = st.button("🚀 Ask AI", use_container_width=True, type="primary")
        with col_clear:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.chat_history = [st.session_state.chat_history[0]]
                st.rerun()
        
        # Process question
        question = None
        if send_btn and user_input:
            question = user_input
        elif hasattr(st.session_state, 'pending_question') and st.session_state.pending_question:
            question = st.session_state.pending_question
            st.session_state.pending_question = None
        
        if question:
            # Add user message
            st.session_state.chat_history.append({"role": "user", "content": question})
            
            # Get AI response
            response = get_nl2sql_response(question)
            
            # Build bot message
            bot_msg = {
                "role": "bot",
                "content": f"I've analyzed your question and generated the following:\n\n{response['insight']}",
                "sql": response["sql"],
                "chart": render_chart(response),
                "dataframe": SAMPLE_DATA[response["data_key"]],
            }
            
            st.session_state.chat_history.append(bot_msg)
            st.rerun()
    
    with col2:
        # AI Capabilities Panel
        st.markdown('<div class="section-header">🧠 AI Capabilities</div>', unsafe_allow_html=True)
        
        capabilities = [
            ("🔤→🔢", "NL to SQL", "Convert plain English to optimized SQL queries"),
            ("📊", "Auto Charts", "Automatically select best visualization"),
            ("💡", "Smart Insights", "AI-generated business insights"),
            ("🔍", "Anomaly Detection", "Spot unusual patterns in data"),
            ("📈", "Forecasting", "Predict future trends"),
            ("🏷️", "Auto Tagging", "Classify and tag data automatically"),
        ]
        
        for icon, title, desc in capabilities:
            st.markdown(f"""
            <div style='background:#1a1a3e; border:1px solid #334466; border-radius:10px; padding:12px; margin-bottom:8px;'>
                <div style='font-size:1.2rem;'>{icon} <strong style='color:#00d4ff;'>{title}</strong></div>
                <div style='font-size:0.78rem; color:#8899bb; margin-top:4px;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Sample Questions
        st.markdown('<div class="section-header">📚 Sample Questions</div>', unsafe_allow_html=True)
        
        sample_qs = [
            "What is our total revenue this quarter?",
            "Show me customers at risk of churning",
            "Which product has the highest margin?",
            "Compare sales performance by region",
            "What are the top 10 transactions?",
            "Show monthly expense trends",
            "Which department is most profitable?",
            "Find anomalies in sales data",
        ]
        
        for q in sample_qs:
            st.markdown(f"""
            <div style='background:#0d1b2a; border:1px solid #1e3a5f; border-radius:8px; padding:8px 12px; margin:4px 0; font-size:0.8rem; color:#8899bb;'>
                💬 {q}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Stats
        st.markdown('<div class="section-header">📊 Usage Stats</div>', unsafe_allow_html=True)
        st.metric("Queries Today", "1,247", "+23%")
        st.metric("Avg Response Time", "0.8s", "-45%")
        st.metric("User Satisfaction", "4.8/5", "+0.2")
