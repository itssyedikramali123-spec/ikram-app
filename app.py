import streamlit as st
st.title("IKRAMs score calculator")
st.markdown("### *Check Your Results Instantly!*")
st.markdown("___")
#lets set up two variable to compare
x=st.number_input("enter your score of subject 1:",min_value=0,max_value=100,value=0)
y=st.number_input("enter your score of subject 2:",min_value=0,max_value=100,value=0)
z=st.number_input("enter your score of subject 3:",min_value=0,max_value=100,value=0)
a=st.number_input("enter your score of subject 4:",min_value=0,max_value=100,value=0)
b=st.number_input("enter your score of subject 5:",min_value=0,max_value=100,value=0)
f=(a+b+x+y+z)
my_score=(f/5)
st.markdown("___")
passing_score=25
perfect_score=100
#. greater than (>)
if my_score>passing_score:
    st.success("yesss YOU have proved yourself you passed")
if my_score<passing_score:
    st.error("you are failed YOU need hardwork")
if my_score==perfect_score:
    st.balloons()
    st.write("you got perfect score you are unbeatable")
#== is sign og equal and!= is for not equal to
if my_score>passing_score:
    st.write(my_score)
if my_score>=90:
    st.balloons()
    st.write("you got an A grade")
elif my_score>=70:
    st.snow()
    st.info("you got B grade")
elif my_score>=60:
    st.snow()
    st.warning("you got C grade")
elif my_score>=40:
    st.info("you got D grade")
else:
    st.error("you got E grade")
        

