import streamlit as st
from controller.cyk import is_accepted, get_table_element, get_parse_tree, get_sentance_pattern

def MainView():
    st.title("Parsing Kalimat Baku Bahasa Indonesia")
    st.write("Aplikasi ini dibuat untuk memenuhi tugas akhir mata kuliah Teori Bahasa dan Automata.")

    st.header("Input Kalimat")
    input_sentence = st.text_input("Kalimat", "")
    if input_sentence != "":
        if is_accepted(input_sentence):
            st.success('Kalimat tersebut diterima!', icon="✅")
        else:
            st.error('Kalimat tersebut tidak diterima', icon="❌")
    else:
        st.write("Masukkan kalimat di atas untuk memulai.")

    st.header("Tabel")
    if input_sentence != "":
        st.table(get_table_element(input_sentence))
    
    # st.header("Parse Tree")
    # if is_accepted(input_sentence):
    #     st.graphviz_chart(get_parse_tree(input_sentence))

    # if is_accepted(input_sentence):
    #     st.subheader("Pola Kalimat = " + get_sentance_pattern())