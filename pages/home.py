import streamlit as st

def show():
    # Hero Banner
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🧠 SmartData Hub</div>
        <div class="hero-subtitle">AI-Powered Modern Data Platform | Cloud-Native | Scalable | Intelligent</div>
        <div style='margin-top:16px;'>
            <span class="badge-green">✅ Cloud Connected</span>&nbsp;&nbsp;
            <span class="badge-blue">🤖 AI Enabled</span>&nbsp;&nbsp;
            <span class="badge-orange">⚡ Real-time</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # KPI Row
    st.markdown('<div class="section-header">📈 Platform Overview</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    kpis = [
        ("2.4 TB", "Data Processed Today", "↑ 18%"),
        ("47", "Active Data Pipelines", "↑ 5 new"),
        ("98.7%", "Platform Uptime", "↑ 0.2%"),
        ("63%", "Cost Reduction", "↓ vs Legacy"),
        ("12", "AI Models Deployed", "↑ 3 this week"),
    ]
    
    for col, (val, label, delta) in zip([col1, col2, col3, col4, col5], kpis):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{val}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-delta">{delta}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature Cards
    st.markdown('<div class="section-header">🚀 Platform Capabilities</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    features = [
        ("📊", "BI & Analytics", "Real-time dashboards, KPI tracking, operational & strategic reporting across all business units."),
        ("🔄", "Data Ingestion", "Ingest from 20+ sources: CSV, APIs, databases, streaming, IoT, cloud storage — all unified."),
        ("🤖", "AI Chatbot", "Ask questions in plain English. Get instant SQL queries, charts, and AI-powered insights."),
        ("🔬", "Data Science", "AutoML pipeline builder, model training, evaluation, and deployment for all Lines of Business."),
        ("💰", "Cost Optimizer", "Track ETL costs, identify bottlenecks, and get AI recommendations to reduce infrastructure spend."),
        ("🏗️", "Architecture", "Cloud-native, scalable architecture with data lake, warehouse, and lakehouse patterns."),
        ("🔐", "Data Governance", "Role-based access, data lineage tracking, quality scoring, and compliance monitoring."),
        ("⚡", "Real-time Processing", "Stream processing with sub-second latency for operational analytics and alerting."),
    ]
    
    cols = st.columns(4)
    for i, (icon, title, desc) in enumerate(features):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="feature-card" style="margin-bottom:16px;">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How AI Helps Section
    st.markdown('<div class="section-header">🤖 How AI Solves Your Problems</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #1a1a3e, #0d1b2a); border: 1px solid #334466; border-radius:16px; padding:24px;'>
            <div style='font-size:1.1rem; font-weight:700; color:#00d4ff; margin-bottom:16px;'>❌ Problems You Face</div>
            <div style='color:#cc8888; margin:10px 0;'>🔴 Data silos across departments</div>
            <div style='color:#cc8888; margin:10px 0;'>🔴 Slow ETL pipelines (days to build)</div>
            <div style='color:#cc8888; margin:10px 0;'>🔴 High infrastructure costs</div>
            <div style='color:#cc8888; margin:10px 0;'>🔴 Manual, error-prone reporting</div>
            <div style='color:#cc8888; margin:10px 0;'>🔴 No self-service analytics</div>
            <div style='color:#cc8888; margin:10px 0;'>🔴 Delayed business insights</div>
            <div style='color:#cc8888; margin:10px 0;'>🔴 Complex ML model deployment</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #0d2a1a, #0d1b2a); border: 1px solid #00ff8833; border-radius:16px; padding:24px;'>
            <div style='font-size:1.1rem; font-weight:700; color:#00ff88; margin-bottom:16px;'>✅ AI-Powered Solutions</div>
            <div style='color:#88cc88; margin:10px 0;'>🟢 Unified data lake with AI cataloging</div>
            <div style='color:#88cc88; margin:10px 0;'>🟢 Auto-generated ETL pipelines (minutes)</div>
            <div style='color:#88cc88; margin:10px 0;'>🟢 63% cost reduction via smart optimization</div>
            <div style='color:#88cc88; margin:10px 0;'>🟢 AI-automated report generation</div>
            <div style='color:#88cc88; margin:10px 0;'>🟢 NL2SQL chatbot for everyone</div>
            <div style='color:#88cc88; margin:10px 0;'>🟢 Real-time AI insights & alerts</div>
            <div style='color:#88cc88; margin:10px 0;'>🟢 One-click AutoML deployment</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Data Flow
    st.markdown('<div class="section-header">🔄 Data Flow Architecture</div>', unsafe_allow_html=True)
    
    cols = st.columns(7)
    steps = [
        ("📥", "Ingest", "20+ Sources"),
        ("➡️", "", ""),
        ("🔧", "Transform", "AI-ETL"),
        ("➡️", "", ""),
        ("🏪", "Store", "Data Lake"),
        ("➡️", "", ""),
        ("📊", "Analyze", "BI + AI"),
    ]
    
    for col, (icon, title, sub) in zip(cols, steps):
        with col:
            if title:
                st.markdown(f"""
                <div class="pipeline-step pipeline-step-active" style="margin:4px;">
                    <div style='font-size:1.8rem;'>{icon}</div>
                    <div style='color:#00d4ff; font-weight:700; font-size:0.85rem;'>{title}</div>
                    <div style='color:#8899bb; font-size:0.7rem;'>{sub}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='text-align:center; padding:20px 0; font-size:1.5rem; color:#334466;'>{icon}</div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # LOB Coverage
    st.markdown('<div class="section-header">🏢 Lines of Business Coverage</div>', unsafe_allow_html=True)
    
    lobs = ["Finance & Risk", "Sales & CRM", "HR & Workforce", "Operations", "Marketing", "Supply Chain", "Customer Service", "IT & Security"]
    cols = st.columns(4)
    for i, lob in enumerate(lobs):
        with cols[i % 4]:
            st.markdown(f"""
            <div style='background:#1a1a3e; border:1px solid #334466; border-radius:10px; padding:12px; text-align:center; margin-bottom:10px;'>
                <span style='color:#00d4ff; font-size:0.85rem; font-weight:600;'>✅ {lob}</span>
            </div>
            """, unsafe_allow_html=True)
