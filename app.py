# Step 1: Install required libraries
# Run this command in the terminal to install Streamlit and Matplotlib if they are not already installed.
# !pip install streamlit matplotlib numpy

# Step 2: Import necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Step 3: Create input boxes for two values and output area
st.title("Graphical Calculator")

# Basic Arithmetic Operations
st.subheader("Basic Arithmetic Operations")
num1 = st.number_input("Enter number 1:", value=0.0)
num2 = st.number_input("Enter number 2:", value=0.0)

if st.button("Add"):
    result = num1 + num2
    st.write("Addition Result:", result)

if st.button("Subtract"):
    result = num1 - num2
    st.write("Subtraction Result:", result)

if st.button("Multiply"):
    result = num1 * num2
    st.write("Multiplication Result:", result)

if st.button("Divide"):
    if num2 != 0:
        result = num1 / num2
        st.write("Division Result:", result)
    else:
        st.write("Error: Division by zero")

# Trigonometric Functions
st.subheader("Trigonometric Functions")
single_value = st.number_input("Enter a single number for trigonometric functions:", value=0.0)

if st.button("Sine"):
    result = np.sin(single_value)
    st.write(f"sin({single_value}) =", result)

if st.button("Cosine"):
    result = np.cos(single_value)
    st.write(f"cos({single_value}) =", result)

if st.button("Tangent"):
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
    except ValueError:
        st.write("Error: Please enter valid numeric values separated by commas.")
