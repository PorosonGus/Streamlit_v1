import streamlit as st

# Title for the web app
st.title("Leetekas, õpime arvutama")

# User input for a number
user_input = st.number_input("Sisesta number")

# Calculate the square of the input
square = user_input ** 2

# Display the result
st.write(f"Ruut numbrist {user_input} on {square}")
