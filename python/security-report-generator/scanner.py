import requests


def scan(url):
    if not url.startswith(("http://", "https://")):
        print("Invalid URL. Please provide a valid URL starting with http:// or https://")
        return

    print("Scanning URL:", url)

    try:
        response = requests.get(url, timeout=10) # 10 sec

    except requests.exceptions.RequestException:
        print("Unable to reach website.")
        return

    print("Scan successful")
    print("Status code:", response.status_code)

    headerAnalysis = headerCheck(response.headers)

    return response.status_code, response.headers, headerAnalysis


def headerCheck(headers):
    security_headers = {
        "Content-Security-Policy": {"risk": "", "status": ""},
        "Strict-Transport-Security": {"risk": "", "status": ""},
        "X-Content-Type-Options": {"risk": "", "status": ""},
        "X-Frame-Options": {"risk": "", "status": ""},
        "Referrer-Policy": {"risk": "", "status": ""},
        }
    
    print("now checking the headers")

    for header in security_headers:
        if header in headers:
            security_headers[header]["status"] = "present"
        else:
            security_headers[header]["status"] = "not present"

    # print(security_headers)
    return security_headers