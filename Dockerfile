FROM python:3.12-slim 

WORKDIR /app

# Install uv for dependency management
RUN pip install uv

# Copy only the package files first for better layer caching
COPY pyproject.toml uv.lock ./

# Create a src directory for the package
COPY agents/ ./agents/
COPY utils/ ./utils/
COPY main.py ./
COPY config/config.ini ./config/config.ini
COPY README.md ./

# Install project dependencies
RUN uv pip install --system -e .

CMD ["adk", "web", "--host", "0.0.0.0"]