from scanner import initializer
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class URL(BaseModel): 
    url:str
    



@app.get("/")
async def root():
    return {"message": "Welcome to the Security Report Generator"}

@app.post("/scan")
async def scan(target: URL):
    scan_result = initializer(target.url)
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