import streamlit as st
from streamlit_option_menu import option_menu
from Firebase.cred import initialize_firebase
from Users.user_interface import user_ui
from Ngos.ngo_interface import ngo_interface
from Ngos.register_ngo import ngo_registration
from Info.about_us import about_us
from datetime import datetime
import os
from blockchain.blockchain import get_transactions_last_3_minutes
from Firebase.db_interaction import NGO_Database
from Ngos.upldate_ngo import update_profile

# Custom component for the sidebar
def sidebar(db):
    # st.sidebar.title("NGO Navigation")
    # ngo_action = st.sidebar.radio("Select Action", ["Login", "Register NGO"])
    if st.session_state.get("logged_in"):
        ngo_interface(db)
        
    else:
        with st.sidebar:
            ngo_action = option_menu("NGO Navigation", ["Login", "Register NGO","About-Us"],icons=["box-arrow-in-right", "pencil-square","info-circle"])
        
        if ngo_action == "Login":
            ngo_interface(db)
            
        elif ngo_action == "Register NGO":
            ngo_registration(db)
        
        elif ngo_action == "About-Us":
            about_us()             

# Function to display the main page and navigation options
def main():
    # Initialize Firebase once
    db = initialize_firebase()
    if st.session_state.get("timestamp") is None:
        st.session_state["timestamp"] = datetime.now()
    if (datetime.now() - st.session_state["timestamp"]).seconds > 160:
        st.session_state["timestamp"] = datetime.now()
        f=os.fork()
        if f==0:
            print("Checking for transactions")
            ngo_db=NGO_Database(db)
            
            get_transactions_last_3_minutes([i["metamask_address"] for i in ngo_db.get_ngos()])
            exit(0)

    # Custom CSS to modify the design according to your requirements
    st.markdown("""
        <style>
        /* Global Settings */
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom, #1a202c, #000000);
            color: #f1f1f1;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .stApp {
            background: linear-gradient(to bottom, #1a202c, #000000);
        }
        
        .css-1d391kg {  /* Targets the sidebar */
        background: linear-gradient(to bottom, #1a202c, #000000);
        }
        .css-1d391kg > div { /* This centers the content within the sidebar */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .css-1d391kg .css-2vl3m9 {  /* Targets the option menu */
            background-color: transparent;  /* Keep transparent to show gradient */
        }
        .css-2vl3m9 .nav-item {  /* Aligns the individual nav items to center */
            text-align: center;
            width: 100%;
        }

        /* Card styling */
        .card {
            display: flex;
            flex: 1 1 auto;
            background-color: #2d3748;
            border-radius: 0.5rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            overflow: hidden;
            max-width: 64rem;
            width: 100%;
            margin: 2rem auto;
        }
        .card-content {
            display: flex;
            flex-direction: column;
        }
        @media (min-width: 768px) {
            .card-content {
                flex-direction: row;
            }
        }
        .image-container {
            flex: 1;
            padding-top: 6.1rem;
        }
        .image-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .text-container {
            flex: 1;
            padding: 2rem;
        }
        .card h1, .card h3 {
            color: #e5e5e5;
        }
        /* Button styling */
        .stButton > button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 9999px;
            padding: 0.5rem 1rem;
            border: none;
            font-size: 1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            margin: 0.5rem 0;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #FFFFFF;
            color: #FF4B4B;
            transform: scale(1.05);
        }
        </style>
        """, unsafe_allow_html=True)

    # Check if the user role is stored in session_state
    if 'role' not in st.session_state:
        st.session_state['role'] = None

    # If role is not set, display the landing page with role selection
    if st.session_state['role'] is None:
        
        
        # st.markdown('<div class="card"><div class="card-content">', unsafe_allow_html=True)
        
        # Create two columns for the layout
        col1, col2 = st.columns(2, gap='medium')
        
        # Image in the first column
        with col1:
            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            st.image("./temp.png")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Text and buttons in the second column
        with col2:
            st.markdown('<div class="text-container">', unsafe_allow_html=True)
            st.markdown("<h1>Welcome to NexusNGO</h1>", unsafe_allow_html=True)
            st.markdown("<h3>Connecting donors with NGOs to make a lasting impact.</h3>", unsafe_allow_html=True)
            st.markdown("<h3>Please select your role:</h3>", unsafe_allow_html=True)
            
            # Donor and NGO buttons for navigation
            donor_button = st.button("I'm a Donor")
            ngo_button = st.button("I'm an NGO")
            # about_us_button = st.button("About Us")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Store the selected role in session_state
        if donor_button:
            st.session_state['role'] = 'Donor'
            st.rerun()  # Immediately rerun to hide the role selection
        elif ngo_button:
            st.session_state['role'] = 'NGO'
            st.rerun()  # Immediately rerun to hide the role selection
        # elif about_us_button:
        #     about_us()
            # st.rerun()

    # If role is selected, redirect to respective interface
    if st.session_state['role'] == 'Donor':
        st.markdown('<div class="content-container">', unsafe_allow_html=True)
        user_ui(db)
        st.markdown('</div>', unsafe_allow_html=True)
    elif st.session_state['role'] == 'NGO':
        st.markdown('<div class="content-container">', unsafe_allow_html=True)
        sidebar(db)
        st.markdown('</div>', unsafe_allow_html=True)

    # Add a "Select Role" option in the sidebar for easy role switching
    if st.session_state['role'] is not None:
        if st.sidebar.button("Select Role"):
            reset_role()
            st.rerun()  # Refresh the app to return to the role selection page

# Function to reset the role and go back to the landing page
def reset_role():
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]

# Run the main function
if __name__ == "__main__":
    main()