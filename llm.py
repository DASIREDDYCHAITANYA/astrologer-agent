from groq import Groq
import json

# Set your API key
api_key = "api"
client = Groq(api_key=api_key)


def response_(name,dob,time,place,free_text_question):
    system_prompt = """
    You are an expert astrologer.  
    Your role is to analyze a person's birth details and provide meaningful, positive, and easy-to-understand astrological insights.  

    Your answers should be conversational and feel like a real astrologer speaking to a client.  
    Always give guidance in a respectful and optimistic way.  
    """



# User prompt with inputs
    user_prompt = f"""
    Here are the user's birth details:  
    - Name: {name}  
    - Date of Birth: {dob}  
    - Time of Birth: {time}  
    - Place of Birth: {place}  

    Please provide an astrological reading for this person.

    User's specific question: "{free_text_question}"
    """       

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]




    chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            seed=None,
            max_tokens=2000,
            stream=False,
        )
    return chat_completion.choices[0].message.content
