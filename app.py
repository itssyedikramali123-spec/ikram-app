import streamlit as st
st.title("IKRAMs score calculator")
#lets set up two variable to compare
my_score=st.number_input("enter your score:",min_value=0,max_value=100,value=90)
passing_score=70
perfect_score=100
#. greater than (>)
if my_score>passing_score:
    st.write("yesss YOU have proved yourself you passed")
if my_score<passing_score:
    st.write("you are failed YOU need hardwork")
if my_score==perfect_score:
    st.write("you got perfect score you are unbeatable")
#== is sign og equal and!= is for not equal to
if my_score!=perfect_score:
    st.write("you have to do more hardwork to acheive 100")
if my_score>=85:
    st.write("you got an A grade")
elif my_score>=70:
    st.write("you got B grade")
elif my_score>=55:
    st.write("you got C grade")
elif my_score>=40:
    st.write("you got D grade")
else:
    st.write("you got E grade")
        

