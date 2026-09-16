from scanner import initializer
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Security Report Generator"}

@app.post("/scan")
async def scan(url:str):
    scan_result = initializer(url)
    return {"message": scan_result}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")

# url = {
#     "target": "",
#     "status": "",
#     "headerResults": {},
#     "headersAnalysis": {},
#     "aiSummary": ""
# }

# url["target"] = input("Enter your URL: ")

# url["status"], url["headerResults"], url["headersAnalysis"] = scan(url["target"])
# url["aiSummary"] = analyzer(url)
# report(url)