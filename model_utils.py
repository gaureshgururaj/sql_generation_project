import os
from groq import Groq

# Initialize the Groq client with API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Fetch API key from environment variable

# Generate SQL query from text prompt using a model
def generate_sql_query(text_prompt, schema_info, model_name="llama3-70b-8192"):
    try:
        # Construct the prompt with schema information and the query request
        prompt = (
            f"You have access to the following database schema:\n{schema_info}\n\n"
            f"Generate a MySQL-compatible SQL query for the following request:\n"
            f"{text_prompt}\nMake sure the syntax is correct for MySQL."
        )
        
        # Send the request to the model
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that converts text into SQL queries."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        # Extract the SQL query from the response
        if response and response.choices:
            sql_query = response.choices[0].message.content.strip()
            return sql_query
        else:
            print("No SQL query generated or unexpected response structure.")
            return None

    except Exception as e:
        print(f"Error generating SQL: {e}")
        return None
