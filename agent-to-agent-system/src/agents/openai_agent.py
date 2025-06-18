import os
from dotenv import load_dotenv
from openai import OpenAI
from src.agents.google_agent import GoogleSearchAgent
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
api_key_google = os.getenv("GOOGLE_API_SEARCH")
if not api_key:
    raise ValueError("OPENAI_API_KEY не установлен в переменных окружения")

if not api_key_google:
    raise ValueError("GOOGLE_API_SEARCH не установлен в переменных окружения")


# search_agent = GoogleSearchAgent(api_key=api_key_google, cx_id="00d92e72f2da44f8b")
# search_results = search_agent.search("что такое GPT-4o")

def Google_search_results( query: str = "что такое GPT-4o"):
    search_agent = GoogleSearchAgent(api_key=api_key_google, cx_id="00d92e72f2da44f8b")
    search_results = search_agent.search(query)
    return search_results

def search_google(query: str) -> str:
    results = Google_search_results(query)
    formatted = "\n".join([f"{i+1}. {item['title']} - {item['link']}" for i, item in enumerate(results)])
    return formatted




from openai import OpenAI

client = OpenAI(api_key=api_key)

functions = [
    {
        "name": "search_google",
        "description": "Поиск в Google, если модель не знает ответа.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Что искать"},
            },
            "required": ["query"],
        },
    }
]

def run_agent_with_search(user_query: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_query}],
        functions=functions,
        function_call="auto"
    )

    message = response.choices[0].message

    if message.function_call:
        func_name = message.function_call.name
        args = json.loads(message.function_call.arguments)

        if func_name == "search_google":
            result = search_google(args["query"])

            # второй запрос: вставляем результат поиска обратно в диалог
            follow_up = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": user_query},
                    message,  # функция, которую GPT захотел вызвать
                    {"role": "function", "name": func_name, "content": result}
                ]
            )
            return follow_up.choices[0].message.content
    else:
        return message.content
 

