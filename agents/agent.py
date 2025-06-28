from utils.config import settings
import os

from .sub_agents import OrchestratorAgent, YieldAgent

os.environ["GOOGLE_API_KEY"] = settings.ADK_AGENTS.google_api_key

yield_optimizer_agent = YieldAgent()

root_agent = OrchestratorAgent(
    yield_optimizer_agent=yield_optimizer_agent,
)
