import json, requests, os
from dotenv import load_dotenv
# from ai_document_analyzer.main import load_doc

load_dotenv("../../.env")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY was not found in the .env file")

# person={
#     "name" : "sad",
#     "age" : 22
# }
response_formate = {
     "topic": "",
     "keypoints": [], 
     "summary": "",
     "recommendations": []
     }

try:
       with open("../ai-document-analyzer/test.txt","r") as file:
           content = file.read()
           
except FileNotFoundError:
       print("file not found")
       raise 

user_input = input("Enter your prompt: ")


payload = {
    "model": "nvidia/nemotron-3.5-lightning:free",
    "messages": [
        {
            "role": "user",
            "content": f"""
{user_input}

Return the result as JSON matching this structure:
{json.dumps(response_formate)}

File content:
{content}
"""
        }
    ],
    "temperature": 0.7,
    "response_format": {
        "type": "json_object"
    }
}


# formated_payload = json.dumps(payload)

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    },
    json=payload
)
# print(response.json())

# print(json.loads(response))

data = response.json()

if response.ok:
    answer = data["choices"][0]["message"]["content"]

    try:
        result = json.loads(answer)
        print(json.dumps(result, indent=4))
    except json.JSONDecodeError:
        print("Model did not return valid JSON:")
        print(answer)
else:
    print("Error:", data)