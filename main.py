import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    response = client.models.generate_content(model='gemini-2.5-flash', 
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    if response.usage_metadata == None:
        raise RuntimeError("Error accessing usage_metadata property - possible failed API request.")
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

    print(f'Response: {response.text}')

    # if (len(sys.argv) < 2):
    #     print("Usage: uv run main.py <prompt>")
    #     sys.exit(1)
    
    # user_prompt = sys.argv[1]

    # messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    # response = client.models.generate_content(
    #     model='gemini-2.0-flash-001', 
    #     contents=messages,
    # )

    # if '--verbose' in sys.argv:
    #     print(f'User prompt: {user_prompt}')
    #     print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    #     print(f'Response tokens: {response.usage_metadata.candidates_token_count}')


if __name__ == "__main__":
    main()
