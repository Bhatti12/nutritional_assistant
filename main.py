from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool,  RunContextWrapper
from dotenv import load_dotenv, find_dotenv
import os
from user_profile import UserProfile
import asyncio
from tavily import AsyncTavilyClient

_: bool = load_dotenv(find_dotenv())
gemini_api_key = os.environ.get("GEMINI_API_KEY")
tavili_api_key = os.environ.get("TAVILI_API_KEY")
tavily_client: AsyncTavilyClient = AsyncTavilyClient(api_key=tavili_api_key)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY","")


# Which LLM Service 
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/" 
)

# Which LLM Model 
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model = "gemini-2.5-flash",
    openai_client = external_client
)

@function_tool()
async def search_recipe(local_context: RunContextWrapper[UserProfile], query: str) -> str:
   print("[TOOL CALLING ... ] Search Recipe...")
   response = await tavily_client.search(query, max_results=1)
   return response
    

@function_tool()
async def extract_content(urls: list)-> dict:
    # DATA -> ABOUT USER  or SOMETHING
    print("[TOOL...] Extracting content from URLs:", urls)
    response = await tavily_client.extract(urls)
    #print("[TOOL...] Extracting Completed:", response)
    return response

#Callable Function for dynamic instructions
async def prompt(local_context: RunContextWrapper[UserProfile], agent: Agent[UserProfile]) -> str:
    #print(f"\nUser: {local_context.context},\n Agent: {agent.name}\n")
    return f"""You are deep search agent. Use the tools provided to answer questions." \
    "Always use the search tool first to find the relevant information," \
    "then use the extract tool to get detailed content from the URLs returned by search. " \
    "Be Concise and accurate in your response by using below user details and prefernces.
    User {local_context.context.name} , whose age is {local_context.context.age} and gender  {local_context.context.gender} 
        and weight {local_context.context.weight} and height is {local_context.context.height}. Based on below diet preferences , details:
        {local_context.context.diet_type} , alergies {local_context.context.allergies} and disliked food is {local_context.context.disliked_foods}
        suggest recipe to the user for today. Restrict yourself for one recipe for now. 
        The recipe must tell the user about the nutritional value it gains based on the {local_context.context.country} and {local_context.context.region} 
        daily recomended calorie consumption and inform the user about the calorie gain for consuming this recipe. 
        Restrict your output to 500 words and present the output in nice tabular format alont with recipie.
"""


# Agent Level confiuration for LLM Model
base_agent: Agent = Agent(
    name = "NutritionalExpertAgent",
    instructions = prompt,
    model = llm_model,
    tools=[search_recipe, extract_content ]
)


async def call_nutritional_agent():

    user_context = UserProfile(
    name="Farrukh",
    age=35,
    gender="male",
    weight=75.0,
    height=178.0,
    #activity_level="moderate",
    #goal="weight_loss",
    diet_type="halal",
    allergies=["nuts"],
    disliked_foods=["broccoli"],
    country="Belgium",
    region="Europe"
)

    response = await Runner.run(starting_agent=base_agent, input="You are a deep search nutritional assitant who can provide recipe to the user?",context=user_context)
    print(response.final_output)


if __name__ == "__main__":
    asyncio.run(call_nutritional_agent())
