def tytul(name):
	th = f'''<tr>\n<th class='bg-dark fw-bold h3 text-warning' colspan="3">{name}</th>\n</tr>\n'''
	return th

def rodzaj(*args):
    th = f'''<tr>\n<th class='bg-dark text-danger h4'>{args[0]}</th>\n<th class='bg-dark text-white fw-bold'>{args[1]}</th>\n<th class='bg-dark text-white fw-bold'>{args[2]}</th>\n</tr>\n'''
    return th

def dane(*kurs):
    for i in range(len(kurs)):
        t = f'''<tr>\n<td>{kurs[0][0]}</td>\n<td class='bg-dark text-white h6'>{kurs[0][1]}</td>\n<td>{kurs[0][2]}</td>\n</tr>\n'''
        return t


def glowna(win,dc,gole0,gole1,gole2,gole3,gole4,dnb,bts,home0,home1,away0,away1):
	t = '<div class="container">\n'
	t += '<table class="table table-striped text-center table-dark">\n'
	t += '''<tr>\n<th class='bg-dark text-white fw-bold' colspan="3">Oczekiwane kursy</th>\n</tr>\n'''
	t += tytul('Regulaminowy czas')
	t += rodzaj('1','X','2')
	t += dane(win)
	t += tytul('Podwójna szansa')
	t += rodzaj('1X','12','X2')
	t += dane(dc)
	t += tytul('Gole')
	t += rodzaj('Over','Linia','Under')
	t += dane(gole0)
	t += dane(gole1)
	t += dane(gole2)
	t += dane(gole3)
	t += dane(gole4)
	t += tytul('DNB')
	t += rodzaj('Home','','Away')
	t += dane(dnb)
	t += tytul('Obie strzelą')
	t += rodzaj('Tak','','Nie')
	t += dane(bts)
	t += tytul('Gole gospodarzy')
	t += rodzaj('Over','','Under')
	t += dane(home0)
	t += dane(home1)
	t += tytul('Gole gości')
	t += rodzaj('Over','','Under')
	t += dane(away0)
	t += dane(away1)
	t += '</div>'
	return t
