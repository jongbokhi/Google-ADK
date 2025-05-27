from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.stock_analyst import stock_analyst
from .sub_agents.news_analyst import news_analyst
from .tools.tools import get_current_time

from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name="supervisor",
    model = "gemini-2.0-flash",
    description="Supervisor Agent",
    instruction="""
    You are a supervisor agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    sub_agents=[stock_analyst],
    tools=[
        AgentTool(news_analyst), 
        get_current_time
        ],
    
)