from google.adk import Agent

from .prompt import TEACHER_PROMPT

teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='teacher_agent',
    description='An English teacher agent.',
    instruction=TEACHER_PROMPT,
)
