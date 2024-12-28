from database_utils import connect_to_mysql, get_db_schema, execute_sql_query
from model_utils import generate_sql_query

def main():
    # Connect to the MySQL database
    connection = connect_to_mysql()
    if not connection:
        return

    # Fetch and prepare database schema
    schema_info = get_db_schema(connection)
    print("Database Schema:\n", schema_info)

    # Define the text prompt for generating SQL
    text_prompt = "List top 5 products from the product table and join with table inventory_fact_1998 and get warehouse sales"  # Replace with your prompt

    # Generate the SQL query using the model
    sql_query = generate_sql_query(text_prompt, schema_info)
    print("Generated SQL Query:", sql_query)

    # Execute the SQL query if it was generated successfully
    # Since SQL query is generated with triple backticks, i just commented the code.
    # if sql_query:
    #     execute_sql_query(connection, sql_query)

    # Close the MySQL connection
    connection.close()

if __name__ == "__main__":
    main()
