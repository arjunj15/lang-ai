from google.adk import Agent

from .prompt import CONVERSATION_PROMPT

conversation_agent = Agent(
    model='gemini-2.5-flash',
    name='conversation_agent',
    description='An English conversation agent.',
    instruction=CONVERSATION_PROMPT,
)
