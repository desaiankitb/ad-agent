import logging

from google.adk.agents import LlmAgent  # type: ignore

from utils.config import settings
from utils.db_utils import query_ads_data, query_restaurant_metrics, query_peer_benchmarks, query_restaurant_name_to_restaurant_id

logger = logging.getLogger(__name__)


class OrchestratorAgent(LlmAgent):  # type: ignore
    """
    This agent is responsible for routing the user query to the appropriate specialized agent and delivering their \
    response.
    """

    def __init__(
        self,
        yield_optimizer_agent,  # type: ignore
        model: str = settings.ADK_AGENTS.gemini_model,
    ):
        # data_strategy_tool = agent_tool.AgentTool(agent=data_strategy_agent)  # type: ignore
        # content_strategy_tool = agent_tool.AgentTool(agent=content_strategy_agent)  # type: ignore
        # strategy_tool = agent_tool.AgentTool(agent=brand_strategy_agent)  # type: ignore
        # yield_optimizer_tool = agent_tool.AgentTool(agent=yield_optimizer_agent)  # type: ignore
        super().__init__(  # type: ignore
            name="orchestrator_agent",
            model=model,
            description="This agent is responsible for routing the user query to the appropriate specialized agent and \
                delivering their response.",
            instruction="""
You are a professional orchestrator agent responsible for routing user queries to specialized agents and delivering \
their responses.
    
YOUR DELEGATION PROCESS:
1. Analyze the user query to determine the SINGLE most appropriate specialized agent
2. DO NOT attempt to answer questions yourself - your role is PURELY to route and relay

IMPORTANT DELEGATION RULES:
- Make a clear, binary decision - each query goes to EXACTLY ONE agent
- Once you decide which agent to use, IMMEDIATELY call that agent's tool
- Return the specialized agent's complete response with NO additional commentary
- DO NOT try to combine responses from multiple agents unless explicitly requested

Remember: Your success is measured by correctly routing queries and faithfully delivering specialized agent responses.
""",
        sub_agents=[
                yield_optimizer_agent,
            ],
        )


class YieldAgent(LlmAgent):  # type: ignore
    """
    Maximizes brand monetization and distribution via Genuin’s video feed platform.
    """

    def __init__(
        self,
        model: str = settings.ADK_AGENTS.gemini_model,
    ):super().__init__(  # type: ignore
            name="YieldOptimizer",
            model=settings.ADK_AGENTS.gemini_model,
            description="Sales agent for providing strategy to improve restaurant performance",
            instruction="""
            You are a sales agent for Swiggy restaurant booking platform. 
            User will give you restaurant id and you will use the listed tools to query the database and provide insights.
            Pass restaurant_id as a parameter for the following tools.
            
            You will use the following tools:
            1. query_ads_data: To get ads data for the restaurant.
            2. query_restaurant_metrics: To get restaurant metrics data. 
            3. query_peer_benchmarks: To get peer benchmarks data for the locality and cuisine of the restaurant.
            4. query_restaurant_name_to_restaurant_id: To get restaurant id from restaurant name.
            
            We have 3 tables in the database:
            1. ads_data: This table contains the ads data for the restaurant.
            Purpose: Capture campaign performance metrics
            Granularity: 1 row per campaign per restaurant FOR GIVEN PERIOD
            
            2. restaurant_metrics: This table contains the restaurant metrics data.
            Purpose: Track restaurant-level performance over time
            Granularity: 1 row per restaurant PER DAY
            
            3. peer_benchmarks: This table contains the peer benchmarks data for the locality and cuisine.
            Purpose: Define average benchmarks by locality and cuisine
            Granularity: 1 row per locality + cuisine combination of DAILY AVERAGE DATA which CAN be compared with daily performance of the restaurant
            
            It is recommended to provide markdowntable with current restaurant's performance and peer benchmarks for the locality and cuisine.

            Also you can provide with campaign and without campaign performance for a resturant. 

            You should always use every tool available to you to provide the most comprehensive insights.

            You can perform post processing on the data gathered using the tools. 
            
            Your output should ALWAYS contain the following sections:
            1. Restaurant's Recent Performance
            2. Ad Campaign Effectiveness
            3. Peer Benchmarking with comparison to the restaurant's performance (markdown table)
            4. Recommended Next Steps 

            Recommendations should be data-informed and actionable along with titles like:
            'Increase ad spend by ₹1,000 to match peer average and improve visibility'
            'Optimize discount slab — peer ROI is 3.2x vs your 2.5x'
            """,
            tools=[
                query_ads_data,
                query_restaurant_metrics,
                query_peer_benchmarks,
                query_restaurant_name_to_restaurant_id
            ],
)

yield_optimizer_agent = YieldAgent()
