import streamlit as st

def show():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0f3460, #533483, #e94560); border-radius:16px; padding:24px; margin-bottom:24px;'>
        <div style='font-size:1.8rem; font-weight:800; color:white;'>🏗️ Platform Architecture</div>
        <div style='color:#ccddff; margin-top:6px;'>Cloud-Native | Scalable | Modern Data Lakehouse Architecture</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["🏛️ Architecture Overview", "☁️ Cloud Components", "🔐 Governance & Security", "🗺️ Roadmap"])

    with tabs[0]:
        st.markdown('<div class="section-header">🏛️ Modern Data Lakehouse Architecture</div>', unsafe_allow_html=True)
        
        # Architecture layers
        layers = [
            {
                "name": "📥 INGESTION LAYER",
                "color": "#0f3460",
                "border": "#00d4ff",
                "components": ["Batch ETL (ADF/Glue)", "Stream Processing (Kafka/Kinesis)", "API Connectors (20+)", "File Ingestion (CSV/JSON/XML)", "CDC (Debezium)"]
            },
            {
                "name": "🏪 STORAGE LAYER",
                "color": "#1a1a3e",
                "border": "#00ff88",
                "components": ["Raw Zone (Data Lake)", "Curated Zone (Delta Lake)", "Serving Zone (Data Warehouse)", "Archive Zone (Cold Storage)", "Feature Store (ML)"]
            },
            {
                "name": "🔧 PROCESSING LAYER",
                "color": "#0d2a1a",
                "border": "#ffd700",
                "components": ["Apache Spark (Batch)", "Apache Flink (Streaming)", "dbt (Transformations)", "AI-ETL Generator", "Data Quality Engine"]
            },
            {
                "name": "📊 CONSUMPTION LAYER",
                "color": "#2a1a0d",
                "border": "#ff8800",
                "components": ["Power BI / Tableau", "Self-Service Analytics", "AI Chatbot (NL2SQL)", "REST APIs", "ML Model Serving"]
            },
        ]
        
        for layer in layers:
            st.markdown(f"""
            <div style='background:{layer["color"]}; border:2px solid {layer["border"]}44; border-radius:12px; padding:16px; margin-bottom:12px;'>
                <div style='font-weight:800; color:{layer["border"]}; font-size:1rem; margin-bottom:10px;'>{layer["name"]}</div>
                <div style='display:flex; flex-wrap:wrap; gap:8px;'>
                    {"".join([f'<span style="background:{layer["border"]}22; border:1px solid {layer["border"]}44; border-radius:20px; padding:4px 12px; font-size:0.8rem; color:#ccddff;">{c}</span>' for c in layer["components"]])}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Cross-cutting concerns
        st.markdown("""
        <div style='background:linear-gradient(135deg, #1a0a2a, #0a1a2a); border:2px solid #ff88ff44; border-radius:12px; padding:16px; margin-top:8px;'>
            <div style='font-weight:800; color:#ff88ff; font-size:1rem; margin-bottom:10px;'>🔐 CROSS-CUTTING: Governance | Security | Monitoring | Lineage</div>
            <div style='display:flex; flex-wrap:wrap; gap:8px;'>
                <span style='background:#ff88ff22; border:1px solid #ff88ff44; border-radius:20px; padding:4px 12px; font-size:0.8rem; color:#ccddff;'>Data Catalog (Purview/Glue)</span>
                <span style='background:#ff88ff22; border:1px solid #ff88ff44; border-radius:20px; padding:4px 12px; font-size:0.8rem; color:#ccddff;'>RBAC & IAM</span>
                <span style='background:#ff88ff22; border:1px solid #ff88ff44; border-radius:20px; padding:4px 12px; font-size:0.8rem; color:#ccddff;'>Data Lineage (OpenLineage)</span>
                <span style='background:#ff88ff22; border:1px solid #ff88ff44; border-radius:20px; padding:4px 12px; font-size:0.8rem; color:#ccddff;'>Observability (Datadog)</span>
                <span style='background:#ff88ff22; border:1px solid #ff88ff44; border-radius:20px; padding:4px 12px; font-size:0.8rem; color:#ccddff;'>Encryption (AES-256)</span>
                <span style='background:#ff88ff22; border:1px solid #ff88ff44; border-radius:20px; padding:4px 12px; font-size:0.8rem; color:#ccddff;'>Compliance (GDPR/SOC2)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">☁️ Cloud Technology Stack</div>', unsafe_allow_html=True)
        
        tech_stack = {
            "Cloud Platform": [("Azure", "Primary Cloud"), ("AWS", "Secondary/DR"), ("GCP", "ML Workloads")],
            "Data Storage": [("Azure ADLS Gen2", "Data Lake"), ("Snowflake", "Data Warehouse"), ("Delta Lake", "Lakehouse Format")],
            "Processing": [("Apache Spark", "Batch Processing"), ("Apache Kafka", "Streaming"), ("dbt", "Transformations")],
            "Orchestration": [("Apache Airflow", "Pipeline Orchestration"), ("Azure Data Factory", "ETL/ELT"), ("Prefect", "Workflow Mgmt")],
            "BI & Reporting": [("Power BI", "Enterprise BI"), ("Tableau", "Self-Service"), ("Streamlit", "Custom Apps")],
            "AI & ML": [("Azure ML", "Model Training"), ("MLflow", "Model Registry"), ("OpenAI GPT", "NL2SQL/Insights")],
            "Monitoring": [("Datadog", "Infrastructure"), ("Great Expectations", "Data Quality"), ("Monte Carlo", "Data Observability")],
        }
        
        for category, tools in tech_stack.items():
            st.markdown(f"**{category}**")
            cols = st.columns(3)
            for i, (tool, purpose) in enumerate(tools):
                with cols[i % 3]:
                    st.markdown(f"""
                    <div style='background:#1a1a3e; border:1px solid #334466; border-radius:10px; padding:12px; text-align:center; margin-bottom:10px;'>
                        <div style='color:#00d4ff; font-weight:700;'>{tool}</div>
                        <div style='color:#8899bb; font-size:0.75rem; margin-top:4px;'>{purpose}</div>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown("")

    with tabs[2]:
        st.markdown('<div class="section-header">🔐 Data Governance & Security</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            governance_items = [
                ("🏷️", "Data Catalog", "Automated metadata discovery and tagging for all datasets"),
                ("🔍", "Data Lineage", "End-to-end tracking from source to consumption"),
                ("✅", "Data Quality", "Automated quality checks with 50+ built-in rules"),
                ("👥", "Access Control", "Role-based access with column/row-level security"),
                ("📋", "Data Contracts", "Schema enforcement between producers and consumers"),
                ("🔒", "Encryption", "AES-256 at rest, TLS 1.3 in transit"),
            ]
            
            for icon, title, desc in governance_items:
                st.markdown(f"""
                <div style='background:#1a1a3e; border:1px solid #334466; border-radius:10px; padding:14px; margin-bottom:8px;'>
                    <div style='font-size:1.1rem;'>{icon} <strong style='color:#00d4ff;'>{title}</strong></div>
                    <div style='font-size:0.82rem; color:#8899bb; margin-top:4px;'>{desc}</div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            compliance_items = [
                ("✅", "GDPR Compliant", "Data residency, right to erasure, consent management"),
                ("✅", "SOC 2 Type II", "Security, availability, confidentiality controls"),
                ("✅", "ISO 27001", "Information security management"),
                ("✅", "HIPAA Ready", "Healthcare data protection (if applicable)"),
                ("✅", "PCI DSS", "Payment card data security"),
                ("🔄", "CCPA", "California Consumer Privacy Act compliance"),
            ]
            
            for icon, title, desc in compliance_items:
                color = "#00ff88" if icon == "✅" else "#ffaa00"
                st.markdown(f"""
                <div style='background:#1a1a3e; border:1px solid {color}33; border-radius:10px; padding:14px; margin-bottom:8px;'>
                    <div style='font-size:1.1rem;'>{icon} <strong style='color:{color};'>{title}</strong></div>
                    <div style='font-size:0.82rem; color:#8899bb; margin-top:4px;'>{desc}</div>
                </div>
                """, unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<div class="section-header">🗺️ Implementation Roadmap</div>', unsafe_allow_html=True)
        
        phases = [
            {
                "phase": "Phase 1 — Foundation",
                "duration": "Months 1-3",
                "status": "✅ Complete",
                "color": "#00ff88",
                "items": ["Cloud infrastructure setup", "Core data lake deployment", "Basic ETL pipelines (top 5 sources)", "Initial BI dashboards", "Data governance framework"]
            },
            {
                "phase": "Phase 2 — Scale",
                "duration": "Months 4-6",
                "status": "🔄 In Progress",
                "color": "#00d4ff",
                "items": ["All 20+ data source connectors", "Self-service analytics portal", "AI Chatbot (NL2SQL)", "Advanced BI dashboards", "Data quality automation"]
            },
            {
                "phase": "Phase 3 — Intelligence",
                "duration": "Months 7-9",
                "status": "📅 Planned",
                "color": "#ffd700",
                "items": ["AutoML platform launch", "First 3 ML models in production", "Real-time streaming analytics", "Predictive dashboards", "Cost optimization engine"]
            },
            {
                "phase": "Phase 4 — Optimization",
                "duration": "Months 10-12",
                "status": "📅 Planned",
                "color": "#ff8800",
                "items": ["12 ML models across all LOBs", "Advanced anomaly detection", "Automated insight generation", "Full data mesh architecture", "Center of Excellence launch"]
            },
        ]
        
        for phase_info in phases:
            st.markdown(f"""
            <div style='background:#1a1a3e; border-left:4px solid {phase_info["color"]}; border-radius:0 12px 12px 0; padding:16px; margin-bottom:12px;'>
                <div style='display:flex; justify-content:space-between; margin-bottom:10px;'>
                    <strong style='color:{phase_info["color"]}; font-size:1rem;'>{phase_info["phase"]}</strong>
                    <span style='color:#8899bb; font-size:0.85rem;'>{phase_info["duration"]} | {phase_info["status"]}</span>
                </div>
                <div style='display:flex; flex-wrap:wrap; gap:6px;'>
                    {"".join([f'<span style="background:{phase_info["color"]}22; border:1px solid {phase_info["color"]}44; border-radius:20px; padding:3px 10px; font-size:0.78rem; color:#ccddff;">✓ {item}</span>' for item in phase_info["items"]])}
                </div>
            </div>
            """, unsafe_allow_html=True)
