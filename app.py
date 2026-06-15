import streamlit as st
st.title("grade and goal checker")
#lets set up two variable to compare
my_score=st.number_input("enter your score:",min_value=0,max_value=100,value=90)
passing_score=70
perfect_score=100
#. greater than (>)
if my_score>passing_score:
    st.write("hey you did it you are pased")
if my_score<passing_score:
    st.write("you are failed do some study")
if my_score==perfect_score:
    st.write("you got perfect score you are unbeatable")
#== is sign og equal and!= is for not equal to
if my_score!=perfect_score:
    st.write("you are left with only some points from 100")
if my_score>=85:
    st.write("you got an A grade")
