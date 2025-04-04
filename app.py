import streamlit as st
from gemini_summarizer import generate_summary
from scraper import get_articles
from report_generator import generate_pdf

# Set Page Config
st.set_page_config(page_title="AI Research Report Generator", layout="centered", page_icon="📄")

# Custom CSS for Brighter Report and Title
st.markdown(
    """
    <style>
        body { background: #f5f5f5; color: #111; font-family: Arial, sans-serif; }
        .title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            background: -webkit-linear-gradient(45deg, #ff6a00, #ffea00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding: 10px;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        }
        .stTextInput > div > div > input {
            font-size: 18px;
            border: 2px solid #333;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff6a00, #ffea00);
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px 24px;
            border: none;
        }
        .stButton>button:hover { background: linear-gradient(90deg, #ffea00, #ff6a00); }
        .report-container {
            background: #fff;
            color: #000;
            font-size: 18px;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            margin-top: 20px;
        }
        .footer {
            text-align: center;
            color: #666;
            font-size: 14px;
            margin-top: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Brighter Title with Gradient Effect
st.markdown('<div class="title">📄 AI Research Report Generator</div>', unsafe_allow_html=True)
st.write("Generate clean and structured research reports using AI.")

st.markdown("### 🔍 Enter a topic below")
topic = st.text_input("", placeholder="e.g., AI in Healthcare 2025")

if st.button("🚀 Generate Report", key="generate_btn"):
    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("⏳ Fetching articles and generating report..."):
            articles = get_articles(topic, max_results=3)
            if not articles:
                st.error("❌ No articles found. Try a different topic.")
            else:
                summaries = [f"### {article['title']}\n{generate_summary(article['content'])}\n" for article in articles]
                final_report = "\n\n".join(summaries)
                st.success("✅ Report ready!")
                st.markdown(f'<div class="report-container">{final_report}</div>', unsafe_allow_html=True)
                pdf_path = generate_pdf(final_report)
                with open(pdf_path, "rb") as f:
                    st.download_button(label="📄 Download Report as PDF", data=f, file_name="ai_research_report.pdf",
                                       mime="application/pdf", key="download_pdf_btn")

st.markdown('<div class="footer">Powered by AI Research & Innovation</div>', unsafe_allow_html=True)
