import streamlit as st
st.title("IKRAMs score calculator")
st.markdown("### *Check Your Results Instantly!*")
st.markdown("___")
#lets set up two variable to compare
x=st.number_input("enter your score of subject 1:",min_value=0,max_value=100,value=90)
y=st.number_input("enter your score of subject 2:",min_value=0,max_value=100,value=90)
z=st.number_input("enter your score of subject 3:",min_value=0,max_value=100,value=90)
a=st.number_input("enter your score of subject 4:",min_value=0,max_value=100,value=90)
b=st.number_input("enter your score of subject 5:",min_value=0,max_value=100,value=90)
f=(a+b+x+y+z)
my_score=(f/5)
st.markdown("___")
passing_score=150
perfect_score=500
#. greater than (>)
if my_score>passing_score:
    st.success("yesss YOU have proved yourself you passed")
if my_score<passing_score:
    st.error("you are failed YOU need hardwork")
if my_score==perfect_score:
    st.balloons()
    st.write("you got perfect score you are unbeatable")
#== is sign og equal and!= is for not equal to
if my_score!=perfect_score:
    st.write("you have to do more hardwork to acheive 100")
if my_score>=450:
    st.balloons()
    st.write("you got an A grade")
elif my_score>=350:
    st.snow()
    st.info("you got B grade")
elif my_score>=250:
    st.snow()
    st.warning("you got C grade")
elif my_score>=150:
    st.info("you got D grade")
else:
    st.error("you got E grade")
        

