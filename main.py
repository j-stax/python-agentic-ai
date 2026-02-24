import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
model_name= "gemini-2.5-flash"
client = genai.Client(api_key=api_key)

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    user_prompt = args.user_prompt

    response = client.models.generate_content(
        model=model_name, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        ),
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if response.usage_metadata == None:
        raise RuntimeError("Error accessing usage_metadata property - possible failed API request.")
    
    if args.verbose:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {prompt_tokens}')
        print(f'Response tokens: {response_tokens}')
    
    if not response.function_calls:
        print(f'Response:\n {response.text}')
        return

    function_results = []
    for function_call in response.function_calls:
        # print(f'Calling function: {function_call.name}({function_call.args})')
        function_call_result = call_function(function_call)
        if (
            not function_call_result.parts 
            or not function_call_result.parts[0].function_response
            or not function_call_result.parts[0].function_response.response
        ):
            raise RuntimeError(f'Error: Empty function response for {function_call.name}')
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_results.append(function_call_result.parts[0])

   
if __name__ == "__main__":
    main()
