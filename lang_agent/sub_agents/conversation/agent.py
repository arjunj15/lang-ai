from google.adk import Agent

from .prompt import CONVERSATION_PROMPT
from ...config import get_model_config

# Use model from config
model = get_model_config().get_model()


conversation_agent = Agent(
    model=model,
    name='conversation_agent',
    description='An English conversation agent.',
    instruction=CONVERSATION_PROMPT,
)
