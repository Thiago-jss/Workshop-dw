import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv



# Load environment variables from the .env file
load_dotenv()

# Get variables from the .env file
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Create the database connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the database connection engine
engine = create_engine(DATABASE_URL)

# Query data from the dm_commodity table
def get_data():
    query = f"""
    SELECT
        data,
        symbol,
        closing_value,
        action,
        quantity,
        value,
        earning
    FROM
        public.dm_commodity;
    """
    try:
        df = pd.read_sql(query, engine)
        return df
    except ProgrammingError as e:
        st.error(f"Error accessing table 'dm_commodity' in schema '{DB_SCHEMA}': {e}")
        return pd.DataFrame()  # Returns an empty DataFrame in case of error

# Configure the Streamlit page
st.set_page_config(page_title='Commodities Dashboard', layout='wide')

# Dashboard Title
st.title('Commodities Dashboard')

# Description
st.write("""
This dashboard shows commodity data and transactions.
""")

# Get the data
df = get_data()

# Check if the DataFrame is empty
if df.empty:
    st.write("Unable to load data. Check if the 'dm_commodity' table exists in the specified schema.")
else:
    # Display the data
    st.write("### Commodity Data")
    st.dataframe(df)

    # Statistical summary
    st.write("### Statistical Summary")
    st.write(df.describe())

    # Graphs
    st.write("### Graphs")

    # Bar chart for earnings
    st.bar_chart(df[['data', 'earning']].set_index('data'))

    # Line chart for closing values
    st.line_chart(df[['data', 'closing_value']].set_index('data'))
