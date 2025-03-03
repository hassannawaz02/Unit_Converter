import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    body{
        background-color : # ;
        color : white ;
    }
    .stApp{
        background-color : linear-graident(135deg,#bcbcbc , #cfe2f3) ;
        padding : 30px ;
        border-radius : 15px ;
        box-shadow : 0 10px 20px rgba(0,0,0,0.3) ;
    }
    h1{
        text-align : center ;
        font-size : 36px ;
        color : white ;
    }
    stButton>button{
        background-color : linear-graident(45deg,rgba(255, 0, 251, 0.4),#351c75) ;
        color : white ;
        padding : 10px 20px ;
        font-size : 18px ;
        border-radius : 10px ;
        transition: 0.3s ;
        box-shadow : 0 5px 15px rgba(0,201,255,0.4) ;
    }
    stButton>button:hover{
        color : black ;
        background : linear-graident(45deg,rgba(255, 0, 251, 0.7),#351c75) ;
        transform : scale (1.05)
    }
    .result-box{
        margin-top : 20px ;
        border-radius : 10px ;
        padding : 20px ;
        font-size : 25px ;
        box-shadow : 0 5px 15px rgb(15, 191, 240) ;
        backaground : rgb(240, 15, 15);
        font-weight : bold ;
        text-align : center ;
    }
    footer{
        color : black ;
        text-align : center ;
        margin-top : 50px ;
        font-size : 14px ;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Tittle & Description :
st.markdown("<h1>Unit Converter using Python </h1>", unsafe_allow_html=True)
st.write("This simple web app allows you to convert units of length, weight, temperature, and volume. Please select the unit to convert from and to, then enter the value.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])

value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms", "Centimeters", "Millimeters", "Miles", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilograms", "Centimeters", "Millimeters", "Miles", "Yards", "Inches"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsis", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsis", "Fahrenheit", "Kelvin"])

def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37
    }
    return (value / length_units[from_unit] * length_units[to_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit] * weight_units[to_unit])

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

if st.button("🎛️ Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Created by Hassan Nawaz</div>", unsafe_allow_html=True)
