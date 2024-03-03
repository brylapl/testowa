import streamlit as st

def sklady_wyjsciowe(list1,list2,flagi_home,flagi_away,tytul):
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
    
    # tworzenie tabeli HTML
    html = "<div class='container mw-100'>\n"
    html += "<table class='table table-responsive table-striped text-center table-dark table-sm'>\n"
    html += f"<tr><th class='fw-bold' colspan='4'>{tytul}</th></tr>"
    html += "<tr>\n"
    html += f"<th class='bg-dark text-white fw-bold' colspan='2'>HOME NAME</th>\n"
    html += f"<th class='bg-dark text-white fw-bold' colspan='2'>AWAY NAME}</th>\n"
    html += "</tr>\n"
    if power:
        html += "<tr>\n"
        html += f"<th class='bg-dark text-white fw-bold' colspan='2'>STATS HOME</th>\n"
        html += f"<th class='bg-dark text-white fw-bold' colspan='2'>STATS AWAY</th>\n"
        html += "</tr>\n"
    for i in range(max_len):
        # flaga = flagi_home[i].split('/')[-1]
        # flaga = flaga.split('.')[0]
        # flaga = f'/content/{flaga}.svg'
        html += "<tr>\n"
        html += f"<td><img src='{flagi_home[i]}' alt=''</img></td><td>{list1[i]}</td>\n"

        html += f"<td><img src='{flagi_away[i]}' alt=''</img><td>{list2[i]}</td>\n"
        html += "</tr>\n"

    html += "</table>\n"
    html += "</div>"
    return html


    
