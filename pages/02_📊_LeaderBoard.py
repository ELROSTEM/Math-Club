import pandas as pd
import streamlit as st

import plotly.graph_objects as go

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
leaderboard["score"] = leaderboard[columns[4:]].sum(axis=1)
leaderboard = leaderboard[["username", "grade", "score"]]

data = [20, 14, 23, 25]

colors = ['lightslategray',] * 5
colors[data.index(max(data))] = 'crimson'

fig = go.Figure(data=[go.Bar(
    x=['Freshman', 'Sophmore', 'Junior', 'Senior'],
    y= data,
    marker_color=colors # marker color can be a single color value or an iterable
)])
fig.update_layout(title_text='Winning')

st.plotly_chart(fig, use_container_width=True)











st.table(leaderboard)
