import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"

def generate_content(topic, tone, target_audience, brand_name):
    prompt = f"""You are a professional content writer for {brand_name}.

Topic: {topic}
Tone: {tone}
Target Audience: {target_audience}

Respond ONLY with valid JSON, no explanation, no markdown:
{{
  "twitter": {{
    "variant_1": "tweet max 280 chars, direct hook",
    "variant_2": "tweet max 280 chars, question hook",
    "variant_3": "tweet max 280 chars, statistic or bold claim"
  }},
  "linkedin": "professional LinkedIn post 800-1200 characters with line breaks and emojis",
  "email": {{
    "subject": "email subject line max 60 chars",
    "preview": "preview text max 90 chars"
  }},
  "blog_titles": [
    "Blog title idea 1",
    "Blog title idea 2",
    "Blog title idea 3",
    "Blog title idea 4",
    "Blog title idea 5"
  ]
}}"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.7, "num_predict": 900}
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
        raw = response.json()["response"].strip()

        if "```" in raw:
            raw = raw.split("```")[1].replace("json", "").strip()

        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start != -1 and end > start:
            raw = raw[start:end]

        return json.loads(raw)

    except json.JSONDecodeError:
        return get_fallback(topic, "JSON parse error")
    except Exception as e:
        return get_fallback(topic, str(e))

def get_fallback(topic, error="Unknown error"):
    return {
        "twitter": {
            "variant_1": f"[Failed: {topic[:50]}]",
            "variant_2": f"[Error: {error[:50]}]",
            "variant_3": "[Please retry]"
        },
        "linkedin": f"[Generation failed for: {topic}]",
        "email": {
            "subject": f"[Failed: {topic[:40]}]",
            "preview": "[Generation failed]"
        },
        "blog_titles": [
            f"[Failed: {topic}]",
            "[Retry]", "[Retry]", "[Retry]", "[Retry]"
        ]
    }