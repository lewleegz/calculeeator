import streamlit as st

# Initialize session state variables
if "calculation" not in st.session_state:
    st.session_state.calculation = ""
if "nth_root_mode" not in st.session_state:
    st.session_state.nth_root_mode = False

# Function to display the current calculation
def display_calculation():
    st.text_area("Calculation", value=st.session_state.calculation, height=70)

# Function to add symbols to the calculation
def add_to_calculation(symbol):
    st.session_state.calculation += str(symbol)

# Function to clear the calculation
def clear_field():
    st.session_state.calculation = ""
    st.session_state.nth_root_mode = False

# Function to activate nth root mode
def activate_nth_root():
    st.session_state.calculation += "√"
    st.session_state.nth_root_mode = True

# Function to evaluate the calculation
def evaluate_calculation():
    try:
        if st.session_state.nth_root_mode:
            # Handle nth root calculation
            n, x = st.session_state.calculation.split("√")
            n = float(n)
            x = float(x)
            result = x ** (1 / n)
            st.session_state.calculation = str(round(result, 10))
            st.session_state.nth_root_mode = False
        else:
            # Evaluate the expression
            st.session_state.calculation = str(eval(st.session_state.calculation))
    except:
        st.session_state.calculation = "Error"

# Display the current calculation
display_calculation()

# Create calculator buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"): add_to_calculation(7)
    if st.button("4"): add_to_calculation(4)
    if st.button("1"): add_to_calculation(1)
    if st.button("AC"): clear_field()

with col2:
    if st.button("8"): add_to_calculation(8)
    if st.button("5"): add_to_calculation(5)
    if st.button("2"): add_to_calculation(2)
    if st.button("0"): add_to_calculation(0)

with col3:
    if st.button("9"): add_to_calculation(9)
    if st.button("6"): add_to_calculation(6)
    if st.button("3"): add_to_calculation(3)
    if st.button("="): evaluate_calculation()
    if st.button("x^y"): add_to_calculation("**")

with col4:
    if st.button("plus"): add_to_calculation("+")
    if st.button("minus"): add_to_calculation("-")
    if st.button("x"): add_to_calculation("*")
    if st.button("/"): add_to_calculation("/")
    if st.button("y√x"): activate_nth_root()