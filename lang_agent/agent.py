from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.teacher import teacher_agent
from .sub_agents.conversation import conversation_agent
from .sub_agents.exercise import exercise_agent
from .prompt import LANGUAGE_COORDINATOR_PROMPT

lang_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='lang_agent',
    description='A language coordinator agent.',
    instruction=LANGUAGE_COORDINATOR_PROMPT,
    tools=[
        AgentTool(agent=teacher_agent),
        AgentTool(agent=conversation_agent),
        AgentTool(agent=exercise_agent),
    ],
)


root_agent = lang_agent
