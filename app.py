import streamlit as st
st.title("IKRAMs score calculator")
st.markdown("### *Check Your Results Instantly!*")
st.markdown("___")
#lets set up two variable to compare
my_score=st.number_input("enter your score:",min_value=0,max_value=100,value=90)
st.markdown("___")
passing_score=70
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
if my_score!=perfect_score:
    st.write("you have to do more hardwork to acheive 100")
if my_score>=85:
    st.balloons()
    st.write("you got an A grade")
elif my_score>=70:
    st.snow()
    st.info("you got B grade")
elif my_score>=55:
    st.snow()
    st.warning("you got C grade")
elif my_score>=40:
    st.image("https://media.giphy.com?media?13q2Z6G1MMmZ84vsc/giphy.gif",width=150)
    st.info("you got D grade")
else:
    st.error("you got E grade")
        

