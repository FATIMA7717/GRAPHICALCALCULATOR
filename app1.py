pip install matplotlib numpy
streamlit run app.py
# Step 1: Import necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Title of the app
st.title("Graphical Calculator")

# Basic Arithmetic Operations
st.subheader("Basic Arithmetic Operations")
num1 = st.number_input("Enter number 1:", value=0.0)
num2 = st.number_input("Enter number 2:", value=0.0)

operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.write("Addition Result:", result)
    elif operation == "Subtract":
        result = num1 - num2
        st.write("Subtraction Result:", result)
    elif operation == "Multiply":
        result = num1 * num2
        st.write("Multiplication Result:", result)
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write("Division Result:", result)
        else:
            st.write("Error: Division by zero")

# Trigonometric Functions
st.subheader("Trigonometric Functions")
single_value = st.number_input("Enter a single number for trigonometric functions:", value=0.0)

trig_function = st.selectbox("Choose a trigonometric function:", ["Sine", "Cosine", "Tangent"])
if st.button("Calculate Trigonometric Function"):
    if trig_function == "Sine":
        result = np.sin(single_value)
        st.write(f"sin({single_value}) =", result)
    elif trig_function == "Cosine":
        result = np.cos(single_value)
        st.write(f"cos({single_value}) =", result)
    elif trig_function == "Tangent":
        result = np.tan(single_value)
        st.write(f"tan({single_value}) =", result)

# Graph Plotting
st.subheader("Custom Plot of X vs Y")
x_values_input = st.text_input("Enter x values (comma-separated):")
y_values_input = st.text_input("Enter y values (comma-separated):")

if st.button("Plot Custom Graph"):
    try:
        x_values = list(map(float, x_values_input.split(',')))
        y_values = list(map(float, y_values_input.split(',')))
        
        if len(x_values) != len(y_values):
            st.write("Error: x and y values must have the same number of elements.")
        else:
            plt.figure(figsize=(8, 5))
            plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
            plt.xlabel('X values')
            plt.ylabel('Y values')
            plt.title('Custom Plot of X vs Y')
            plt.grid(True)
            st.pyplot(plt)
            plt.close()  # Close the plot after displaying
    except ValueError:
        st.write("Error: Please enter valid numeric values separated by commas.")

