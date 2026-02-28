import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time
import random

def show():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0d2a1a, #0f3460); border-radius:16px; padding:24px; margin-bottom:24px;'>
        <div style='font-size:1.8rem; font-weight:800; color:white;'>🔬 Data Science & AutoML</div>
        <div style='color:#ccddff; margin-top:6px;'>Build, Train & Deploy ML Models | AutoML | Multi-LOB Support</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["🤖 AutoML Builder", "📊 Model Performance", "🚀 Deployed Models", "🔮 Predictions"])

    # ─── TAB 1: AutoML Builder ────────────────────────────────────────────────
    with tabs[0]:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown('<div class="section-header">⚙️ Configure AutoML Pipeline</div>', unsafe_allow_html=True)
            
            lob = st.selectbox("🏢 Line of Business", [
                "Sales — Revenue Forecasting",
                "Finance — Risk Scoring",
                "HR — Employee Churn Prediction",
                "Operations — Demand Forecasting",
                "Marketing — Customer Segmentation",
                "CRM — Lead Scoring",
                "Supply Chain — Inventory Optimization",
            ])
            
            problem_type = st.selectbox("🎯 Problem Type", [
                "Classification", "Regression", "Time Series Forecasting",
                "Clustering", "Anomaly Detection", "NLP / Text Analysis"
            ])
            
            target_col = st.text_input("🎯 Target Variable", placeholder="e.g., churn, revenue, risk_score")
            
            st.markdown("**🔧 Feature Engineering (AI-Assisted)**")
            features = st.multiselect(
                "Select Features",
                ["customer_age", "tenure_months", "monthly_spend", "support_tickets",
                 "last_login_days", "product_usage", "contract_type", "region",
                 "payment_method", "num_products", "satisfaction_score"],
                default=["customer_age", "tenure_months", "monthly_spend", "support_tickets"]
            )
            
            st.markdown("**🤖 AutoML Settings**")
            col_a, col_b = st.columns(2)
            with col_a:
                algorithms = st.multiselect(
                    "Algorithms to Try",
                    ["XGBoost", "Random Forest", "LightGBM", "Neural Network", "Logistic Regression", "SVM"],
                    default=["XGBoost", "Random Forest", "LightGBM"]
                )
            with col_b:
                cv_folds = st.slider("Cross-Validation Folds", 3, 10, 5)
                max_time = st.slider("Max Training Time (min)", 5, 60, 15)
            
            optimize_for = st.selectbox("Optimize For", ["Accuracy", "F1 Score", "AUC-ROC", "RMSE", "Business Value"])
            
            if st.button("🚀 Launch AutoML Training", use_container_width=True, type="primary"):
                st.markdown("---")
                progress_bar = st.progress(0)
                status = st.empty()
                
                training_steps = [
                    (5, "📥 Loading and validating dataset..."),
                    (15, "🔧 Feature engineering & preprocessing..."),
                    (25, "🤖 Training XGBoost model..."),
                    (40, "🌲 Training Random Forest model..."),
                    (55, "⚡ Training LightGBM model..."),
                    (70, "🔍 Running cross-validation..."),
                    (80, "🎯 Hyperparameter optimization..."),
                    (90, "📊 Generating model explanations (SHAP)..."),
                    (95, "✅ Evaluating on test set..."),
                    (100, "🎉 AutoML training complete!"),
                ]
                
                for pct, msg in training_steps:
                    time.sleep(0.5)
                    progress_bar.progress(pct)
                    status.markdown(f"<span style='color:#00d4ff;'>{msg}</span>", unsafe_allow_html=True)
                
                st.success("✅ **AutoML Complete!** Best model: **XGBoost** with AUC-ROC: **0.924**")
                
                col_r1, col_r2, col_r3, col_r4 = st.columns(4)
                col_r1.metric("Best Model", "XGBoost")
                col_r2.metric("AUC-ROC", "0.924", "+0.034 vs baseline")
                col_r3.metric("Accuracy", "91.2%", "+5.1%")
                col_r4.metric("Training Time", "8.3 min", "")
        
        with col2:
            st.markdown('<div class="section-header">📊 Model Comparison</div>', unsafe_allow_html=True)
            
            models_data = {
                'Model': ['XGBoost', 'LightGBM', 'Random Forest', 'Neural Network', 'Logistic Reg.'],
                'AUC-ROC': [0.924, 0.918, 0.901, 0.895, 0.847],
                'Accuracy': [91.2, 90.8, 89.4, 88.7, 84.2],
                'F1 Score': [0.912, 0.905, 0.891, 0.884, 0.839],
                'Train Time': ['2.1m', '1.8m', '3.4m', '8.2m', '0.4m'],
                'Status': ['🏆 Best', '✅ Good', '✅ Good', '⚠️ Slow', '❌ Weak'],
            }
            
            df_models = pd.DataFrame(models_data)
            st.dataframe(df_models, use_container_width=True, hide_index=True)
            
            # Model comparison chart
            fig = go.Figure()
            colors = ['#ffd700', '#00d4ff', '#00ff88', '#ff8800', '#ff4444']
            for i, (model, auc, acc) in enumerate(zip(models_data['Model'], models_data['AUC-ROC'], models_data['Accuracy'])):
                fig.add_trace(go.Scatter(
                    x=[auc], y=[acc],
                    mode='markers+text',
                    name=model,
                    marker=dict(size=20, color=colors[i]),
                    text=[model],
                    textposition='top center',
                    textfont=dict(color=colors[i], size=10),
                ))
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#aabbcc'),
                xaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='AUC-ROC'),
                yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Accuracy (%)'),
                showlegend=False,
                margin=dict(l=0, r=0, t=10, b=0),
                height=280,
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Feature Importance
            st.markdown('<div class="section-header">🔍 Feature Importance (SHAP)</div>', unsafe_allow_html=True)
            
            features_imp = ['monthly_spend', 'tenure_months', 'support_tickets', 'last_login_days', 'satisfaction_score']
            importance = [0.34, 0.28, 0.18, 0.12, 0.08]
            
            fig2 = go.Figure(go.Bar(
                x=importance, y=features_imp,
                orientation='h',
                marker=dict(color=importance, colorscale=[[0, '#0f3460'], [1, '#00d4ff']], showscale=False),
                text=[f'{v:.0%}' for v in importance],
                textposition='outside',
                textfont=dict(color='#aabbcc'),
            ))
            fig2.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#aabbcc'),
                xaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
                yaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
                margin=dict(l=0, r=40, t=10, b=0),
                height=220,
            )
            st.plotly_chart(fig2, use_container_width=True)

    # ─── TAB 2: Model Performance ─────────────────────────────────────────────
    with tabs[1]:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="section-header">📈 ROC Curve</div>', unsafe_allow_html=True)
            
            fpr = np.linspace(0, 1, 100)
            tpr_xgb = np.clip(fpr ** 0.3 + np.random.normal(0, 0.02, 100), 0, 1)
            tpr_rf = np.clip(fpr ** 0.4 + np.random.normal(0, 0.02, 100), 0, 1)
            tpr_lr = np.clip(fpr ** 0.7 + np.random.normal(0, 0.02, 100), 0, 1)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=fpr, y=tpr_xgb, name='XGBoost (AUC=0.924)', line=dict(color='#ffd700', width=2)))
            fig.add_trace(go.Scatter(x=fpr, y=tpr_rf, name='Random Forest (AUC=0.901)', line=dict(color='#00d4ff', width=2)))
            fig.add_trace(go.Scatter(x=fpr, y=tpr_lr, name='Logistic Reg. (AUC=0.847)', line=dict(color='#ff4444', width=2)))
            fig.add_trace(go.Scatter(x=[0,1], y=[0,1], name='Random', line=dict(color='#334466', dash='dash')))
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#aabbcc'),
                legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#aabbcc', size=10)),
                xaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='False Positive Rate'),
                yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='True Positive Rate'),
                margin=dict(l=0, r=0, t=10, b=0),
                height=300,
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown('<div class="section-header">🎯 Confusion Matrix</div>', unsafe_allow_html=True)
            
            cm = np.array([[842, 58], [74, 526]])
            
            fig = go.Figure(go.Heatmap(
                z=cm,
                x=['Predicted: No Churn', 'Predicted: Churn'],
                y=['Actual: No Churn', 'Actual: Churn'],
                colorscale=[[0, '#0f3460'], [1, '#00d4ff']],
                text=cm,
                texttemplate='<b>%{text}</b>',
                textfont=dict(size=18, color='white'),
                showscale=False,
            ))
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#aabbcc'),
                xaxis=dict(color='#8899bb'),
                yaxis=dict(color='#8899bb'),
                margin=dict(l=0, r=0, t=10, b=0),
                height=300,
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Model drift monitoring
        st.markdown('<div class="section-header">📉 Model Drift Monitoring</div>', unsafe_allow_html=True)
        
        dates = pd.date_range(end=pd.Timestamp.now(), periods=30, freq='D')
        accuracy_over_time = 91.2 - np.cumsum(np.random.normal(0.05, 0.3, 30))
        threshold = [88.0] * 30
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=accuracy_over_time, name='Model Accuracy', line=dict(color='#00d4ff', width=2)))
        fig.add_trace(go.Scatter(x=dates, y=threshold, name='Min Threshold (88%)', line=dict(color='#ff4444', dash='dash', width=1)))
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#aabbcc'),
            legend=dict(bgcolor='rgba(0,0,0,0)'),
            xaxis=dict(gridcolor='#1e3a5f', color='#8899bb'),
            yaxis=dict(gridcolor='#1e3a5f', color='#8899bb', title='Accuracy (%)'),
            margin=dict(l=0, r=0, t=10, b=0),
            height=250,
        )
        st.plotly_chart(fig, use_container_width=True)

    # ─── TAB 3: Deployed Models ───────────────────────────────────────────────
    with tabs[2]:
        st.markdown('<div class="section-header">🚀 Production Models Registry</div>', unsafe_allow_html=True)
        
        deployed_data = {
            'Model Name': ['Customer Churn Predictor', 'Revenue Forecaster', 'Lead Scorer', 'Fraud Detector', 'Demand Forecaster', 'Employee Attrition'],
            'LOB': ['CRM', 'Finance', 'Sales', 'Finance', 'Operations', 'HR'],
            'Algorithm': ['XGBoost', 'LSTM', 'LightGBM', 'Isolation Forest', 'Prophet', 'Random Forest'],
            'Version': ['v3.2', 'v2.1', 'v4.0', 'v1.8', 'v2.5', 'v1.3'],
            'Accuracy': ['91.2%', '94.7%', '88.3%', '97.1%', '92.8%', '89.4%'],
            'Predictions/Day': ['45K', '12K', '8K', '2.1M', '5K', '1.2K'],
            'Status': ['🟢 Live', '🟢 Live', '🟢 Live', '🟢 Live', '🟡 Retraining', '🟢 Live'],
        }
        
        df_deployed = pd.DataFrame(deployed_data)
        st.dataframe(df_deployed, use_container_width=True, hide_index=True)
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Models", "12", "+3 this month")
        col2.metric("Daily Predictions", "2.17M", "+8.4%")
        col3.metric("Avg Accuracy", "92.3%", "+1.2%")
        col4.metric("Cost/Prediction", "$0.0002", "-34%")

    # ─── TAB 4: Predictions ───────────────────────────────────────────────────
    with tabs[3]:
        st.markdown('<div class="section-header">🔮 Real-time Predictions</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**Select Model & Input Data**")
            
            model_select = st.selectbox("Choose Model", [
                "Customer Churn Predictor",
                "Lead Scorer",
                "Employee Attrition",
            ])
            
            if "Churn" in model_select:
                age = st.slider("Customer Age", 18, 80, 35)
                tenure = st.slider("Tenure (months)", 1, 120, 24)
                spend = st.number_input("Monthly Spend ($)", 0, 10000, 250)
                tickets = st.slider("Support Tickets (last 3 months)", 0, 20, 2)
                satisfaction = st.slider("Satisfaction Score (1-10)", 1, 10, 7)
                
                if st.button("🔮 Predict Churn Risk", use_container_width=True):
                    # Simulate prediction
                    risk_score = max(0, min(100, 
                        (100 - tenure * 0.5 - satisfaction * 5 + tickets * 8 - spend * 0.01 + random.randint(-5, 5))
                    ))
                    
                    with col2:
                        st.markdown('<div class="section-header">📊 Prediction Result</div>', unsafe_allow_html=True)
                        
                        color = "#ff4444" if risk_score > 70 else "#ffaa00" if risk_score > 40 else "#00ff88"
                        label = "HIGH RISK" if risk_score > 70 else "MEDIUM RISK" if risk_score > 40 else "LOW RISK"
                        
                        st.markdown(f"""
                        <div style='background:linear-gradient(135deg, #1a1a3e, #0d1b2a); border:2px solid {color}; border-radius:16px; padding:30px; text-align:center;'>
                            <div style='font-size:3.5rem; font-weight:900; color:{color};'>{risk_score:.0f}%</div>
                            <div style='font-size:1.2rem; font-weight:700; color:{color}; margin-top:8px;'>CHURN RISK: {label}</div>
                            <div style='font-size:0.85rem; color:#8899bb; margin-top:12px;'>Model Confidence: 94.2%</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown("<br>", unsafe_allow_html=True)
                        
                        # Gauge chart
                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=risk_score,
                            domain={'x': [0, 1], 'y': [0, 1]},
                            gauge={
                                'axis': {'range': [0, 100], 'tickcolor': '#8899bb'},
                                'bar': {'color': color},
                                'bgcolor': '#1a1a3e',
                                'steps': [
                                    {'range': [0, 40], 'color': '#00ff8822'},
                                    {'range': [40, 70], 'color': '#ffaa0022'},
                                    {'range': [70, 100], 'color': '#ff444422'},
                                ],
                                'threshold': {'line': {'color': color, 'width': 4}, 'thickness': 0.75, 'value': risk_score}
                            },
                            number={'font': {'color': color, 'size': 40}},
                        ))
                        fig.update_layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='#aabbcc'),
                            margin=dict(l=20, r=20, t=20, b=20),
                            height=250,
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Recommendations
                        st.markdown("**🤖 AI Recommendations:**")
                        if risk_score > 70:
                            recs = ["🔴 Immediate outreach by account manager", "💰 Offer 20% discount on renewal", "📞 Schedule executive business review"]
                        elif risk_score > 40:
                            recs = ["🟡 Send personalized engagement email", "🎁 Offer loyalty rewards", "📊 Share usage insights report"]
                        else:
                            recs = ["🟢 Continue standard engagement", "📈 Upsell opportunity identified", "⭐ Candidate for referral program"]
                        
                        for rec in recs:
                            st.markdown(f"- {rec}")
