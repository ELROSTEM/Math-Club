import streamlit as st

st.title("Rules 📜")

st.subheader("📌 RULE 1: NO SHARING ANSWERS AMONGST GRADE")
st.subheader("📌 RULE 2: NO BAD STUFF")

st.header("\nAbout")
st.write("""
WELCOME to the ELRO game board! Here you will compete against the other grades to win the coveted ELRO Cup.
Only the best grade shall win. A questions will be posted every Sunday that relates to ELRO. 
For example, "How old is Mr. Lin?" hmm. IDK! You will have the whole week to find out. However, for each day
""")

col1, col2 = st.columns([3, 1])
col1.markdown("![Alt Text](https://media.giphy.com/media/un15GSgV1JHby/giphy.gif)")

col2.write("""it takes you to find the answer your score will be deducted. Just think of this as Hogwarts 🧙‍♂️.
The moderators will deduct points from your grade if deemed necessary.
""")

