import psycopg2
from pathlib import Path
from .config import settings

def setup_test_database():
    """Set up test database with sample data"""
    try:
        # Connect to the database
        connection = psycopg2.connect(settings.RDS.db_url)
        cursor = connection.cursor()
        
        # Read and execute the SQL script
        sql_file = Path(__file__).parent / 'setup_test_data.sql'
        with open(sql_file, 'r') as f:
            sql_script = f.read()
            
        cursor.execute(sql_script)
        connection.commit()
        print("Test database setup completed successfully!")
        
    except Exception as e:
        print(f"Error setting up test database: {str(e)}")
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    setup_test_database() 