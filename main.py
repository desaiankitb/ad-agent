import asyncio
from agents.agent import root_agent
from typing import Dict, Any
import json

def print_section(title: str, data: Dict[str, Any]) -> None:
    """Pretty print a section of data"""
    print(f"\n=== {title} ===")
    if data.get("success"):
        if data.get("data"):
            print(json.dumps(data["data"], indent=2))
        else:
            print("No data available")
    else:
        print(f"Error: {data.get('error', 'Unknown error')}")

async def test_agent(restaurant_id: str) -> None:
    """Test the agent with a given restaurant ID"""
    print(f"\nAnalyzing restaurant ID: {restaurant_id}")
    print("\nPlease wait while the agent analyzes the data...\n")
    
    # Run the agent
    async for event in root_agent.run_async(restaurant_id):
        if event.response and event.response.text:
            print(event.response.text)

def main():
    """Main function to run the agent locally"""
    print("Welcome to Restaurant Sales Analysis Tool!")
    print("----------------------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Analyze a restaurant")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            restaurant_id = input("\nEnter restaurant ID: ")
            asyncio.run(test_agent(restaurant_id))
        elif choice == "2":
            print("\nThank you for using Restaurant Sales Analysis Tool!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
