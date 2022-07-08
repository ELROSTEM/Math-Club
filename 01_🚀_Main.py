from datetime import date

import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth


st.set_page_config(
     page_title="ELRO Gameboard",
     page_icon="🎲",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "# Weekly games. Answer questions and compete against other grades"
     }
)

# Constants
todays_date = date.today()
isocalendar = date(todays_date.year, todays_date.month, todays_date.day).isocalendar()
weekday = isocalendar[2]
WEEK = str(isocalendar[1])

# Problem
### IMPORTANT ###
# EVERY TIME YOU UPDATE DOWNLOAD USER CSV OR ELSE IT WILL RESET LEADERBOARD T-T
QUESTION = "When was ERHS Created?"
IMAGE = "https://www.nyclgbtsites.org/wp-content/uploads/2021/06/17.-Eleanor-Roosevelt-High-School.-Photo-NY-Daily-News-2019.jpg"
CORRECT_ANSWER = 2002 # DID YOU REPLACE USERS.CSV??



users = pd.read_csv("database/users.csv")

# Authentication
names = users["name"].tolist()
usernames = users["username"].tolist()
passwords = users["password"].tolist()
hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login','main')

# Logged In
if authentication_status:

    # Welcome
    st.subheader(f'Welcome {name}, today is {todays_date} on week {WEEK}.')
    authenticator.logout("Logout")
    if WEEK not in users.columns:
        users[WEEK] = 0
 
    # Problem
    st.image(IMAGE)
    st.subheader(QUESTION)

    form = st.empty()
    with form.container():
        # Form
        with st.form(key='answer_form'):

            st.header("Answer")
            answer = st.number_input("What is your answer?")
            # Submit button
            submit_button = st.form_submit_button(label='Submit')

    if submit_button is True:
        # Get current user index
        if answer == CORRECT_ANSWER:
            form.empty()
            users.loc[users["username"] == username, WEEK] = int(100/weekday)
            users.to_csv('database/users.csv', index=False)
            st.success(f"Submission day {todays_date}. Hope you have a great day! 😊")
            st.balloons()
        else:
            st.warning(f"Sorry {name} you are incorrect. Please try again.")
    


    # Admin
    if username == "BoppityBop":
        users.loc[users["grade"] == "Junior", "grade"] = "Senior"
        users.loc[users["grade"] == "Sophomore", "grade"] = "Junior"
        users.loc[users["grade"] == "Freshman", "grade"] = "Sophmore"
        users_csv = users.to_csv().encode('utf-8')
        st.download_button(
        label="Download users.csv",
        data=users_csv,
        file_name='users.csv',
        mime='text/csv',
        )


# Incorrect Password
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
    url = "https://forms.gle/cHbVEdbC1yLwo9xE7"
    st.write("Sign Up Here [link](%s)" % url)
