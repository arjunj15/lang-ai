from google.adk import Agent

from .prompt import TEACHER_PROMPT
from ...config import get_model_config

# Use model from config
model = get_model_config().get_model()

teacher_agent = Agent(
    model=model,
    name='teacher_agent',
    description='An English teacher agent.',
    instruction=TEACHER_PROMPT,
)
