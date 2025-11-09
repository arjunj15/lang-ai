from google.adk import Agent

from .prompt import EXERCISE_PROMPT
from ...config import get_model_config

# Use model from config
model = get_model_config().get_model()

exercise_agent = Agent(
    model=model,
    name='exercise_agent',
    description='An English exercise agent.',
    instruction=EXERCISE_PROMPT,
)
