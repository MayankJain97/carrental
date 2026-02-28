import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

def show():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1a2a0a, #0f3460); border-radius:16px; padding:24px; margin-bottom:24px;'>
        <div style='font-size:1.8rem; font-weight:800; color:white;'>💰 Cost Optimizer</div>
        <div style='color:#ccddff; margin-top:6px;'>Reduce Infrastructure Costs | Eliminate Bottlenecks | Maximize ROI</div>
    </div>
    """, unsafe_allow_html=True)

    # Top savings metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">$2.4M</div>
            <div class="metric-label">Annual Savings</div>
            <div class="metric-delta">↑ 63% vs Legacy</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">78%</div>
            <div class="metric-label">ETL Dev Time Saved</div>
            <div class="metric-delta">↓ 3 days → 4 hours</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">45%</div>
            <div class="metric-label">Query Cost Reduction</div>
            <div class="metric-delta">↓ $0.08 → $0.044/query</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">3.2x</div>
            <div class="metric-label">ROI on Platform</div>
            <div class="metric-delta">↑ Payback in 8 months</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tabs = st.tabs(["💸 Cost Breakdown", "⚡ Bottleneck Analyzer", "🤖 AI Recommendations", "📊 ROI Calculator"])

    # ─── TAB 1: Cost Breakdown ────────────────────────────────────────────────
    with tabs[0]:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="section-header">📊 Monthly Cost by Category</div>', unsafe_allow_html=True)
            
            categories = ['Compute', 'Storage', 'Data Transfer', 'ETL Jobs', 'BI Tools', 'ML Training']
            current_costs = [45000, 18000, 12000, 28000, 15000, 22000]
            optimized_costs = [28000, 12000, 8000, 8000, 9000, 14000]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Current Cost', x=categories, y=current_costs,
                               marker_color='#ff6b6b', opacity=0.8))
            fig.add_trace(go.Bar(name='Optimized Cost', x=categories, y=optimized_costs,
                               marker_color='#00ff88', opacity=0.8))
            
            fig.update_layout(
                barmode='group',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#aabbcc'),
                legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#aabbcc')),
                xaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
                yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Monthly Cost ($)'),
                margin=dict(l=0, r=0, t=10, b=0),
                height=300,
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown('<div class="section-header">📈 Cost Trend (12 Months)</div>', unsafe_allow_html=True)
            
            months = pd.date_range(end=datetime.now(), periods=12, freq='MS').strftime('%b %Y')
            legacy_cost = [180000, 185000, 188000, 192000, 195000, 198000, 200000, 202000, 205000, 208000, 210000, 212000]
            new_platform = [None, None, None, None, 195000, 175000, 155000, 140000, 128000, 118000, 110000, 105000]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(months), y=legacy_cost, name='Legacy Platform',
                                    line=dict(color='#ff6b6b', width=2, dash='dash')))
            fig.add_trace(go.Scatter(x=list(months), y=new_platform, name='SmartData Hub',
                                    line=dict(color='#00d4ff', width=3),
                                    connectgaps=False))
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#aabbcc'),
                legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#aabbcc')),
                xaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
                yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Monthly Cost ($)'),
                margin=dict(l=0, r=0, t=10, b=0),
                height=300,
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Cost table
        st.markdown('<div class="section-header">📋 Detailed Cost Analysis</div>', unsafe_allow_html=True)
        
        cost_data = {
            'Category': ['Compute (Cloud VMs)', 'Data Storage', 'Data Transfer', 'ETL Development', 'BI Licensing', 'ML Infrastructure', 'Support & Ops'],
            'Legacy Monthly': ['$45,000', '$18,000', '$12,000', '$28,000', '$15,000', '$22,000', '$8,000'],
            'New Platform': ['$28,000', '$12,000', '$8,000', '$8,000', '$9,000', '$14,000', '$4,000'],
            'Savings': ['$17,000', '$6,000', '$4,000', '$20,000', '$6,000', '$8,000', '$4,000'],
            'Savings %': ['38%', '33%', '33%', '71%', '40%', '36%', '50%'],
            'How': ['Auto-scaling', 'Compression + tiering', 'CDN optimization', 'AI-generated ETL', 'Consolidated platform', 'Spot instances', 'Automation'],
        }
        
        df_cost = pd.DataFrame(cost_data)
        st.dataframe(df_cost, use_container_width=True, hide_index=True)

    # ─── TAB 2: Bottleneck Analyzer ───────────────────────────────────────────
    with tabs[1]:
        st.markdown('<div class="section-header">⚡ Performance Bottleneck Analysis</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            bottlenecks = [
                ("🔴 Critical", "Finance ETL Pipeline", "Query scan 2.4TB full table — missing partition", "Add date partition filter → 95% cost reduction"),
                ("🟡 Warning", "Sales Dashboard", "N+1 query problem — 847 separate DB calls", "Implement query batching → 40x faster"),
                ("🟡 Warning", "HR Report", "No index on employee_id join column", "Add composite index → 8x faster"),
                ("🟢 Info", "Marketing ETL", "Uncompressed Parquet files in S3", "Enable Snappy compression → 60% storage savings"),
                ("🟢 Info", "CRM Sync", "Scheduled every 5 min but data changes hourly", "Change to hourly → 12x fewer compute cycles"),
            ]
            
            for severity, name, issue, fix in bottlenecks:
                color = "#ff4444" if "Critical" in severity else "#ffaa00" if "Warning" in severity else "#00d4ff"
                st.markdown(f"""
                <div style='background:#1a1a3e; border-left:4px solid {color}; border-radius:0 12px 12px 0; padding:14px; margin-bottom:10px;'>
                    <div style='display:flex; justify-content:space-between; margin-bottom:6px;'>
                        <strong style='color:{color};'>{severity}</strong>
                        <span style='color:#aabbcc; font-weight:600;'>{name}</span>
                    </div>
                    <div style='font-size:0.82rem; color:#cc8888; margin-bottom:4px;'>⚠️ Issue: {issue}</div>
                    <div style='font-size:0.82rem; color:#88cc88;'>✅ Fix: {fix}</div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="section-header">📊 Query Performance Distribution</div>', unsafe_allow_html=True)
            
            query_times = np.random.exponential(2, 1000)
            query_times = np.clip(query_times, 0.01, 30)
            
            fig = go.Figure(go.Histogram(
                x=query_times,
                nbinsx=50,
                marker=dict(color='#00d4ff', opacity=0.7, line=dict(color='#0f3460', width=0.5)),
            ))
            fig.add_vline(x=np.percentile(query_times, 95), line_color='#ff4444', line_dash='dash',
                         annotation_text='P95', annotation_font_color='#ff4444')
            fig.add_vline(x=np.median(query_times), line_color='#00ff88', line_dash='dash',
                         annotation_text='Median', annotation_font_color='#00ff88')
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#aabbcc'),
                xaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Query Time (seconds)'),
                yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Count'),
                margin=dict(l=0, r=0, t=10, b=0),
                height=280,
            )
            st.plotly_chart(fig, use_container_width=True)
            
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Median Query", f"{np.median(query_times):.2f}s")
            col_b.metric("P95 Query", f"{np.percentile(query_times, 95):.2f}s")
            col_c.metric("Slow Queries", f"{(query_times > 10).sum()}", "need fixing")

    # ─── TAB 3: AI Recommendations ────────────────────────────────────────────
    with tabs[2]:
        st.markdown('<div class="section-header">🤖 AI Cost Optimization Recommendations</div>', unsafe_allow_html=True)
        
        recommendations = [
            {
                "priority": "🔴 HIGH",
                "title": "Partition Finance ETL Tables",
                "impact": "$17,000/month savings",
                "effort": "Low (2 hours)",
                "description": "AI detected full table scans on finance_transactions (2.4TB). Adding date partitioning will reduce scan to ~50GB per query.",
                "steps": ["ALTER TABLE finance_transactions ADD PARTITION BY date", "Rebuild existing data with partitions", "Update ETL queries to include date filter"],
                "color": "#ff4444"
            },
            {
                "priority": "🔴 HIGH",
                "title": "Enable Auto-Scaling on Compute Cluster",
                "impact": "$12,000/month savings",
                "effort": "Low (1 hour)",
                "description": "Cluster runs at 100% capacity 24/7 but actual usage is only 40% during off-peak hours (10pm-6am).",
                "steps": ["Configure min/max node counts", "Set scale-down threshold to 30% CPU", "Enable spot instances for batch jobs"],
                "color": "#ff4444"
            },
            {
                "priority": "🟡 MEDIUM",
                "title": "Consolidate Redundant ETL Pipelines",
                "impact": "$8,000/month savings",
                "effort": "Medium (1 week)",
                "description": "AI found 12 ETL pipelines reading the same source tables independently. Consolidating to shared staging layer eliminates redundancy.",
                "steps": ["Create shared staging tables", "Refactor 12 pipelines to use staging", "Decommission redundant source connections"],
                "color": "#ffaa00"
            },
            {
                "priority": "🟡 MEDIUM",
                "title": "Implement Data Tiering Strategy",
                "impact": "$6,000/month savings",
                "effort": "Medium (3 days)",
                "description": "78% of stored data is older than 90 days and rarely accessed. Moving to cold storage tier reduces costs by 80%.",
                "steps": ["Classify data by access frequency", "Move data >90 days to cold tier", "Set up lifecycle policies"],
                "color": "#ffaa00"
            },
        ]
        
        for rec in recommendations:
            with st.expander(f"{rec['priority']} | {rec['title']} — {rec['impact']}", expanded=True):
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"<div style='color:#aabbcc; font-size:0.9rem;'>{rec['description']}</div>", unsafe_allow_html=True)
                    st.markdown("**Implementation Steps:**")
                    for i, step in enumerate(rec['steps'], 1):
                        st.markdown(f"{i}. {step}")
                with col2:
                    st.markdown(f"""
                    <div style='background:#1a1a3e; border:1px solid {rec['color']}44; border-radius:10px; padding:14px; text-align:center;'>
                        <div style='color:{rec['color']}; font-size:1.3rem; font-weight:800;'>{rec['impact']}</div>
                        <div style='color:#8899bb; font-size:0.8rem; margin-top:6px;'>Effort: {rec['effort']}</div>
                    </div>
                    """, unsafe_allow_html=True)

    # ─── TAB 4: ROI Calculator ────────────────────────────────────────────────
    with tabs[3]:
        st.markdown('<div class="section-header">📊 ROI Calculator</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**💰 Current State (Legacy)**")
            legacy_infra = st.number_input("Monthly Infrastructure Cost ($)", value=150000, step=5000)
            legacy_etl_devs = st.number_input("ETL Developers (FTEs)", value=8, step=1)
            legacy_bi_devs = st.number_input("BI Developers (FTEs)", value=5, step=1)
            avg_salary = st.number_input("Avg Developer Salary ($/year)", value=120000, step=5000)
            legacy_downtime = st.number_input("Monthly Downtime Hours", value=12, step=1)
            downtime_cost = st.number_input("Cost per Downtime Hour ($)", value=5000, step=500)
            
            st.markdown("**🚀 SmartData Hub Investment**")
            platform_cost = st.number_input("Platform Monthly Cost ($)", value=45000, step=1000)
            implementation_cost = st.number_input("One-time Implementation ($)", value=200000, step=10000)
        
        with col2:
            # Calculate ROI
            legacy_monthly = legacy_infra + (legacy_etl_devs + legacy_bi_devs) * avg_salary / 12 + legacy_downtime * downtime_cost
            new_monthly = platform_cost + (legacy_etl_devs * 0.3 + legacy_bi_devs * 0.4) * avg_salary / 12 + legacy_downtime * 0.1 * downtime_cost
            monthly_savings = legacy_monthly - new_monthly
            annual_savings = monthly_savings * 12
            payback_months = implementation_cost / monthly_savings if monthly_savings > 0 else 999
            roi_3yr = ((annual_savings * 3 - implementation_cost) / implementation_cost * 100)
            
            st.markdown(f"""
            <div style='background:linear-gradient(135deg, #0d2a1a, #0f3460); border:2px solid #00ff88; border-radius:16px; padding:24px;'>
                <div style='font-size:1.2rem; font-weight:700; color:#00ff88; margin-bottom:16px;'>📊 ROI Analysis Results</div>
                
                <div style='display:flex; justify-content:space-between; margin:10px 0; padding:8px; background:#1a1a3e; border-radius:8px;'>
                    <span style='color:#8899bb;'>Legacy Monthly Cost</span>
                    <span style='color:#ff6b6b; font-weight:700;'>${legacy_monthly:,.0f}</span>
                </div>
                <div style='display:flex; justify-content:space-between; margin:10px 0; padding:8px; background:#1a1a3e; border-radius:8px;'>
                    <span style='color:#8899bb;'>New Platform Monthly Cost</span>
                    <span style='color:#00d4ff; font-weight:700;'>${new_monthly:,.0f}</span>
                </div>
                <div style='display:flex; justify-content:space-between; margin:10px 0; padding:8px; background:#1a1a3e; border-radius:8px;'>
                    <span style='color:#8899bb;'>Monthly Savings</span>
                    <span style='color:#00ff88; font-weight:700;'>${monthly_savings:,.0f}</span>
                </div>
                <div style='display:flex; justify-content:space-between; margin:10px 0; padding:8px; background:#1a1a3e; border-radius:8px;'>
                    <span style='color:#8899bb;'>Annual Savings</span>
                    <span style='color:#00ff88; font-weight:800; font-size:1.2rem;'>${annual_savings:,.0f}</span>
                </div>
                <div style='display:flex; justify-content:space-between; margin:10px 0; padding:8px; background:#1a1a3e; border-radius:8px;'>
                    <span style='color:#8899bb;'>Payback Period</span>
                    <span style='color:#ffd700; font-weight:700;'>{payback_months:.1f} months</span>
                </div>
                <div style='display:flex; justify-content:space-between; margin:10px 0; padding:8px; background:#1a1a3e; border-radius:8px;'>
                    <span style='color:#8899bb;'>3-Year ROI</span>
                    <span style='color:#00ff88; font-weight:800; font-size:1.3rem;'>{roi_3yr:.0f}%</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Cumulative savings chart
            months_range = list(range(1, 37))
            cumulative_savings = [monthly_savings * m - implementation_cost for m in months_range]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=months_range, y=cumulative_savings,
                fill='tozeroy',
                fillcolor='rgba(0, 255, 136, 0.1)',
                line=dict(color='#00ff88', width=2),
                name='Cumulative Savings',
            ))
            fig.add_hline(y=0, line_color='#ff4444', line_dash='dash', annotation_text='Break-even', annotation_font_color='#ff4444')
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#aabbcc'),
                xaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Month'),
                yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Cumulative Savings ($)'),
                margin=dict(l=0, r=0, t=10, b=0),
                height=250,
                title=dict(text='Cumulative ROI Over 3 Years', font=dict(color='#00d4ff', size=13)),
            )
            st.plotly_chart(fig, use_container_width=True)
