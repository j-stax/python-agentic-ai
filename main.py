import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    user_prompt = args.user_prompt

    response = client.models.generate_content(model='gemini-2.5-flash', contents=messages)
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if response.usage_metadata == None:
        raise RuntimeError("Error accessing usage_metadata property - possible failed API request.")
    
    if args.verbose:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {prompt_tokens}')
        print(f'Response tokens: {response_tokens}')
    else:
        print(f'Response: {response.text}')

    # if (len(sys.argv) < 2):
    #     print("Usage: uv run main.py <prompt>")
    #     sys.exit(1)
    
    # user_prompt = sys.argv[1]

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
