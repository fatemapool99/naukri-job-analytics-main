import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

user="postgres"
password="postgres"
database="naukri_jobs"
port=52033

engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@localhost:{port}/{database}"
)

df = pd.read_sql("SELECT * FROM clean_jobs", engine)

print("Total jobs:", len(df))
print("\nTop locations:")
print(df["location"].value_counts().head(10))

print("\nTop companies:")
print(df["company"].value_counts().head(10))

print("\nMissing values:")
print(df.isnull().sum())

# Save a chart of the top 10 locations
top_locations = df["location"].value_counts().head(10)

if not top_locations.empty:
    top_locations.sort_values().plot(kind="barh")
    plt.title("Top 10 Job Locations")
    plt.xlabel("Number of Listings")
    plt.tight_layout()
    plt.savefig("top_locations.png")
    plt.show()

engine.dispose()