import streamlit as st
col1,col2,col3=st.columns(3)
col2.image("percentage\makaut.png",width=300)
st.title("makaut percentage calculator")
st.subheader("Convert your MAKAUT SGPA to percentage in one click")
odd_sem=st.number_input("Enter ODD Semester SGPA" ,min_value=0.0,max_value=10.0,step=0.1,)
even_sem=st.number_input("Enter Even Semester SGPA" ,min_value=0.0,max_value=10.0,step=0.1)

def percentage(odd_sem,even_sem):
    if odd_sem==0.00:
        st.warning("please enter your odd sem correctly")
    elif even_sem==0.00:
        st.warning("please enter your even sem correctly")
    else:
        percent=((float(odd_sem)+float(even_sem))/2-0.75)*10
        percent=round(percent,2)
        st.success(f"""succesfully calculated
               your percentage is: {percent}%""")
        
if st.button("Submit",type="primary"):
    percentage(odd_sem,even_sem)