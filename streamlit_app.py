import base64
from io import BytesIO

import streamlit as st
from streamlit.components.v1 import html as st_html
from PIL import Image


def load_icon_assets(icon_path: str) -> tuple[Image.Image, str]:
    """Return a favicon-sized icon and a base64 string for inline usage."""

    with Image.open(icon_path) as icon_source:
        favicon = icon_source.resize((32, 32), Image.LANCZOS)
        header_icon = icon_source.resize((56, 56), Image.LANCZOS)

    buffer = BytesIO()
    header_icon.save(buffer, format="PNG")
    icon_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return favicon, icon_b64


page_icon, brand_icon_data = load_icon_assets("assets/icon.png")

st.set_page_config(page_title="Outwize", page_icon=page_icon, layout="centered")

st.markdown(
    """
    <style>
    .main .block-container { max-width: 820px; padding-top: 2rem; padding-bottom: 3rem; }

    .outwize-brand { font-weight: 600; color: #0f172a; display: flex; align-items: center; gap: 10px; }
    .outwize-icon {
      height: 48px; width: 48px; display: inline-flex; align-items: center; justify-content: center;
      border-radius: 9999px; box-shadow: 0 6px 18px rgba(79, 70, 229, 0.15);
    }
    .outwize-icon img {
      height: 100%; width: 100%; display: block; border-radius: 50%; object-fit: cover;
    }
    .outwize-name { font-size: 20px; }

    h1 { font-size: 56px !important; line-height: 1.05; margin: 0 0 8px !important; font-weight: 800 !important; letter-spacing: -0.02em; color: #0f172a; }
    .outwize-sub { font-size: 22px; color: #334155; margin-bottom: 28px; }
    .outwize-sub .highlight { color: #b91c1c; font-weight: 700; }

    .stButton>button {
      width: 100%; padding: 14px 18px; border-radius: 12px; border: 1px solid #3f3cf6;
      background: linear-gradient(135deg, #3f3cf6, #473bfd); color: white; text-transform: uppercase;
      letter-spacing: 0.6px; font-weight: 800; font-size: 18px;
      box-shadow: 0 2px 0 rgba(0,0,0,0.08), 0 12px 30px rgba(63,60,246,0.3);
    }
    .stButton>button:hover { filter: brightness(1.05); }

    div.streamlit-expanderHeader { font-size: 20px; font-weight: 700; color: #1e293b; }
    div.streamlit-expander { border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 6px 16px rgba(15, 23, 42, 0.06); }
    div.streamlit-expander + div.streamlit-expander { margin-top: 14px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
st.markdown(
    f"""
    <div class="outwize-brand">
        <span class="outwize-icon"><img src="data:image/png;base64,{brand_icon_data}" alt="Outwize logo" /></span>
        <span class="outwize-name">Outwize</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# --- Hero ---
st.title("Recruit smarter agents.")
st.markdown(
    """
    <p class="outwize-sub">Outwize is the <span class="highlight">world's first</span> headhunter for AI agents.</p>
    """,
    unsafe_allow_html=True,
)

# --- Actions ---
col1, col2 = st.columns(2, gap="large")
with col1:
    hire_clicked = st.button("HIRE", use_container_width=True, key="hire_button")
with col2:
    st.button("GET HIRED", use_container_width=True, key="get_hired_button")

if hire_clicked:
    st.session_state["show_hire"] = True

if st.session_state.get("show_hire"):
    st_html(
        """
        <script type="module">
          import Typebot from 'https://cdn.jsdelivr.net/npm/@typebot.io/js@0/dist/web.js';
          Typebot.initStandard({ typebot: "outwize" });
        </script>
        <typebot-standard style="width: 100%; height: 600px;"></typebot-standard>
        """,
        height=620,
    )

# --- Information sections ---
st.divider()
with st.expander("How it works"):
    st.markdown(
        "- Tell us what you need.\n"
        "- We shortlist agent options.\n"
        "- You hire with confidence."
    )

with st.expander("Why Outwize"):
    st.write("We benchmark, vet, and match specialized AI agents for real business outcomes.")

with st.expander("Popular agent roles"):
    st.markdown(
        "- Sales and SDR\n"
        "- RevOps\n"
        "- Marketing Ops\n"
        "- Support and CX\n"
        "- Data automation\n"
        "- Custom internal tools"
    )

with st.expander("Contact"):
    st.write("Coming soon")
