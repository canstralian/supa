import os
from supabase import create_client, Client

# create a Supabase client to connect to your db
url: str = "https://ernhobnpmmupjnmxpfbt.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVybmhvYm5wbW11cGpubXhwZmJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NDYyODQwMDgsImV4cCI6MTk2MTg2MDAwOH0.UQsOkUsIn9hTjYJuSldMikKSXeUxanVTgP04XrPp05M"
supabase: Client = create_client(url, key)

# query the database for all countries in Asia
response = supabase.table("countries").select("name").eq('continent', 'Asia').order('name').execute()

# print country names
for country in response.data:
  print(country['name'])