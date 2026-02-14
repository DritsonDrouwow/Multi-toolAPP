import config
from openai import OpenAI

GROQ_URL = "https://api.groq.com/openai/v1"

MODELS = getattr(config, "GROQ_MODELS", ["llama-3.1-8b-instant", "mixtral-8x7b-32768"])

def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = getattr(config, "GROQ_API_KEY", None)
    if not key:
        return "Error: GROQ_API_key not found in config.py"
        
    c = OpenAI(api_key=key, api_base=GROQ_URL)

    last_err = None
    for m in MODELS:
        try:
            response = c.chat.completions.create(
                model=m,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            last_err = str(e)
    return (
        "Groq model failed. \n"
        f"Tried models: {MODELS}\n"
        "Fix:\n"
        "1) Swtich to hf by importing hf.py in main.py OR\n"
        "2) Replace Groq model in groq.py (GROQ_MODELS).\n"
        f"Details: {type(last_err).__name__}: {last_err}"
    )



    