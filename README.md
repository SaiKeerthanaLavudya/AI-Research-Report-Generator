# AI-Research-Report-Generator
The AI Research Report Generator is a smart, AI-powered tool that helps users generate clean, structured research reports on any topic. It fetches real-world articles, summarizes key insights using AI, and allows users to download a professional PDF report—all with a simple click.
## Features

🔍 Real-Time Web Scraping – Fetches the latest articles on your chosen topic.

🤖 AI-Powered Summarization – Uses Google Gemini AI to distill key insights.

📄 Instant PDF Report – Generates a well-structured report in a downloadable format.

🎨 Modern UI – Built with Streamlit for a fast, user-friendly experience.

🔑 Secure API Management – Stores sensitive API keys safely in a .env file.

 

## Tech Stack

💻 Python – The powerhouse behind the app.

📊 Streamlit – Creates an intuitive web-based interface.

🧠 Google Gemini API – Summarizes text with AI.

🌍 duckduckgo-search – Retrieves relevant articles.

📰 newspaper3k – Extracts content from articles.

📄 fpdf – Converts summaries into a polished PDF report.

🔐 dotenv – Keeps API credentials secure.

## Project 

![Screenshot 1](Images/Screenshot%202025-04-03%20230757.png)

![Screenshot 2](Images/Screenshot%202025-04-03%20230811.png)
## LIVE
[Access the AI Research Report Generator](https://ai-research-report-generator.onrender.com)

## How to Run

1. Clone this repository:
```
git clone https://github.com/SaiKeerthanaLavudya/AI-Research-Report-Generator.git
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

🚀 Simplify research with AI-driven automation! Try it now! 🎯
