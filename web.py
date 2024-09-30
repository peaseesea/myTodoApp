import streamlit as st
import functions as fn

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.write_todos(todos)
    st.rerun

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("this is to increase your productivity")

todos = fn.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(placeholder="Add new todo....",
              on_change=add_todo, key='new_todo')

st.session_state
