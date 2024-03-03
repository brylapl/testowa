import sqlite3
def pokaz():
	conn = sqlite3.connect('soccer.db')
	c = conn.cursor()
	options = [row[0] for row in c.execute(f'SELECT ID FROM list_teams').fetchall()]
	st.markdown('''<h1 class='fw-bold text-center'>Obliczanie Kursów</h1>''',unsafe_allow_html=True)    
	team = st.selectbox('Wybierz drużynę', options,index=None,placeholder="Wybierz drużynę")
	if team != '':
	    for row in c.execute(f'SELECT * FROM list_teams WHERE ID like "{team}"'):
	        st.markdown(f'''
	                    <div class="select_team">
	                        <h3 class="info text-white">Drużyna: 
	                        <span class="info text-white">{row[0]}</span>
	                        </h3>
	                        <h3 class="info text-white">Kraj: 
	                        <span class="info text-white">{row[1]}</span>
	                        </h3>
	                        <h3 class="info text-white">Liga: 
	                        <span class="info text-white">{row[2]}</span>
	                        </h3>
	                        </div>''',unsafe_allow_html=True)
	        APWIN = row[3]
	        MAKEYOURSTATS = row[4]
	        BESOCCER = row[5]
	        FOOTYSTATS = row[6]
	        SOCCERRATING = row[7]
