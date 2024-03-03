import streamlit as st

def sklady_wyjsciowe(list1,list2):
max_len = max(len(list1), len(list2))
min_len = min(len(list1), len(list2))
st.write(max_len, 'vs' ,min_len)
# dodanie pustych wartości do krótszej listy
if len(list1) < max_len:
    list1 += [''] * (max_len - min_len)

elif len(list2) < max_len:
    list2 += [''] * (max_len - min_len)
  
st.write(max_len, 'vs' ,min_len)
    
