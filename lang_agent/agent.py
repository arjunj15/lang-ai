from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.teacher import teacher_agent
from .sub_agents.conversation import conversation_agent
from .sub_agents.exercise import exercise_agent
from .prompt import LANGUAGE_COORDINATOR_PROMPT
from .config import get_model_config

# Use model from config
model = get_model_config().get_model()

lang_agent = LlmAgent(
    model=model,
    name='lang_agent',
    description='A language coordinator agent.',
    instruction=LANGUAGE_COORDINATOR_PROMPT,
    sub_agents=[
        teacher_agent,
        conversation_agent,
        exercise_agent,
    ],
    # tools=[
    #     AgentTool(agent=teacher_agent),
    #     AgentTool(agent=conversation_agent),
    #     AgentTool(agent=exercise_agent),
    # ],
)


root_agent = lang_agent
