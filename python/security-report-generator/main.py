from scanner import scan
from report import report
from ai_analyzer import analyzer

url = {
    "target": "",
    "status": "",
    "headerResults": {},
    "headersAnalysis": {},
    "aiSummary": ""
}

url["target"] = input("Enter your URL: ")

url["status"], url["headerResults"], url["headersAnalysis"] = scan(url["target"])
url["aiSummary"] = analyzer(url)
report(url)