# Restaurant Sales Analysis Agent

A powerful AI-powered Yield Optimiser Agent that analyzes restaurant performance and provides data-driven recommendations.

## Features

- Restaurant performance analysis
- Ad campaign effectiveness evaluation
- Peer benchmarking
- Data-driven recommendations
- Support Google ADK based web for testing

## Prerequisites

- Google API key with Gemini access
- git 
- Python 3.12 or higher
- Docker (for containerized deployment)

## Project Structure

```
ad-agent/
├── agents/
│   ├── __init__.py
│   ├── agent.py          # Main agent implementation
│   └── sub_agents.py     # Specialized agent implementations
├── config/
│   ├── config.ini        # Configuration settings (gitignored)
│   └── config.ini.example
├── utils/
│   ├── __init__.py
│   ├── config.py         # Configuration management
│   ├── db_utils.py       # Database utilities
│   ├── setup_db.py       # Database setup script
│   └── setup_test_data.sql  # Database schema and test data
├── docker-compose.yml    # Docker compose configuration
├── Dockerfile           # Docker build configuration
├── pyproject.toml       # Project dependencies
├── README.md            # Project documentation
└── uv.lock              # Dependency lock file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/desaiankitb/ad-agent.git
   cd ad-agent
   ```

2. Install dependencies using uv:
   ```bash
   pip install uv
   uv pip install -e .
   ```

## Configuration

1. Copy the example config file:
   ```bash
   cp config/config.ini.example config/config.ini
   ```

2. Edit `config/config.ini` with your settings:
   ```ini
   [ADK_AGENTS]
   gemini_api_key=<your-key-here>
   google_api_key=<your-key-here>
   [RDS]
   db_url=postgresql://username:password@localhost:5432/dbname
   ```

## Running with Docker

### Prerequisites
- Docker
- Docker Compose

### Setup Instructions

1. Create a `config/config.ini` file with your API keys:
   ```ini
   [ADK_AGENTS]
   gemini_api_key=<your-key-here>
   google_api_key=<your-key-here>
   [RDS]
   db_url=postgresql://username:password@db:5432/ad-agent
   ```

2. Build and start the containers:
   ```bash
   docker compose up --build
   ```

The agent will be available via ADK web interface at `http://localhost:8000`.

### Project Structure

- `agents/`: Contains the AI agent implementation
- `config/`: Configuration files
- `data/`: CSV data files for analysis
- `utils/`: Utility functions and database setup
- `main.py`: Application entry point

### Configuration

The application uses two main configuration files:
- `config/config.ini`: Main configuration file (created from config.ini.example)
