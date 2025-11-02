from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.teacher import teacher_agent
from .sub_agents.conversation import conversation_agent
from .sub_agents.exercise import exercise_agent
from .prompt import LANGUAGE_COORDINATOR_PROMPT

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A language coordinator agent.',
    instruction=LANGUAGE_COORDINATOR_PROMPT,
    tools=[
        AgentTool(agent=teacher_agent),
        AgentTool(agent=conversation_agent),
        AgentTool(agent=exercise_agent),
    ],
)
