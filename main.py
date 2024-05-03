import langchain_helper as lch
import streamlit as st

# setting a title for our web page
st.title('Pets name generator')

# creating a drop-down of pets for our user to use
user_animal_type = st.sidebar.selectbox("What is your animal type?", ("cat", "dog", "horse"))

# creating a text area for our user to choose from
pet_color = st.sidebar.text_area(label=f"what color is your {user_animal_type}?", max_chars=15)

# showing our results after the user has finished choosing by calling our pet generator
if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])
    st.text(lch.langchain_agent())

#streamlit run main.py to run the application
