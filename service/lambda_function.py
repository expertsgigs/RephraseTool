import json
import os
from groq import Groq

# -----------------------------------
# Groq Client
# -----------------------------------
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# -----------------------------------
# Lambda Handler
# -----------------------------------
def lambda_handler(event, context):

    try:

        # -----------------------------------
        # Parse Request Body
        # -----------------------------------
        body = json.loads(event["body"])

        language = body.get("language", "English")
        tone = body.get("tone", "Formal")
        variants = int(body.get("variants", 1))
        input_text = body.get("text", "")

        # -----------------------------------
        # Prompt
        # -----------------------------------
        prompt = f"""
You are an AI-powered sentence paraphrasing assistant.

Instructions:
- Generate exactly {variants} paraphrased versions.
- Language: {language}
- Tone: {tone}
- Preserve original meaning.
- Make each variation different.
- Return ONLY numbered paraphrases.

Text:
{input_text}
"""

        # -----------------------------------
        # Groq API Call
        # -----------------------------------
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

        output = response.choices[0].message.content

        # -----------------------------------
        # Convert Output Into Array
        # -----------------------------------
        lines = output.split("\n")

        results = []

        for line in lines:

            cleaned = line.strip()

            if cleaned:
                results.append(cleaned)

        # -----------------------------------
        # Response
        # -----------------------------------
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "results": results
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }