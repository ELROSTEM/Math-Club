from datetime import datetime

import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

# Authentication
names = ['John Smith','Rebecca Briggs']
usernames = ['jsmith','rbriggs']
passwords = ['123','456']
hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)
name, authentication_status = authenticator.login('Login','main')


# Logged In
if authentication_status:
    st.write('Welcome *%s*' % (name))

    # Sidebar nav
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Leader Board'], 
            icons=['house', 'list-ol'], menu_icon="cast", default_index=0)
        selected
    
    if selected == "Home":
        # Home Page
        st.title("Problem")

        # Problem
        problem = r'./problem/problem_1.png'
        correct_answer = 45
        st.image(problem)

        form = st.empty()
        with form.container():
            # Form
            with st.form(key='answer_form'):

                st.header("Answer")
                answer = st.number_input("What is your answer?")
                # Submit button
                submit_button = st.form_submit_button(label='Submit')

        if submit_button == True:

            if answer == correct_answer:
                form.empty()

                date = datetime.now().strftime("%d/%m/%Y")
                time = datetime.now().strftime("%H:%M:%S")

                # Write in database
                    # Code

                st.success(f"Submission Time: {date} {time}. Hope you have a great day! 😊")
                st.balloons()
            else:
                st.warning(f"Sorry {name} you are incorrect. Please try again.")

        
        
        
    elif selected == "Leader Board":
        # Leader Board
        st.write("Leader Board")





# Incorrect Password
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

