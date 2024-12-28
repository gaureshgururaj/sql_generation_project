import mysql.connector

# MySQL connection details
db_config = {
    'host': 'localhost',       # Change if not on localhost
    'user': 'foodmart',         # Replace with your MySQL username
    'password': 'foodmart@123', # Replace with your MySQL password
    'database': 'FOODMART'      # Replace with your MySQL database name
}

# Connect to MySQL database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Retrieve database schema information
def get_db_schema(connection):
    schema_info = ""
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            schema_info += f"Table: {table_name}\n"
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()
            for column in columns:
                column_name, column_type = column[0], column[1]
                schema_info += f"  - {column_name}: {column_type}\n"
            schema_info += "\n"
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error fetching schema: {e}")
    return schema_info

# Execute the generated SQL query
def execute_sql_query(connection, sql_query):
    try:
        print("Executing SQL Query:", sql_query)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error executing SQL query: {e}")
