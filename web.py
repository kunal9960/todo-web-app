import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo.capitalize())
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("Welcome to my todo app!")
st.write("This app helps to increase your <b>productivity</b>.",
         unsafe_allow_html=True)  # html is only for write method.


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
