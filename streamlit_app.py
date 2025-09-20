import base64
from io import BytesIO

import streamlit as st
from streamlit.components.v1 import html as st_html
from PIL import Image

with open("assets/icon.png", "rb") as icon_file:
    icon_bytes = icon_file.read()

page_icon = Image.open(BytesIO(icon_bytes)).resize((32, 32), Image.LANCZOS)
brand_icon_data = base64.b64encode(icon_bytes).decode("utf-8")

st.set_page_config(page_title="Outwize", page_icon=page_icon, layout="centered")

# --- Styles ---
st.markdown(
    """
    <style>
    /* Center content and adjust max width */
    .main .block-container { max-width: 820px; padding-top: 2rem; padding-bottom: 3rem; }

    /* Brand */
    .outwize-brand { font-weight: 600; color: #0f172a; display: flex; align-items: center; gap: 10px; }
    .outwize-icon { height: 28px; width: 28px; display: inline-flex; align-items: center; justify-content: center; border-radius: 9999px; background: #ecebff; overflow: hidden; }
    .outwize-icon img { height: 100%; width: 100%; object-fit: contain; }

    /* Headline + subtitle */
    h1.outwize-hero { font-size: 56px; line-height: 1.05; margin: 10px 0 8px; font-weight: 800; letter-spacing: -0.02em; }
    p.outwize-sub { font-size: 22px; color: #334155; margin-bottom: 24px; }
    p.outwize-sub .highlight { color: #b91c1c; font-weight: 700; }

    /* Buttons */
    .stButton>button {
      width: 100%; padding: 14px 18px; border-radius: 12px; border: 1px solid #3f3cf6;
      background: #3f3cf6; color: white; text-transform: uppercase; letter-spacing: 0.6px;
      font-weight: 800; font-size: 18px;
      box-shadow: 0 2px 0 rgba(0,0,0,0.08), 0 8px 24px rgba(63,60,246,0.28);
    }
    .stButton>button:hover { filter: brightness(1.02); }

    /* Expanders */
    div.streamlit-expanderHeader { font-size: 20px; font-weight: 700; }
    div.streamlit-expander { border: 1px solid #e2e8f0; border-radius: 14px; }
    div.streamlit-expander + div.streamlit-expander { margin-top: 14px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
header_html = (
    f'<div class="outwize-brand"><span class="outwize-icon">'
    f'<img src="data:image/png;base64,{brand_icon_data}" alt="Outwize logo" />'
    f'</span><span>Outwize</span></div>'
)

st.markdown(header_html, unsafe_allow_html=True)

# --- Hero ---
st.markdown('<h1 class="outwize-hero">Recruit smarter agents.</h1>', unsafe_allow_html=True)
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
st.write("")
with st.expander("How it works"):
    st.write("• Tell us what you need. • We shortlist agent options. • You hire with confidence.")

with st.expander("Why Outwize"):
    st.write("We benchmark, vet, and match specialized AI agents for real business outcomes.")

with st.expander("Popular agent roles"):
    st.write("• Sales and SDR • RevOps • Marketing Ops • Support and CX • Data automation • Custom internal tools")

with st.expander("Contact"):
    st.write("Coming soon")
