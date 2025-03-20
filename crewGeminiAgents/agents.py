from crewai import Agent, LLM
from dotenv import load_dotenv
import os
from tools import tool

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash',
                             verbose=True, 
                             temperature=0.5,
                             google_api_key=os.getenv('GOOGLE_API_KEY'))



llm = LLM(api_key=os.getenv('GOOGLE_API_KEY'),
          temperature=0.7,
          model='gemini/gemini-2.0-flash')

researcher = Agent(
    role = "Senior Researcher",
    goal = "uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=("driven bu curiositym, you're at the forefront"
               "innovation, eager to explore and share knowledge that can change"
               "world"),
               tools= [tool],
               llm=llm,
               allow_delegation=True
)

# creating writer agent with custom tools responsible for writing news blog!
writer = Agent(
    role = "Senior Writer",
    goal = "Narrate compelling stories about {topic}",
    verbose=True,
    memory=True,
    backstory=("with the flair for simplifying complex topics, you craft"
               "engaging narratives that captivate and educate, bringing new"
               "discoveries to light in an accessible manner"),
               tools= [tool],
               llm=llm,
               allow_delegation=True
)