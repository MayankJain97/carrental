import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time
import random
from datetime import datetime

def show():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0f3460, #1a5276); border-radius:16px; padding:24px; margin-bottom:24px;'>
        <div style='font-size:1.8rem; font-weight:800; color:white;'>🔄 Data Ingestion Hub</div>
        <div style='color:#ccddff; margin-top:6px;'>Multi-Source Data Ingestion | 20+ Connectors | Real-time & Batch</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["📥 Ingest Data", "🔌 Connectors", "📊 Pipeline Monitor", "📋 Data Catalog"])

    # ─── TAB 1: Ingest Data ───────────────────────────────────────────────────
    with tabs[0]:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown('<div class="section-header">⚙️ Configure Ingestion</div>', unsafe_allow_html=True)
            
            source_type = st.selectbox("📂 Source Type", [
                "📄 CSV / Excel File", "🗄️ SQL Database", "🌐 REST API",
                "☁️ AWS S3 / Azure Blob", "📡 Kafka Stream", "🔗 Salesforce CRM",
                "📊 Google Analytics", "🏭 SAP ERP", "📧 Email / SFTP"
            ])
            
            if "CSV" in source_type or "Excel" in source_type:
                uploaded = st.file_uploader("Upload File", type=['csv', 'xlsx', 'json'])
                if uploaded:
                    try:
                        if uploaded.name.endswith('.csv'):
                            df = pd.read_csv(uploaded)
                        else:
                            df = pd.read_excel(uploaded)
                        st.success(f"✅ File loaded: {len(df)} rows × {len(df.columns)} columns")
                        st.dataframe(df.head(5), use_container_width=True)
                    except Exception as e:
                        st.error(f"Error: {e}")
            
            elif "SQL" in source_type:
                db_type = st.selectbox("Database", ["PostgreSQL", "MySQL", "SQL Server", "Oracle", "Snowflake", "BigQuery"])
                host = st.text_input("Host", placeholder="db.company.com")
                db_name = st.text_input("Database Name", placeholder="analytics_db")
                query = st.text_area("SQL Query", placeholder="SELECT * FROM sales_data WHERE date >= '2024-01-01'", height=100)
            
            elif "API" in source_type:
                api_url = st.text_input("API Endpoint", placeholder="https://api.example.com/data")
                auth_type = st.selectbox("Auth Type", ["None", "API Key", "OAuth 2.0", "Bearer Token"])
                if auth_type != "None":
                    st.text_input("Token / Key", type="password")
            
            elif "Kafka" in source_type:
                broker = st.text_input("Kafka Broker", placeholder="kafka.company.com:9092")
                topic = st.text_input("Topic", placeholder="sales-events")
                consumer_group = st.text_input("Consumer Group", placeholder="analytics-group")
            
            else:
                st.text_input("Connection String / URL", placeholder="Enter connection details...")
            
            st.markdown("---")
            
            target = st.selectbox("🎯 Target Destination", [
                "🏪 Data Lake (Azure ADLS)", "❄️ Snowflake Data Warehouse",
                "🔴 Amazon Redshift", "📦 Delta Lake", "🗄️ PostgreSQL Analytics DB"
            ])
            
            col_a, col_b = st.columns(2)
            with col_a:
                mode = st.selectbox("Load Mode", ["Full Load", "Incremental", "CDC (Change Data Capture)"])
            with col_b:
                schedule = st.selectbox("Schedule", ["Manual", "Every 15 min", "Hourly", "Daily", "Weekly"])
            
            if st.button("🚀 Start Ingestion Pipeline", use_container_width=True):
                with st.spinner("Initializing pipeline..."):
                    progress = st.progress(0)
                    status_text = st.empty()
                    
                    steps = [
                        (10, "🔌 Connecting to source..."),
                        (25, "🔍 Validating schema..."),
                        (40, "📥 Extracting data..."),
                        (60, "🔧 Applying transformations..."),
                        (75, "✅ Running data quality checks..."),
                        (90, "📤 Loading to destination..."),
                        (100, "🎉 Pipeline completed successfully!"),
                    ]
                    
                    for pct, msg in steps:
                        time.sleep(0.4)
                        progress.progress(pct)
                        status_text.markdown(f"<span style='color:#00d4ff;'>{msg}</span>", unsafe_allow_html=True)
                    
                    st.success("✅ **Ingestion Complete!** 1,247,832 records loaded in 3.2 seconds")
                    
                    col_r1, col_r2, col_r3 = st.columns(3)
                    col_r1.metric("Records Loaded", "1,247,832", "+100%")
                    col_r2.metric("Data Quality", "98.7%", "+0.3%")
                    col_r3.metric("Duration", "3.2s", "-45%")
        
        with col2:
            st.markdown('<div class="section-header">🔧 AI-Powered Transformation</div>', unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background:#1a1a3e; border:1px solid #334466; border-radius:12px; padding:16px; margin-bottom:16px;'>
                <div style='color:#00d4ff; font-weight:700; margin-bottom:10px;'>🤖 AI Schema Mapping</div>
                <div style='font-size:0.85rem; color:#8899bb;'>AI automatically detects and maps source schema to target schema</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Sample schema mapping
            mapping_data = {
                'Source Column': ['cust_id', 'cust_nm', 'sale_amt', 'txn_dt', 'prod_cd'],
                'Target Column': ['customer_id', 'customer_name', 'sale_amount', 'transaction_date', 'product_code'],
                'Data Type': ['INTEGER', 'VARCHAR(100)', 'DECIMAL(10,2)', 'DATE', 'VARCHAR(20)'],
                'AI Confidence': ['99%', '97%', '100%', '98%', '95%'],
                'Transform': ['Direct', 'UPPER()', 'ROUND(2)', 'TO_DATE()', 'Direct'],
            }
            
            df_map = pd.DataFrame(mapping_data)
            st.dataframe(df_map, use_container_width=True, hide_index=True)
            
            st.markdown('<div class="section-header">📊 Data Quality Rules</div>', unsafe_allow_html=True)
            
            rules = [
                ("✅", "Null Check", "customer_id NOT NULL", "Active"),
                ("✅", "Range Validation", "sale_amount BETWEEN 0 AND 1000000", "Active"),
                ("✅", "Format Check", "transaction_date IS VALID DATE", "Active"),
                ("⚠️", "Duplicate Check", "customer_id UNIQUE", "Warning"),
                ("✅", "Referential Integrity", "product_code IN products table", "Active"),
            ]
            
            for icon, rule, condition, status in rules:
                color = "#00ff88" if status == "Active" else "#ffaa00"
                st.markdown(f"""
                <div style='background:#1a1a3e; border:1px solid #334466; border-radius:8px; padding:10px; margin:6px 0; display:flex; justify-content:space-between;'>
                    <span style='color:#aabbcc;'>{icon} <strong style='color:#00d4ff;'>{rule}</strong>: <span style='font-size:0.8rem;'>{condition}</span></span>
                    <span style='color:{color}; font-size:0.8rem;'>{status}</span>
                </div>
                """, unsafe_allow_html=True)

    # ─── TAB 2: Connectors ────────────────────────────────────────────────────
    with tabs[1]:
        st.markdown('<div class="section-header">🔌 Available Data Connectors</div>', unsafe_allow_html=True)
        
        connector_categories = {
            "🗄️ Databases": [
                ("PostgreSQL", "✅ Connected", "#00ff88"),
                ("MySQL", "✅ Connected", "#00ff88"),
                ("SQL Server", "✅ Connected", "#00ff88"),
                ("Oracle DB", "⚙️ Configuring", "#ffaa00"),
                ("MongoDB", "✅ Connected", "#00ff88"),
                ("Snowflake", "✅ Connected", "#00ff88"),
            ],
            "☁️ Cloud Storage": [
                ("AWS S3", "✅ Connected", "#00ff88"),
                ("Azure ADLS", "✅ Connected", "#00ff88"),
                ("Google Cloud Storage", "✅ Connected", "#00ff88"),
                ("Azure Blob", "✅ Connected", "#00ff88"),
            ],
            "📡 Streaming": [
                ("Apache Kafka", "✅ Connected", "#00ff88"),
                ("AWS Kinesis", "✅ Connected", "#00ff88"),
                ("Azure Event Hub", "⚙️ Configuring", "#ffaa00"),
                ("Apache Pulsar", "❌ Not Connected", "#ff4444"),
            ],
            "🏢 Enterprise Apps": [
                ("Salesforce", "✅ Connected", "#00ff88"),
                ("SAP ERP", "✅ Connected", "#00ff88"),
                ("ServiceNow", "⚙️ Configuring", "#ffaa00"),
                ("Workday HR", "✅ Connected", "#00ff88"),
                ("Google Analytics", "✅ Connected", "#00ff88"),
            ],
        }
        
        for category, connectors in connector_categories.items():
            st.markdown(f"**{category}**")
            cols = st.columns(4)
            for i, (name, status, color) in enumerate(connectors):
                with cols[i % 4]:
                    st.markdown(f"""
                    <div style='background:#1a1a3e; border:1px solid #334466; border-radius:10px; padding:14px; text-align:center; margin-bottom:10px;'>
                        <div style='color:#aabbcc; font-weight:600; font-size:0.9rem;'>{name}</div>
                        <div style='color:{color}; font-size:0.75rem; margin-top:6px;'>{status}</div>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown("")

    # ─── TAB 3: Pipeline Monitor ──────────────────────────────────────────────
    with tabs[2]:
        st.markdown('<div class="section-header">📊 Active Pipeline Monitor</div>', unsafe_allow_html=True)
        
        pipeline_data = {
            'Pipeline': ['Sales → Snowflake', 'Finance → Redshift', 'HR → Data Lake', 'CRM → Analytics DB', 'IoT → Kafka → Lake'],
            'Status': ['🟢 Running', '🟢 Running', '🟡 Warning', '🟢 Running', '🟢 Running'],
            'Records/sec': [12450, 8320, 2100, 5670, 45000],
            'Latency (ms)': [45, 78, 234, 56, 12],
            'Success Rate': ['99.8%', '99.5%', '97.2%', '99.9%', '99.7%'],
            'Last Run': ['2 min ago', '5 min ago', '1 hr ago', '3 min ago', 'Live'],
        }
        
        df_pipe = pd.DataFrame(pipeline_data)
        st.dataframe(df_pipe, use_container_width=True, hide_index=True)
        
        # Throughput chart
        st.markdown('<div class="section-header">⚡ Real-time Throughput</div>', unsafe_allow_html=True)
        
        times = list(range(60))
        throughput = [random.randint(60000, 100000) for _ in times]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=times, y=throughput,
            fill='tozeroy',
            fillcolor='rgba(0, 212, 255, 0.1)',
            line=dict(color='#00d4ff', width=2),
            name='Records/sec'
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#aabbcc'),
            xaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Time (seconds ago)'),
            yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Records/sec'),
            margin=dict(l=0, r=0, t=10, b=0),
            height=250,
        )
        st.plotly_chart(fig, use_container_width=True)

    # ─── TAB 4: Data Catalog ──────────────────────────────────────────────────
    with tabs[3]:
        st.markdown('<div class="section-header">📋 AI-Powered Data Catalog</div>', unsafe_allow_html=True)
        
        search_term = st.text_input("🔍 Search datasets, tables, columns...", placeholder="e.g., customer, sales, revenue")
        
        catalog_data = {
            'Dataset': ['sales_transactions', 'customer_master', 'product_catalog', 'hr_employees', 'finance_gl', 'marketing_campaigns'],
            'Domain': ['Sales', 'CRM', 'Operations', 'HR', 'Finance', 'Marketing'],
            'Records': ['12.4M', '2.1M', '450K', '85K', '8.7M', '320K'],
            'Last Updated': ['2 min ago', '1 hr ago', 'Daily', 'Weekly', '5 min ago', 'Daily'],
            'Quality Score': ['98.7%', '99.1%', '97.5%', '99.8%', '98.2%', '96.4%'],
            'Owner': ['Sales Analytics', 'CRM Team', 'Ops Team', 'HR Analytics', 'Finance BI', 'Mktg Analytics'],
        }
        
        df_cat = pd.DataFrame(catalog_data)
        
        if search_term:
            mask = df_cat.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
            df_cat = df_cat[mask]
        
        st.dataframe(df_cat, use_container_width=True, hide_index=True)
