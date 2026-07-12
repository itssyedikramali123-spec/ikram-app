import streamlit as st
st.title(" Ikram's DISCOUNT & TAX calculator")
real_prize=st.number_input("Enter your MRP prize of product :",min_value=0,max_value=10000000,value=0)
discount=st.number_input("Enter your discount percentage :",min_value=0,max_value=100,value=0)
#real_discount=rc
rc=real_prize/100*discount
p=real_prize-rc
st.write("your MRP after discount is",p)
st.write("Total money you saved",rc)

