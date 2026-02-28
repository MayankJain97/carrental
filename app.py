import streamlit as st
import os
os.system("pip install plotly")
import plotly.graph_objects as go

st.set_page_config(
    page_title="SmartData Hub",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        border-right: 1px solid #0f3460;
    }
    
    /* Cards */
    .metric-card {
        background: linear-gradient(135deg, #1e3a5f, #0f2744);
        border: 1px solid #1e90ff33;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(30, 144, 255, 0.15);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(30, 144, 255, 0.3);
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #00d4ff;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #8899aa;
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-delta {
        font-size: 0.9rem;
        color: #00ff88;
        margin-top: 6px;
    }
    
    /* Hero banner */
    .hero-banner {
        background: linear-gradient(135deg, #0f3460, #533483, #e94560);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(233, 69, 96, 0.3);
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 900;
        color: white;
        margin: 0;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #ccddff;
        margin-top: 10px;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(135deg, #1a1a3e, #0d1b2a);
        border: 1px solid #334466;
        border-radius: 16px;
        padding: 24px;
        height: 100%;
        transition: all 0.3s;
    }
    .feature-card:hover {
        border-color: #00d4ff;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 12px;
    }
    .feature-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #00d4ff;
        margin-bottom: 8px;
    }
    .feature-desc {
        font-size: 0.85rem;
        color: #8899bb;
        line-height: 1.5;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #00d4ff;
        border-left: 4px solid #e94560;
        padding-left: 12px;
        margin: 20px 0 15px 0;
    }
    
    /* Status badges */
    .badge-green {
        background: #00ff8822;
        color: #00ff88;
        border: 1px solid #00ff8844;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .badge-blue {
        background: #00d4ff22;
        color: #00d4ff;
        border: 1px solid #00d4ff44;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .badge-orange {
        background: #ff880022;
        color: #ff8800;
        border: 1px solid #ff880044;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    /* Streamlit overrides */
    .stSelectbox label, .stTextInput label, .stTextArea label {
        color: #aabbcc !important;
    }
    div[data-testid="stMetricValue"] {
        color: #00d4ff !important;
        font-size: 1.8rem !important;
    }
    div[data-testid="stMetricDelta"] {
        color: #00ff88 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: #1a1a3e;
        border-radius: 10px;
        padding: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #8899bb;
        border-radius: 8px;
    }
    .stTabs [aria-selected="true"] {
        background: #0f3460 !important;
        color: #00d4ff !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0f3460, #533483);
        color: white;
        border: 1px solid #00d4ff44;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1e5090, #7344a3);
        border-color: #00d4ff;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
        transform: translateY(-1px);
    }
    
    /* Chat messages */
    .chat-user {
        background: linear-gradient(135deg, #0f3460, #1e5090);
        border-radius: 16px 16px 4px 16px;
        padding: 14px 18px;
        margin: 8px 0;
        color: white;
        max-width: 80%;
        margin-left: auto;
        border: 1px solid #1e90ff33;
    }
    .chat-bot {
        background: linear-gradient(135deg, #1a1a3e, #0d1b2a);
        border-radius: 16px 16px 16px 4px;
        padding: 14px 18px;
        margin: 8px 0;
        color: #ccddff;
        max-width: 85%;
        border: 1px solid #334466;
    }
    
    /* Pipeline steps */
    .pipeline-step {
        background: linear-gradient(135deg, #1e3a5f, #0f2744);
        border: 1px solid #1e90ff33;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        position: relative;
    }
    .pipeline-step-active {
        border-color: #00d4ff;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #1a1a2e; }
    ::-webkit-scrollbar-thumb { background: #334466; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #00d4ff; }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0;'>
        <div style='font-size:3rem;'>🧠</div>
        <div style='font-size:1.4rem; font-weight:800; color:#00d4ff;'>SmartData Hub</div>
        <div style='font-size:0.75rem; color:#8899bb; margin-top:4px;'>Modern AI Data Platform</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    page = st.selectbox(
        "🗺️ Navigate",
        [
            "🏠 Home — Overview",
            "📊 BI Dashboard",
            "🔄 Data Ingestion",
            "🤖 AI Chatbot (NL2SQL)",
            "🔬 Data Science & AutoML",
            "💰 Cost Optimizer",
            "🏗️ Architecture"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Platform Status
    st.markdown("### 🟢 Platform Status")
    st.markdown("""
    <div style='font-size:0.8rem; color:#8899bb;'>
        <div style='margin:6px 0;'>🟢 Data Pipelines: <span style='color:#00ff88;'>Active</span></div>
        <div style='margin:6px 0;'>🟢 AI Engine: <span style='color:#00ff88;'>Running</span></div>
        <div style='margin:6px 0;'>🟢 Cloud Storage: <span style='color:#00ff88;'>Connected</span></div>
        <div style='margin:6px 0;'>🟡 ML Models: <span style='color:#ffaa00;'>3 Training</span></div>
        <div style='margin:6px 0;'>🟢 BI Reports: <span style='color:#00ff88;'>Live</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.7rem; color:#556677; text-align:center;'>
        Built with ❤️ using Streamlit<br>
        Modern Data Platform v2.0
    </div>
    """, unsafe_allow_html=True)

# Route to pages
if "🏠 Home" in page:
    from pages import home
    home.show()
elif "📊 BI Dashboard" in page:
    from pages import bi_dashboard
    bi_dashboard.show()
elif "🔄 Data Ingestion" in page:
    from pages import data_ingestion
    data_ingestion.show()
elif "🤖 AI Chatbot" in page:
    from pages import ai_chatbot
    ai_chatbot.show()
elif "🔬 Data Science" in page:
    from pages import data_science
    data_science.show()
elif "💰 Cost Optimizer" in page:
    from pages import cost_optimizer
    cost_optimizer.show()
elif "🏗️ Architecture" in page:
    from pages import architecture
    architecture.show()
