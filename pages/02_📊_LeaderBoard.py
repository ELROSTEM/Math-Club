import pandas as pd
import streamlit as st

import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
     page_title="ELRO Gameboard",
     page_icon="🎲",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "# Weekly games. Answer questions and compete against other grades"
     }
)

# Load data
leaderboard = pd.read_csv("database/users.csv")

# Parse the dataframe
columns = list(leaderboard.columns)
leaderboard["score"] = leaderboard[columns[4:]].sum(axis=1)
leaderboard = leaderboard[["username", "grade", "score"]].sort_values(by=['score'], ascending=False).reset_index(drop=True)

# New dataframe by grades
freshman_leaderboard = leaderboard[leaderboard["grade"] == "Freshman"]
sophomore_leaderboard = leaderboard[leaderboard["grade"] == "Sophomore"]
junior_leaderboard = leaderboard[leaderboard["grade"] == "Junior"]
senior_leaderboard = leaderboard[leaderboard["grade"] == "Senior"]

# Grade Ranking
freshman_total = freshman_leaderboard["score"].sum()
sophomore_total = sophomore_leaderboard["score"].sum()
junior_total = junior_leaderboard["score"].sum()
senior_total = senior_leaderboard["score"].sum()

# Tallied data
data = [freshman_total, sophomore_total, junior_total, senior_total]

# Bar chart
colors = ['lightslategray',] * 5
colors[data.index(max(data))] = 'crimson' # Color highest red
fig = go.Figure(data=[go.Bar(
    x=['Freshman', 'Sophmore', 'Junior', 'Senior'],
    y= data,
    marker_color=colors # marker color can be a single color value or an iterable
)])
st.plotly_chart(fig, use_container_width=True)













st.table(leaderboard)
