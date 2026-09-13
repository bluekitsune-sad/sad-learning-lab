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
            "content":  f"{user_input}\n\nhere is the formate for the result{response_formate}\n\nhere is the file content:\n{content}"

        }
    ],
    "temperature": 0.7
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
    print("\nAI:", answer)
else:
    print("Error:", data)