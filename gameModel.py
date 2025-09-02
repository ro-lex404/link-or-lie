def model(url):
    import os
    from google import genai
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key = api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"Check if this url is likely to be a phishing attempt or not {url}"
    )
    
    return response.text