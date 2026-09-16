folder = "reports/"

def report(url):
    print(f"now generating report")

    print("target:", url["target"])
    print("status:", url["status"])
    for findings in url["headersAnalysis"]:
        print(f" - {findings}: {url['headersAnalysis'][findings]['status']}")
    print("ai summary:", url["aiSummary"])

    report_location = folder + url["target"] + ".json"
    try:
        with open(report_location, "w") as file:
            file.write(str(url))
    except FileNotFoundError:
        print("file not found")
        raise
    