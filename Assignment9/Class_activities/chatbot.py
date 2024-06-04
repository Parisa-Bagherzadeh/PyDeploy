import streamlit as st
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import User, Message


@st.cache_resource
def connect_to_database():
    engine = create_engine("sqlite:///database.db")
    SQLModel.metadata.create_all(engine)
    return engine

engine = connect_to_database()

def ai(user_text_message):
    ai_text_message = user_text_message * 3
    return ai_text_message

def process(user_text_message):
    ai_text_message = ai(user_text_message)

    user_message = Message(text=user_text_message, type="user", user_id=1)
    ai_message = Message(text=ai_text_message, type="ai", user_id=1)


    #backend
    with Session(engine) as session:
        session.add(user_message)
        session.add(ai_message)
        session.commit()



    #frontend
    st.session_state.messages.append({'type':'user', 'text':user_text_message})
    st.session_state.messages.append({'type':'ai', 'text':'Hey there'})
    return ai_text_message



if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["type"]):
        st.write(message["text"])


if user_text_message := st.chat_input("Send a new message..."):
    
    ai_text_message = process(user_text_message)

    with st.chat_message("user"):
        st.write(user_text_message)

    with st.chat_message("ai"):
        st.write(ai_text_message)    