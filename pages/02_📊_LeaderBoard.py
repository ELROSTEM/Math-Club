import pandas as pd
import streamlit as st


# Page Configuration
st.set_page_config(
     page_title="Weekly Math",
     page_icon="🤓",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "# Weekly Math. Do math problems and compete against other grades"
     }
)

# Load data
leaderboard = pd.read_csv("database/users.csv")

columns = list(leaderboard.columns)
leaderboard["Score"] = leaderboard[columns[4:]].sum(axis=1)
leaderboard = leaderboard[["username", "grade", "Score"]]

st.dataframe(leaderboard)
