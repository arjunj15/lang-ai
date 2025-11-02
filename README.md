# Voice Bot

A language learning assistant built with Google Agent Development Kit (ADK) for Python, featuring a multi-agent system with specialized sub-agents for teaching, conversation, and exercises.

## Prerequisites

- Python 3.12 or later
- Poetry (for dependency management)
- Google Gemini API key ([Get one here](https://aistudio.google.com/apikey))

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd Voice-Bot
   ```

2. **Install Poetry** (if not already installed):
   ```bash
   # Windows PowerShell
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   
   # macOS/Linux
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies** using Poetry:
   ```bash
   poetry install
   ```

4. **Activate the Poetry virtual environment**:
   ```bash
   poetry shell
   ```

   Or use Poetry's run command to execute commands within the virtual environment:
   ```bash
   poetry run <command>
   ```

## Setup

### Configure API Key

Create a `.env` file in the project root directory and add your Google Gemini API key:

```bash
# Windows PowerShell
echo 'GOOGLE_API_KEY="YOUR_API_KEY_HERE"' > .env

# Windows CMD
echo GOOGLE_API_KEY="YOUR_API_KEY_HERE" > .env

# macOS/Linux
echo 'GOOGLE_API_KEY="YOUR_API_KEY_HERE"' > .env
```

**Note:** Replace `YOUR_API_KEY_HERE` with your actual Google Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

## Running the Agent

You can run the Voice Bot agent in two ways:

### Option 1: Command-Line Interface

Run the agent using the ADK CLI with the `lang_agent` directory:

```bash
poetry run adk run lang_agent
```

### Option 2: Web Interface

Start the ADK web interface for an interactive chat experience:

```bash
poetry run adk web --port 8000
```

Then open your browser and navigate to [http://localhost:8000](http://localhost:8000). Select the agent in the upper right corner and start chatting!

**Note:** Make sure to run the `adk web` command from the project root directory (the parent directory containing the `lang_agent/` folder).

## Project Structure

```
Voice-Bot/
├── lang_agent/           # Main agent package
│   ├── agent.py         # Root agent configuration
│   ├── prompt.py        # Main agent prompts
│   └── sub_agents/      # Specialized sub-agents
│       ├── teacher/     # Teaching agent
│       ├── conversation/# Conversation agent
│       └── exercise/    # Exercise agent
├── pyproject.toml       # Poetry configuration
└── README.md           # This file
```

## Features

- **Multi-agent System**: Coordinated agents for different language learning tasks
- **Teacher Agent**: Provides language instruction and explanations
- **Conversation Agent**: Handles natural language conversations
- **Exercise Agent**: Creates and manages language exercises

## Documentation

For more information about Google ADK, visit the [official documentation](https://google.github.io/adk-docs/get-started/python/#run-your-agent).
