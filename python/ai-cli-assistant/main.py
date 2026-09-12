import json, requests


person={
    "name" : "sad",
    "age" : 22
}


print("Hello ask any Question and I will try to answer it for you")

user_input = input("Enter your question: ")


query = {
    "request" : user_input,
    "model" : "gpt-3.5-turbo",
    "temperature" : 0.7
}
formated_query = json.dumps(query)

response = requests.post("https://api.openai.com/v1/completions", json=formated_query, headers={"Authorization": "Bearer YOUR_API_KEY"})

print(response.json())

print(json.loads(response))