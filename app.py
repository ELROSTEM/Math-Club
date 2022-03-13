from datetime import datetime

import gspread
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

#Google API credentials from st.secrets
google_api_credentials = {
"type": st.secrets['type'],
"project_id": st.secrets['project_id'],
"private_key_id": st.secrets['private_key_id'],
"private_key": st.secrets['private_key'],
"client_email":st.secrets['client_email'],
"client_id": st.secrets['client_id'],
"auth_uri": st.secrets['auth_uri'],
"token_uri": st.secrets['token_uri'],
"auth_provider_x509_cert_url": st.secrets['auth_provider_x509_cert_url'],
"client_x509_cert_url": st.secrets['client_x509_cert_url'],
}

# Gspread
sa = gspread.service_account_from_dict(google_api_credentials)
sh = sa.open('math-club')
wks = sh.worksheet('Leader Board')

# Authentication
names = (wks.col_values(1))[1:]
usernames = (wks.col_values(2))[1:]
os_passwords = (wks.col_values(3))[1:]
hashed_passwords = stauth.hasher(os_passwords).generate()

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

                #Write the data into database
                cell = wks.find(name)
                streak = wks.cell(cell.row, (cell.col + 5)).value
                wks.update_cell(cell.row, (cell.col + 5), int(streak)+1)

                st.success(f"Submission Time: {date} {time}. Hope you have a great day! 😊")
                st.balloons()
            else:
                st.warning(f"Sorry {name} you are incorrect. Please try again.")

        
    elif selected == "Leader Board":
        # Leader Board
        st.write("Leader Board")
        st.write(names)





# Incorrect Password
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

