import requests

print("Saad Yousuf here")


url = input("enter your website ")


print(f"checking {url}")
url="https://"+url
request = requests.get(url)


print(f"here is the result {request}")