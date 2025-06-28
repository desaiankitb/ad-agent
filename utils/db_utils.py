import psycopg2
from psycopg2 import Error
from typing import Dict, Any, Optional, Union
from datetime import date, datetime
from decimal import Decimal
from .config import settings

def serialize_value(value: Any) -> Any:
    """
    Serialize values that are not JSON serializable by default
    """
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    elif isinstance(value, Decimal):
        return float(value)
    return value

def execute_query(query: str, params: Optional[tuple] = None) -> Dict[str, Any]:
    """
    Execute a query on the database
    """
    try:
        connection = psycopg2.connect(settings.RDS.db_url)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()

        # Fetch results if any
        try:
            results = cursor.fetchall()
            if cursor.description:  # Check if there are column descriptions
                column_names = [desc[0] for desc in cursor.description]
                # Serialize each value in the row
                serialized_results = []
                for row in results:
                    serialized_row = {}
                    for col_name, value in zip(column_names, row):
                        serialized_row[col_name] = serialize_value(value)
                    serialized_results.append(serialized_row)
                return {"success": True, "data": serialized_results}
            return {"success": True, "data": None}
        except psycopg2.ProgrammingError:
            # No results to fetch (e.g., for INSERT/UPDATE/DELETE)
            return {"success": True, "data": None}

    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if 'connection' in locals():
            connection.close()

def query_peer_benchmarks(locality: str, cuisine: str) -> Dict[str, Any]:
    """
    Query peer benchmarks data for a given locality and cuisine
    """
    query = "SELECT * FROM peer_benchmarks WHERE locality = %s OR cuisine = %s;"
    return execute_query(query, (locality, cuisine))

def query_ads_data(restaurant_id: str) -> Dict[str, Any]:
    """
    Query ads data for a given restaurant ID
    """
    query = "SELECT * FROM ads_data WHERE restaurant_id = %s;"
    return execute_query(query, (restaurant_id,))

def query_restaurant_metrics(restaurant_id: str) -> Dict[str, Any]:
    """
    Query restaurant metrics for a given restaurant ID
    """
    query = "SELECT * FROM restaurant_metrics WHERE restaurant_id = %s;"
    return execute_query(query, (restaurant_id,))

def query_restaurant_name_to_restaurant_id(restaurant_name: str) -> Dict[str, Any]:
    """
    Query restaurant name to restaurant id
    """
    query = "SELECT restaurant_id FROM restaurant_metrics WHERE restaurant_name = %s;"
    return execute_query(query, (restaurant_name,))