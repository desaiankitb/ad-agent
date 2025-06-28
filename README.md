# Restaurant Sales Analysis Agent

A powerful AI-powered sales agent that analyzes restaurant performance and provides data-driven recommendations.

## Features

- Restaurant performance analysis
- Ad campaign effectiveness evaluation
- Peer benchmarking
- Data-driven recommendations
- Support for both local testing and ADK web deployment

## Prerequisites

- Python 3.12 or higher
- PostgreSQL database
- Google API key with Gemini access
- UV package manager (required)

## Project Structure

```
ad-agent/
├── agents/
│   ├── __init__.py
│   └── agent.py        # Main agent definition
├── config/
│   ├── config.ini      # Configuration settings
│   └── config.ini.example
├── data/               # CSV data files
│   ├── ads_data.csv
│   ├── peer_benchmarks.csv
│   └── restaurant_metrics.csv
├── utils/
│   ├── __init__.py
│   ├── config.py       # Configuration management
│   ├── db_utils.py     # Database utilities
│   ├── setup_db.py     # Database setup script
│   └── setup_test_data.sql  # Database schema and test data
├── main.py             # Main entry point
└── pyproject.toml      # Project dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ad-agent
   ```

2. Install UV if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create and activate a Python virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   uv pip install -e .
   ```

## Configuration

1. Copy the example config file:
   ```bash
   cp config/config.ini.example config/config.ini
   ```

2. Edit `config/config.ini` with your settings:
   ```ini
   [RDS]
   db_url=postgresql://username:password@localhost:5432/dbname
   ```

## Database Schema

1. Create a PostgreSQL database:
   ```bash
   createdb your_database_name
   ```

2. Set up the database schema and test data:
   ```bash
   python -m utils.setup_db
   ```

## Usage

### Local Testing (Without ADK Web)

1. Run the main script:
   ```bash
   python main.py
   ```

2. Choose option 1 to analyze a restaurant
3. Enter a restaurant ID (e.g., R001, R002, or R003 for test data)
4. View the analysis results

### With ADK Web

1. Install ADK Web:
   ```bash
   uv pip install google-adk-web
   ```

2. Start the ADK Web server:
   ```bash
   adk web
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

4. Enter a restaurant ID in the chat interface to get analysis

## Sample Restaurant IDs for Testing

The test database includes the following sample restaurants:

| ID    | Name         | Location  | Cuisine      |
|-------|-------------|-----------|--------------|
| R001  | Tasty Bites | Delhi     | North Indian |
| R002  | Spice Garden| Mumbai    | South Indian |
| R003  | Dragon House| Bangalore | Chinese      |

## Agent Response Format

The agent provides analysis in four sections:

1. **Restaurant's Recent Performance**
   - Daily orders and revenue
   - Average order value
   - Customer ratings

2. **Ad Campaign Effectiveness**
   - Campaign performance metrics
   - ROI analysis
   - Spend efficiency

3. **Peer Benchmarking**
   - Comparison with similar restaurants
   - Market position analysis
   - Performance gaps

4. **Recommended Next Steps**
   - Data-driven recommendations
   - Actionable insights
   - Improvement opportunities

## Development

### Adding New Features

1. Create new tools in `agents/tools/`
2. Register tools in `agents/agent.py`
3. Update agent instructions as needed
4. Add new database tables in `utils/setup_test_data.sql`

### Running Tests

```bash
pytest
```

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify PostgreSQL is running
   - Check database credentials in config.ini
   - Ensure database exists

2. **API Key Issues**
   - Verify Gemini API key is valid
   - Check Google API key permissions
   - Ensure keys are properly set in config.ini

3. **ADK Web Connection Issues**
   - Check if port 8080 is available
   - Verify ADK Web installation
   - Check browser console for errors

4. **UV Installation Issues**
   - Make sure you have the latest UV version: `uv --version`
   - Try reinstalling UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Check UV is in your PATH

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Running with Docker

### Prerequisites
- Docker
- Docker Compose

### Setup Instructions

1. Create a `.env` file in the project root with your API keys:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

2. Build and start the containers:
   ```bash
   docker compose up --build
   ```

3. The application will start in interactive mode, allowing you to:
   - Analyze restaurant data
   - Access the PostgreSQL database at localhost:5432
   
   Database credentials:
   - Host: localhost
   - Port: 5432
   - Database: adagent
   - Username: adagent
   - Password: adagent

### Project Structure

- `agents/`: Contains the AI agent implementation
- `config/`: Configuration files
- `data/`: CSV data files for analysis
- `utils/`: Utility functions and database setup
- `main.py`: Application entry point

### Configuration

The application uses two main configuration files:
- `config/config.ini`: Main configuration file (created from config.ini.example)
- `.env`: Environment variables for API keys

## Development

To run the project locally without Docker, see the development setup instructions in the original documentation.
