def html(list1, list2,tytul,soccerrating_home_name,soccerrating_away_name):
    max_len = max(len(list1), len(list2))
    min_len = min(len(list1), len(list2))

    # dodanie pustych wartości do krótszej listy
    if len(list1) < max_len:
        list1 += [''] * (max_len - min_len)



    elif len(list2) < max_len:
        list2 += [''] * (max_len - min_len)



    # tworzenie tabeli HTML
    html = "<div class='container mw-100'>\n"
    html += "<table class='table table-responsive table-striped text-center table-dark table-sm'>\n"
    html += f"<tr><th class='fw-bold' colspan='4'>{tytul}</th></tr>"
    html += "<tr>\n"
    html += f"<th class='bg-dark text-white fw-bold' colspan='2'>{soccerrating_home_name}</th>\n"
    html += f"<th class='bg-dark text-white fw-bold' colspan='2'>{soccerrating_away_name}</th>\n"
    return html
