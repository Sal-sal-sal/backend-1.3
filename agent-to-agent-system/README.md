# Agent to Agent System

This project implements an Agent to Agent system using OpenAI and Google services. It leverages FastAPI for the web framework, Pydantic for data validation, and includes various agents that interact with external APIs.

## Project Structure

```
agent-to-agent-system
├── src
│   ├── main.py               # Entry point of the application
│   ├── agents                # Contains agent implementations
│   │   ├── openai_agent.py   # OpenAI agent for interacting with OpenAI API
│   │   ├── google_agent.py    # Google agent for interacting with Google services
│   │   └── __init__.py
│   ├── api                   # Contains API route definitions
│   │   ├── routes.py         # API routes for agent interactions
│   │   └── __init__.py
│   ├── models                # Contains data models and schemas
│   │   ├── schemas.py        # Pydantic models for request/response validation
│   │   ├── dataclasses.py     # Data classes for managing data structures
│   │   └── __init__.py
│   ├── services              # Contains service integrations
│   │   ├── ai_crew.py        # Functions for AI Crew services
│   │   ├── google_avk.py     # Functions for Google AVK services
│   │   └── __init__.py
│   └── utils                 # Utility functions
│       └── __init__.py
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd agent-to-agent-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

Once the application is running, you can interact with the API endpoints defined in `src/api/routes.py`. The agents can be used to send requests to OpenAI and Google services, and the responses will be validated using the Pydantic models defined in `src/models/schemas.py`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to add.
s