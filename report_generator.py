from fpdf import FPDF
import os
import unicodedata

class CustomPDF(FPDF):
    def header(self):
        """ Stylish Header with Background and Shadow Effect """
        self.set_fill_color(52, 152, 219)  # Blue Header
        self.rect(0, 0, 210, 15, 'F')  # Full-width rectangle
        self.set_font("Arial", "B", 16)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, "AI Research Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        """ Footer with Page Number and Line """
        self.set_y(-20)
        self.set_font("Arial", "I", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        """ Chapter Titles with Borders & Backgrounds """
        self.set_fill_color(231, 76, 60)  # Red Background
        self.set_text_color(255, 255, 255)  # White Text
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, sanitize_text(title), ln=True, align="C", fill=True)
        self.ln(5)

    def chapter_body(self, body):
        """ Chapter Content with Styled Borders """
        self.set_fill_color(236, 240, 241)  # Light Gray Background
        self.set_draw_color(44, 62, 80)  # Dark Blue Border
        self.set_line_width(0.5)
        self.set_font("Arial", "", 12)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 8, sanitize_text(body), border=1, align="L", fill=True)
        self.ln(5)

def sanitize_text(text):
    """ Convert Unicode to ASCII-safe text """
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

def generate_pdf(summary_text, filename="output/ai_research_report.pdf"):
    pdf = CustomPDF()
    pdf.add_page()

    sections = summary_text.split("### ")
    for section in sections:
        if not section.strip():
            continue
        lines = section.strip().split("\n", 1)
        title = lines[0]
        body = lines[1] if len(lines) > 1 else ""
        pdf.chapter_title(title.strip())
        pdf.chapter_body(body.strip())

    os.makedirs("output", exist_ok=True)
    pdf.output(filename)
    return filename

# Example Usage
summary_text = """
### Introduction
This report explores AI's impact on modern technology and innovation.

### Machine Learning
Machine learning techniques drive advancements in automation and data analysis.

### Conclusion
AI continues to revolutionize industries, shaping the future.
"""

generate_pdf(summary_text)
