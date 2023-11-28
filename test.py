import streamlit as st
import hashlib

user_database = {}


def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def register_user(email, password):
    hashed_password = hash_password(password)
    user_database[email] = hashed_password


def login_user(email, password):
    hashed_password = hash_password(password)
    stored_password = user_database.get(email)
    return stored_password and stored_password == hashed_password


def main():
    st.title("Registration System")

    page = st.sidebar.radio("Select a page", ["Home", "Sign Up", "Sign In"])

    if page == "Home":
        st.header("Welcome to the Registration System")
        st.write("Choose a page from the sidebar to get started.")

    elif page == "Sign Up":
        st.header("Sign Up")
        email = st.text_input("Email:")
        password = st.text_input("Password:", type="password")

        if st.button("Sign Up"):
            if email and password:
                register_user(email, password)
                st.success("Registration successful! Now you can sign in.")
            else:
                st.warning("Please provide both email and password.")

    elif page == "Sign In":
        st.header("Sign In")
        email = st.text_input("Email:")
        password = st.text_input("Password:", type="password")

        if st.button("Sign In"):
            if email and password:
                if login_user(email, password):
                    st.success(f"Welcome, {email}! You are now signed in.")
                else:
                    st.error("Invalid email or password. Please try again.")
            else:
                st.warning("Please provide both email and password.")


if __name__ == "__main__":
    main()
