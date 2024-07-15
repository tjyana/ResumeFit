import streamlit as st

def main():
    # Title
    st.title("Input Form")

    # Input fields
    input1 = st.text_input("Enter Input 1")
    input2 = st.text_input("Enter Input 2")

    # Submit button
    if st.button("Submit"):
        # Process the inputs
        process_inputs(input1, input2)

def process_inputs(input1, input2):
    # Process the inputs here
    st.write("Input 1:", input1)
    st.write("Input 2:", input2)

if __name__ == "__main__":
    main()
