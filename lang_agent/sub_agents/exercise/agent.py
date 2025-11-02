from google.adk.agents.llm_agent import Agent

from .prompt import EXERCISE_PROMPT

exercise_agent = Agent(
    model='gemini-2.5-flash',
    name='exercise_agent',
    description='An English exercise agent.',
    instruction=EXERCISE_PROMPT,
)
