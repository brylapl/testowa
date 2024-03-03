import streamlit as st

def sklady_wyjsciowe(list1,list2,flagi_home,flagi_away,tytul):
    global soccerrating_home_name
    max_len = max(len(list1), len(list2))
    min_len = min(len(list1), len(list2))
    st.write(max_len, 'vs' ,min_len)
    
    if len(list1) < max_len:
        list1 += [''] * (max_len - min_len)
        flagi_home += [''] * (max_len - min_len)
    elif len(list2) < max_len:
        list2 += [''] * (max_len - min_len)
        flagi_away += [''] * (max_len - min_len)
        
    st.write(f'{len(list1)} {len(list2)}')
    st.write(len(flagi_home))
    html = "<div class='container mw-100'>\n"
    html += "<table class='table table-responsive table-striped text-center table-dark table-sm'>\n"
    html += f"<tr><th class='fw-bold' colspan='4'>{tytul}</th></tr>"
    html += "<tr>\n"
    html += f"<th class='bg-dark text-white fw-bold' colspan='2'>{soccerrating_home_name}</th>\n"
    return html


    
