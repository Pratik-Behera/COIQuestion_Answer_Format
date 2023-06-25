import requests
import json
#Enter OPENAI API key
API_KEY = ""
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def generate_chat_completion(messages, model="gpt-4", temperature=0.7, max_tokens=3000):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
#Input the text data to convert to question answer format
messages = [
    {"role": "system", "content": "You are an expert on Indian Constitution.Your job is to generate high quality questions and answers according to the users requirement and the given text.The set of questions and answers should be factually accurate.It should not be repeated.The answers should be within 200 words.You can use more token if needed to answer the question."},
    {"role": "user", "content": """Generate a set of 20 questions and answers on Constitution of India in jsonl format using the one here as a sample-- {"question": "What are the main components of the Constitution of India?", "answer": "The main components of the Constitution of India are the Preamble, Parts, Schedules, Articles, and Amendments. These elements together form a comprehensive document that lays out the political code, procedures, practices, rights, powers, and duties of the government institutions and sets out fundamental rights, directive principles, and duties of citizens."}using the text given here--
    
"""}
]
response_text = generate_chat_completion(messages)
print(response_text)
with open('response55.txt', 'w') as file:
    file.write(response_text)


#Further Optimisation
#-Automatated data feedinf from directory
#-Automatic token length adjustment 
#-Appending output to single file 