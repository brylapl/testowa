import streamlit as st

def sklady_wyjsciowe(list1,list2):
    max_len = max(len(list1), len(list2))
    min_len = min(len(list1), len(list2))
    st.write(max_len, 'vs' ,min_len)

        
