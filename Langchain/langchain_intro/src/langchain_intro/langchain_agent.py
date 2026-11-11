# pip install -qU langchain "langchain[openai]"

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# Initialize Groq model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
# Create agent
agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)
# agent = create_agent(
#     model="openai:gpt-5.5",
#     tools=[get_weather],
#     system_prompt="You are a helpful assistant",
# )

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)


[
    {'type': 'reasoning', 'reasoning': 'We need to respond with the weather info. The function returned a joke. Probably we should correct. The user asked "What\'s the weather in San Francisco?" The function gave a joke. We should respond with actual weather. But we only have that response. We could say "According to the latest data, it\'s..." but we don\'t have real data. We could apologize and say it\'s always sunny? But that\'s not accurate. Maybe we can say "I’m sorry, I don’t have real-time data." But we have a function that gave a joke. We could ask to try again. Probably respond politely: "I’m sorry, I don’t have real-time weather data."'}, 
    {'type': 'text', 'text': 'I’m sorry—I don’t have real‑time weather data available at the moment. You can check a reliable weather service or app for the current conditions in San\u202fFrancisco.'}
]