# AI-Research-Report-Generator
The AI Research Report Generator is a smart, AI-powered tool that helps users generate clean, structured research reports on any topic. It fetches real-world articles, summarizes key insights using AI, and allows users to download a professional PDF report—all with a simple click.
## Features

✅ Live Web Scraping – Fetches the latest research articles and news on your topic.

✅ AI Summarization (Gemini AI) – Uses Google Gemini to generate concise and structured summaries.

✅ PDF Report Generation – Converts AI-generated summaries into a downloadable PDF.

✅ Streamlit-Based UI – A fast, interactive, and visually appealing frontend.

✅ Secure API Key Handling – Uses .env file for safe Gemini API key management. 

## Tech Stack

Python – Core programming language.

Streamlit – For building an interactive and modern UI.

Google Gemini API – For AI-powered text summarization.

duckduckgo-search – For retrieving relevant articles.

newspaper3k – For web scraping and article extraction.

fpdf – For generating high-quality PDF reports.

dotenv – For secure API key management.



## How to Run

1. Clone this repository:
```
git clone https://github.com/RamcharanSinghRamavath/AI-Research-Report-Generator.git
cd AI-Research-Report-Generator
```


3. Install the dependencies:

```
pip3 install -r requirements.txt
```

3. Add your Gemini API key to a `.env` file:

```
GEMINI_API_KEY=your-api-key-here
```

1. Run the app locally:

```
streamlit run app.py
```

## Example Output

The app fetches real-time articles, generates clean AI summaries, and presents them in a bright and structured UI.

You can download the AI-generated report in a professional PDF format.



## 🤝 Contributing
Pull requests are welcome! If you’d like to add new features, improve the UI, or optimize performance, feel free to contribute.
