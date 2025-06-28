FROM python:3.12-slim 

WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     && rm -rf /var/lib/apt/lists/*

# # Clear cache and update
# # RUN apt-get clean && \
#     # rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
#     # apt-get update

# Install packages with retry logic
# RUN apt-get update && apt-get install -y \
#     --no-install-recommends \
#     --fix-missing \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# Install uv for dependency management
RUN pip install uv

# Copy only the package files first for better layer caching
COPY pyproject.toml uv.lock ./

# Create a src directory for the package
# RUN mkdir src
COPY agents/ ./agents/
COPY utils/ ./utils/
COPY main.py ./
COPY config/config.ini ./config/config.ini
COPY README.md ./

# Install project dependencies
RUN uv pip install --system -e .

CMD ["adk", "web", "--host", "0.0.0.0"]