import google.generativeai as genai

# Configure the API (Make sure to replace with your actual key)
genai.configure(api_key="your_API_key")  # Replace with actual API key

def generate_summary(text):
    """Generate a summary using Gemini AI"""
    model = genai.GenerativeModel("gemini-1.5-pro")  # Use the latest model
    response = model.generate_content(text)
    return response.text if response and hasattr(response, "text") else "Summary generation failed."
