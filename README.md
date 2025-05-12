
# FastAPI + Supabase Integration

This project demonstrates how to integrate FastAPI with Supabase, an open-source Firebase alternative, to create a simple API service. The demo uses a Supabase database and Python client (`supabase-py`) to interact with the database.

## Features
- **FastAPI** as the web framework for the backend.
- **Supabase** as the database provider.
- Fetch data from Supabase tables and display it through FastAPI endpoints.
- Error handling and validation integrated into API calls.
- Built-in ability to handle user requests and fetch data from Supabase with proper authentication.

## Setup Instructions

### 1. Start a New Supabase Project
- Go to [Supabase](https://app.supabase.io) and sign up or log in.
- Create a new project, and Supabase will provide you with a **SUPABASE_URL** and **SUPABASE_KEY**. You will need these to interact with your Supabase instance.

### 2. Create the Database Schema
- In the Supabase dashboard, navigate to the **SQL Editor**.
- Run the provided `countries` schema or any other schema relevant to your project. This will create necessary tables in your Supabase database.
  ```sql
  -- Example schema to create countries table
  CREATE TABLE countries (
      id SERIAL PRIMARY KEY,
      name TEXT NOT NULL,
      code VARCHAR(3) UNIQUE NOT NULL
  );

3. Set Up Environment Variables

Create a .env file or update your environment variables with the following:

SUPABASE_URL=<your_supabase_url>
SUPABASE_KEY=<your_supabase_key>

Replace <your_supabase_url> and <your_supabase_key> with the credentials you received from Supabase.

4. Install Dependencies

Make sure you have Python 3.8+ and pip installed. Then, install the required dependencies:

pip install fastapi uvicorn httpx supabase-py

5. Run the Application

Now, you can run the FastAPI app using the uvicorn server:

uvicorn main:app --reload

This will start the server at http://localhost:8000.

6. Test the Endpoints
   •   Root Endpoint: GET /
      •   Returns a simple “Hello World” message.
   •   Fetch Data Endpoint: GET /fetch/{url:path}
      •   Fetches JSON data from the provided external URL (e.g., https://jsonplaceholder.typicode.com/todos/1).

Example API Calls:
   •   Fetch data from an external API:

curl http://localhost:8000/fetch/jsonplaceholder.typicode.com/todos/1

This will retrieve a sample todo item from the JSONPlaceholder API.

7. Explore Supabase Data
   •   You can interact with your Supabase database directly using the Supabase Python client (supabase-py), allowing you to fetch and manipulate data programmatically:

from supabase import create_client, Client

url: str = "<your_supabase_url>"
key: str = "<your_supabase_key>"
supabase: Client = create_client(url, key)

data = supabase.table("countries").select("*").execute()
print(data)



Further Documentation
   •   Supabase Docs: Supabase Client Libraries
   •   Supabase Python Client: supabase-py GitHub

License

This project is licensed under the MIT License - see the LICENSE file for details.

### Key Adjustments:
- **Supabase Integration**: Clear steps to integrate Supabase into the project, from setting up a new project to interacting with Supabase using `supabase-py`.
- **FastAPI Endpoints**: Detailed instructions for running the FastAPI app and testing the fetch endpoint, which retrieves data from a URL.
- **Environment Setup**: Clear steps on configuring Supabase credentials and environment variables.
- **External Data Fetching**: Example of how to fetch external data via the `/fetch/{url:path}` endpoint.
  
