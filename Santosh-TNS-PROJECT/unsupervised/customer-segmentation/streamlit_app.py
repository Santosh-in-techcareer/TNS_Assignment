from pathlib import Path

import joblib
import pandas as pd
import requests
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "customers.csv"
MODEL_PATH = BASE_DIR / "kmeans_model.pkl"
API_URL = "http://127.0.0.1:8000/predict"
PERSONA_MAP = {
    0: "Careful Spenders",
    1: "Top Spenders",
    2: "Frequent Buyers",
}

st.set_page_config(
    page_title="Customer Intelligence",
    page_icon="C",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --page: #eaf3f2;
        --surface: #ffffff;
        --ink: #172e32;
        --muted: #718386;
        --line: #e5eeed;
        --teal: #247f87;
        --teal-dark: #155b65;
        --mint: #dff2ed;
        --gold: #e7b95e;
    }
    .stApp {
        background: var(--page);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"] { right: 1.5rem; }
    [data-testid="stSidebar"] {
        background: #f8fbfa;
        border-right: 1px solid #dce8e6;
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: var(--muted); }
    [data-testid="stSidebar"] [data-testid="stRadio"] label {
        padding: .55rem .7rem;
        border-radius: 10px;
        font-weight: 600;
    }
    [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
        background: #e1f0ed;
        color: var(--teal-dark);
    }
    .block-container { max-width: 1500px; padding: 1.7rem 3rem 2.5rem; }
    h1, h2, h3, p, div, span, label { letter-spacing: 0 !important; }
    h1, h2, h3 { font-family: 'Manrope', sans-serif !important; color: var(--ink); }
    .eyebrow {
        color: var(--teal) !important;
        font-size: .68rem;
        font-weight: 700;
        letter-spacing: 1.4px !important;
        text-transform: uppercase;
    }
    .page-title {
        margin: .1rem 0 .15rem;
        color: var(--ink);
        font: 800 clamp(1.7rem, 3vw, 2.35rem)/1.18 'Manrope', sans-serif;
    }
    .page-subtitle { margin: 0; color: var(--muted); font-size: .9rem; }
    .top-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #dce8e6;
        color: var(--muted);
        font-size: .72rem;
        font-weight: 700;
        letter-spacing: 1px !important;
        text-transform: uppercase;
    }
    .live-tag {
        padding: .45rem .65rem;
        border: 1px solid #cde8df;
        border-radius: 999px;
        background: #eff9f4;
        color: #347d63;
        white-space: nowrap;
    }
    .metric-card, .panel {
        border: 1px solid #e2ecea;
        border-radius: 13px;
        background: var(--surface);
        box-shadow: 0 5px 20px rgba(40, 80, 79, .035);
    }
    .metric-card { min-height: 121px; padding: 1.05rem 1.15rem; }
    .metric-top { display: flex; align-items: center; justify-content: space-between; gap: .5rem; }
    .metric-label { color: var(--muted); font-size: .75rem; font-weight: 600; }
    .metric-icon {
        display: grid;
        width: 29px;
        height: 29px;
        place-items: center;
        border-radius: 9px;
        background: var(--mint);
        color: var(--teal);
        font-size: .85rem;
        font-weight: 700;
    }
    .metric-value { margin-top: .45rem; color: var(--ink); font: 800 1.55rem 'Manrope', sans-serif; }
    .metric-foot { margin-top: .2rem; color: #8a999a; font-size: .68rem; }
    .section-title { margin: 0; color: var(--ink); font: 700 1rem 'Manrope', sans-serif; }
    .section-description { margin: .25rem 0 .8rem; color: var(--muted); font-size: .75rem; }
    .panel { padding: 1.15rem 1.2rem; }
    .panel-head { display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; margin-bottom: .55rem; }
    .panel-kicker { color: #90a0a0; font-size: .65rem; font-weight: 700; letter-spacing: 1px !important; text-transform: uppercase; }
    .predict-result {
        margin-top: 1rem;
        padding: 1rem;
        border-left: 3px solid var(--teal);
        border-radius: 8px;
        background: #f0f8f6;
    }
    .predict-result-label { color: var(--muted); font-size: .68rem; font-weight: 700; letter-spacing: 1px !important; text-transform: uppercase; }
    .predict-result-value { margin-top: .2rem; color: var(--teal-dark); font: 800 1.2rem 'Manrope', sans-serif; }
    div[data-testid="stButton"] > button, div[data-testid="stFormSubmitButton"] > button {
        min-height: 2.65rem;
        border: 0;
        border-radius: 9px;
        background: var(--teal);
        color: #fff;
        font-weight: 700;
        transition: background .18s, transform .18s;
    }
    div[data-testid="stButton"] > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        border: 0;
        background: var(--teal-dark);
        color: #fff;
        transform: translateY(-1px);
    }
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        border-color: #dce7e5;
        border-radius: 8px;
        background: #fff;
    }
    [data-testid="stMetric"] { padding: .3rem 0; }
    [data-testid="stMetricLabel"] { color: var(--muted); }
    [data-testid="stMetricValue"] { color: var(--ink); }
    [data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 9px; }

    [data-testid="stWidgetLabel"] p {
        color: var(--ink) !important;
        font-weight: 600;
        font-size: .8rem;
    }
    .form-hint {
        margin: 0 0 .8rem;
        color: var(--teal-dark);
        font-size: .8rem;
        font-weight: 600;
    }

    .sidebar-brand { display: flex; align-items: center; gap: .65rem; margin: .2rem 0 1.4rem; }
    .brand-mark {
        display: grid;
        width: 36px;
        height: 36px;
        place-items: center;
        border-radius: 11px;
        background: var(--teal);
        color: white;
        font: 800 1.15rem 'Manrope', sans-serif;
    }
    .brand-name { color: var(--ink); font: 800 .95rem 'Manrope', sans-serif; }
    .brand-caption { margin-top: .05rem; color: #829193; font-size: .64rem; }
    @media (max-width: 800px) {
        .block-container { padding: 1rem 1.1rem 2rem; }
        .top-meta { align-items: flex-start; }
        .metric-card { min-height: 105px; padding: .85rem; }
        .metric-value { font-size: 1.25rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_customers():
    return pd.read_csv(DATA_PATH)


@st.cache_resource
def load_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    return None


def metric_card(label, value, note, icon):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-top">
                <span class="metric-label">{label}</span>
                <span class="metric-icon">{icon}</span>
            </div>
            <div class="metric-value">{value}</div>
            <div class="metric-foot">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_header(section):
    st.markdown(
        f"""
        <div class="top-meta">
            <span>Customer intelligence&nbsp;&nbsp; / &nbsp;&nbsp;{section}</span>
            <span class="live-tag">●&nbsp; DATASET CONNECTED</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def predictor_panel(key_suffix="overview"):
    st.markdown(
        """
        <div class="panel-head">
            <div>
                <p class="panel-kicker">Segment finder</p>
                <h3 class="section-title">Profile a customer</h3>
                <p class="section-description">Enter income and spending score to see which customer group they belong to.</p>
            </div>
            <span class="metric-icon">↗</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form(f"segment-form-{key_suffix}"):
        st.markdown(
            '<p class="form-hint">Enter the customer\'s annual income and spending score (1-100)</p>',
            unsafe_allow_html=True,
        )
        annual_income = st.number_input(
            "Annual income (k$)",
            min_value=0.0,
            max_value=150.0,
            value=50.0,
            step=1.0,
            key=f"income-{key_suffix}",
        )
        spending_score = st.number_input(
            "Spending score",
            min_value=1.0,
            max_value=100.0,
            value=50.0,
            step=1.0,
            key=f"spending-{key_suffix}",
        )
        submitted = st.form_submit_button("Find customer segment", use_container_width=True)

    if submitted:
        try:
            response = requests.post(
                API_URL,
                json={
                    "annual_income_k": annual_income,
                    "spending_score": spending_score,
                },
                timeout=5,
            )
            response.raise_for_status()
            st.session_state[f"prediction-{key_suffix}"] = response.json()
            st.session_state.pop(f"prediction-error-{key_suffix}", None)
        except requests.RequestException as error:
            st.session_state[f"prediction-error-{key_suffix}"] = str(error)
            st.session_state.pop(f"prediction-{key_suffix}", None)

    prediction = st.session_state.get(f"prediction-{key_suffix}")
    if prediction:
        st.markdown(
            f"""
            <div class="predict-result">
                <div class="predict-result-label">Predicted persona · Cluster {prediction['cluster']}</div>
                <div class="predict-result-value">{prediction['persona']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    error = st.session_state.get(f"prediction-error-{key_suffix}")
    if error:
        st.error("Could not reach the segmentation API. Start the customer backend on port 8000.")


try:
    customers = load_customers()
except (OSError, pd.errors.ParserError) as error:
    st.error(f"Could not load the customer dataset: {error}")
    st.stop()

required_columns = {"annual_income_k", "spending_score"}
if not required_columns.issubset(customers.columns):
    st.error("The customer dataset must include annual_income_k and spending_score columns.")
    st.stop()

customers = customers.dropna(subset=list(required_columns)).copy()
model = load_model()
if model is not None:
    try:
        cluster_ids = model.predict(customers[["annual_income_k", "spending_score"]])
        customers["Persona"] = [
            PERSONA_MAP.get(int(cluster_id), f"Segment {int(cluster_id) + 1}")
            for cluster_id in cluster_ids
        ]
    except (AttributeError, ValueError, TypeError):
        customers["Persona"] = "Unclassified"
else:
    customers["Persona"] = "Unclassified"

st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <span class="brand-mark">C</span>
        <div><div class="brand-name">CUSTOMER IQ</div><div class="brand-caption">SEGMENTATION STUDIO</div></div>
    </div>
    <p class="eyebrow">WORKSPACE</p>
    """,
    unsafe_allow_html=True,
)
view = st.sidebar.radio(
    "Workspace navigation",
    ["Overview", "Predictor"],
    label_visibility="collapsed",
)
st.sidebar.markdown("---")
st.sidebar.markdown(f"**{len(customers):,}** customer profiles")
st.sidebar.caption("Annual income and spending score dataset")
st.sidebar.markdown(
    '<div class="live-tag">MODEL FILE FOUND</div>' if model is not None else
    '<div class="live-tag">MODEL FILE MISSING</div>',
    unsafe_allow_html=True,
)

page_header(view)

if view == "Overview":
    chart_column, predictor_column = st.columns([1.55, 1], gap="medium")
    with chart_column:
        st.markdown(
            """
            <div class="panel-head">
                <div>
                    <p class="panel-kicker">Behavior map</p>
                    <h3 class="section-title">Income &amp; spending</h3>
                    <p class="section-description">Each point represents one customer profile.</p>
                </div>
                <span class="metric-icon">◉</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.scatter_chart(
            customers,
            x="annual_income_k",
            y="spending_score",
            color="Persona" if model is not None else None,
            x_label="Annual income (k$)",
            y_label="Spending score",
            height=355,
        )
        st.caption("Customer dataset · K-means persona assignments")

    with predictor_column:
        predictor_panel()

else:
    predictor_column, detail_column = st.columns([1, 1.3], gap="large")
    with predictor_column:
        predictor_panel("page")
    with detail_column:
        st.markdown(
            """
            <div class="panel-head">
                <div>
                    <p class="panel-kicker">Customer distribution</p>
                    <h3 class="section-title">Explore the profile space</h3>
                    <p class="section-description">Compare income and spending across all known customers.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.scatter_chart(
            customers,
            x="annual_income_k",
            y="spending_score",
            color="Persona" if model is not None else None,
            x_label="Annual income (k$)",
            y_label="Spending score",
            height=430,
        )

st.markdown(
    '<div style="margin-top:2rem;padding-top:1rem;border-top:1px solid #dce8e6;color:#849394;font-size:.7rem;">CUSTOMER INTELLIGENCE &nbsp; · &nbsp; K-MEANS SEGMENTATION</div>',
    unsafe_allow_html=True,
)