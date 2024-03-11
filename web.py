import streamlit as st
import functions

# Initialize session state
if 'todos' not in st.session_state:
    st.session_state.todos = functions.get_todos()


# Define Streamlit app content
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    st.session_state.todos.append(todo)
    functions.write_todos(st.session_state.todos)

def main():
    st.title("My Todo App")
    st.subheader("Welcome to my todo app!")
    st.write("This app helps to increase your <b>productivity</b>.", unsafe_allow_html=True)

    for index, todo in enumerate(st.session_state.todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            st.session_state.todos.pop(index)
            functions.write_todos(st.session_state.todos)
            del st.session_state[todo]
            st.rerun()

    st.text_input(label="", placeholder="Add new todo...",
                  on_change=add_todo, key='new_todo')


# Run Streamlit app
if __name__ == "__main__":
    main()
