import streamlit as st
# This is CSS code that tells the browser to make the top menu invisible
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.title("My Python Calculator 🧮")
st.write("This is my first fully functioning web app before deploying it to the world.")

# 1. Get the numbers from the user
# st.number_input is a text box that only accepts numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# 2. Create a dropdown menu to choose the math operation
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# 3. The Math Logic (This is just standard Python!)
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result is: {result}")
        
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result is: {result}")
        
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result is: {result}")
        
    elif operation == "Divide":
        # Gotta prevent that divide-by-zero error!
        if num2 == 0:
            st.error("Bro, you cannot divide by zero!")
        else:
            result = num1 / num2
            st.success(f"The result is: {result}")