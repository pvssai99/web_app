import streamlit as st
import functions

todos = functions.get_todos()
error_msg = "play"

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    if todo_local.strip() != "":
        if todo_local not in todos:
            todos.append(todo_local)
            functions.write_todos(todos)
        else:
            error_msg = "Todo already exists"
    else:
        error_msg = "Enter a valid todo"
    st.session_state["new_todo"] = ""


st.title("To-do App")

index_list = []

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        index_list.append(index)
        if st.button("remove"):
            for ind in index_list:
                todos.pop(ind)
                functions.write_todos(todos)
                del st.session_state[index]
                st.rerun()

st.text_input(label=f"Enter a todo: ", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
