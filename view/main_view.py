import streamlit as st
from controller.cyk import is_accepted, get_table_element, get_parse_tree

def MainView():
    st.title("Parsing Kalimat Baku Bahasa Indonesia")
    st.write("Aplikasi ini dibuat untuk memenuhi tugas akhir mata kuliah Teori Bahasa dan Automata.")

    st.header("Input Kalimat")
    input_sentence = st.text_input("Kalimat", "")
    if input_sentence != "":
        if is_accepted(input_sentence):
            st.write("Kalimat tersebut diterima.")
        else:
            st.write("Kalimat tersebut tidak diterima.")
    else:
        st.write("Masukkan kalimat di atas untuk memulai.")

    st.header("Tabel")
    if is_accepted(input_sentence):
        st.table(get_table_element(input_sentence))
    
    st.header("Parse Tree")
    if is_accepted(input_sentence):
        st.graphviz_chart(get_parse_tree(input_sentence))