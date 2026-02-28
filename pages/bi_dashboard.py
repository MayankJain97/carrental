import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def show():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0f3460, #533483); border-radius:16px; padding:24px; margin-bottom:24px;'>
        <div style='font-size:1.8rem; font-weight:800; color:white;'>📊 BI & Analytics Dashboard</div>
        <div style='color:#ccddff; margin-top:6px;'>Real-time Business Intelligence | Operational & Strategic Reporting</div>
    </div>
    """, unsafe_allow_html=True)

    # Filters
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        lob = st.selectbox("Line of Business", ["All LOBs", "Finance", "Sales", "HR", "Operations", "Marketing"])
    with col2:
        period = st.selectbox("Time Period", ["Last 7 Days", "Last 30 Days", "Last Quarter", "YTD", "Last Year"])
    with col3:
        region = st.selectbox("Region", ["Global", "North America", "Europe", "Asia Pacific", "LATAM"])
    with col4:
        refresh = st.button("🔄 Refresh Data", use_container_width=True)

    st.markdown("---")

    # Top KPIs
    st.markdown('<div class="section-header">📈 Key Performance Indicators</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    metrics = [
        ("$48.2M", "Total Revenue", "+12.4%"),
        ("94.3%", "Customer Satisfaction", "+2.1%"),
        ("1.2M", "Active Users", "+8.7%"),
        ("$3.2M", "Cost Savings", "+63%"),
        ("99.1%", "Data Quality Score", "+0.5%"),
        ("47ms", "Avg Query Time", "-38%"),
    ]
    
    for col, (val, label, delta) in zip([col1, col2, col3, col4, col5, col6], metrics):
        with col:
            st.metric(label=label, value=val, delta=delta)

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts Row 1
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="section-header">📉 Revenue Trend by LOB</div>', unsafe_allow_html=True)
        
        dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
        lobs_data = {
            'Finance': np.cumsum(np.random.randn(90) * 50000 + 10000) + 5000000,
            'Sales': np.cumsum(np.random.randn(90) * 40000 + 15000) + 4000000,
            'Operations': np.cumsum(np.random.randn(90) * 30000 + 8000) + 3000000,
            'Marketing': np.cumsum(np.random.randn(90) * 20000 + 5000) + 2000000,
        }
        
        fig = go.Figure()
        colors = ['#00d4ff', '#00ff88', '#ff6b6b', '#ffd700']
        for (lob_name, values), color in zip(lobs_data.items(), colors):
            fig.add_trace(go.Scatter(
                x=dates, y=values, name=lob_name,
                line=dict(color=color, width=2),
                fill='tonexty' if lob_name != 'Finance' else None,
                fillcolor=color.replace(')', ', 0.1)').replace('rgb', 'rgba') if '#' not in color else None,
            ))
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#aabbcc'),
            legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#aabbcc')),
            xaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
            yaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
            margin=dict(l=0, r=0, t=10, b=0),
            height=300,
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="section-header">🥧 Data Source Distribution</div>', unsafe_allow_html=True)
        
        sources = ['Databases', 'APIs', 'Files/CSV', 'Streaming', 'Cloud Storage', 'IoT']
        values = [35, 25, 15, 12, 8, 5]
        colors_pie = ['#00d4ff', '#00ff88', '#ff6b6b', '#ffd700', '#ff88ff', '#88ffff']
        
        fig = go.Figure(data=[go.Pie(
            labels=sources, values=values,
            hole=0.5,
            marker=dict(colors=colors_pie, line=dict(color='#0f0c29', width=2)),
            textfont=dict(color='white', size=11),
        )])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#aabbcc'),
            legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#aabbcc', size=10)),
            margin=dict(l=0, r=0, t=10, b=0),
            height=300,
        )
        st.plotly_chart(fig, use_container_width=True)

    # Charts Row 2
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="section-header">📊 Pipeline Performance</div>', unsafe_allow_html=True)
        
        pipeline_names = ['Sales ETL', 'Finance ETL', 'HR ETL', 'Ops ETL', 'Mktg ETL']
        success_rates = [98.5, 99.1, 97.8, 99.5, 96.2]
        
        fig = go.Figure(go.Bar(
            x=success_rates,
            y=pipeline_names,
            orientation='h',
            marker=dict(
                color=success_rates,
                colorscale=[[0, '#ff4444'], [0.5, '#ffaa00'], [1, '#00ff88']],
                showscale=False,
            ),
            text=[f'{v}%' for v in success_rates],
            textposition='outside',
            textfont=dict(color='#aabbcc'),
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#aabbcc'),
            xaxis=dict(range=[90, 100], gridcolor='#1e3a5f', color='#8899bb'),
            yaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
            margin=dict(l=0, r=40, t=10, b=0),
            height=250,
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="section-header">⚡ Query Volume (24h)</div>', unsafe_allow_html=True)
        
        hours = list(range(24))
        query_vol = [random.randint(200, 2000) for _ in hours]
        
        fig = go.Figure(go.Bar(
            x=hours, y=query_vol,
            marker=dict(
                color=query_vol,
                colorscale=[[0, '#0f3460'], [1, '#00d4ff']],
                showscale=False,
            ),
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#aabbcc'),
            xaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Hour'),
            yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Queries'),
            margin=dict(l=0, r=0, t=10, b=0),
            height=250,
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        st.markdown('<div class="section-header">🌡️ Data Quality Heatmap</div>', unsafe_allow_html=True)
        
        domains = ['Finance', 'Sales', 'HR', 'Ops', 'Mktg']
        metrics_q = ['Completeness', 'Accuracy', 'Timeliness', 'Consistency']
        
        z_data = np.random.uniform(85, 100, (len(metrics_q), len(domains)))
        
        fig = go.Figure(go.Heatmap(
            z=z_data,
            x=domains,
            y=metrics_q,
            colorscale=[[0, '#ff4444'], [0.5, '#ffaa00'], [1, '#00ff88']],
            text=[[f'{v:.1f}%' for v in row] for row in z_data],
            texttemplate='%{text}',
            textfont=dict(size=10, color='white'),
            showscale=False,
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#aabbcc'),
            xaxis=dict(color='#8899bb'),
            yaxis=dict(color='#8899bb'),
            margin=dict(l=0, r=0, t=10, b=0),
            height=250,
        )
        st.plotly_chart(fig, use_container_width=True)

    # Operational Reports Table
    st.markdown('<div class="section-header">📋 Operational Reports — Live Feed</div>', unsafe_allow_html=True)
    
    report_data = {
        'Report Name': ['Daily Sales Summary', 'Finance P&L', 'HR Headcount', 'Ops Efficiency', 'Customer 360', 'Inventory Status'],
        'LOB': ['Sales', 'Finance', 'HR', 'Operations', 'CRM', 'Supply Chain'],
        'Last Run': ['2 min ago', '5 min ago', '1 hr ago', '15 min ago', '3 min ago', '30 min ago'],
        'Status': ['✅ Success', '✅ Success', '✅ Success', '⚠️ Warning', '✅ Success', '✅ Success'],
        'Records': ['1.2M', '450K', '85K', '2.1M', '3.4M', '780K'],
        'Duration': ['1.2s', '2.8s', '0.9s', '4.1s', '1.7s', '2.3s'],
    }
    
    df = pd.DataFrame(report_data)
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )

    # AI Insights Panel
    st.markdown('<div class="section-header">🤖 AI-Generated Insights</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    insights = [
        ("🔴 Anomaly Detected", "Finance ETL pipeline showing 23% higher latency than baseline. Recommend scaling compute resources.", "#ff444422", "#ff4444"),
        ("🟢 Opportunity Found", "Sales data shows 34% higher conversion on Tuesdays. AI recommends shifting campaign budget to mid-week.", "#00ff8822", "#00ff88"),
        ("🔵 Prediction", "Based on current trends, Q2 revenue projected at $52.4M (+8.7% vs Q1). Confidence: 87%.", "#00d4ff22", "#00d4ff"),
    ]
    
    for col, (title, text, bg, border) in zip([col1, col2, col3], insights):
        with col:
            st.markdown(f"""
            <div style='background:{bg}; border:1px solid {border}44; border-radius:12px; padding:16px;'>
                <div style='font-weight:700; color:{border}; margin-bottom:8px;'>{title}</div>
                <div style='font-size:0.85rem; color:#aabbcc;'>{text}</div>
            </div>
            """, unsafe_allow_html=True)
