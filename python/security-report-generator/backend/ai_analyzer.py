import json
import os

import requests
from dotenv import load_dotenv


load_dotenv("../../../.env")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY was not found in the .env file")


def analyzer(header_analysis):
    print("now analyzing the header analysis with AI")

    payload = {
        "model": "nvidia/nemotron-3.5-lightning:free",
        "messages": [
            {
                "role": "user",
                "content": (
                    "Here are the results from a defensive security scanner:\n\n"
                    f"{header_analysis}\n\n"
                    "Please analyze the headerAnalysis that has been performed "
                    "and provide a summary of the security findings, key points, "
                    "and recommendations for improvements.\n\n"
                    "Return the result as a JSON object with this structure:\n"
                    "{\n"
                    '    "overall_summary": "",\n'
                    '    "findings": [\n'
                    "        {\n"
                    '            "name": "...",\n'
                    '            "severity": "...",\n'
                    '            "explanation": "...",\n'
                    '            "remediation": "..."\n'
                    "        }\n"
                    "    ]\n"
                    "}"
                ),
            }
        ],
        "response_format": {
            "type": "json_object"
        },
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        answer = data["choices"][0]["message"]["content"]

        try:
            result = json.loads(answer)
            return result

        except json.JSONDecodeError:
            print("Model did not return valid JSON:")
            print(answer)
            return None

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

    except (KeyError, TypeError) as e:
        print(f"Unexpected API response: {e}")
        return None
