def tytul(name):
	th = f'''<tr>\n<th class='bg-dark text-white fw-bold h2' colspan="3">{name}</th>\n</tr>\n'''
	return th

def rodzaj(*args):
    th = f'''<tr>\n<th class='bg-dark text-white fw-bold'>{args[0]}</th>\n<th class='bg-dark text-white fw-bold'>{args[1]}</th>\n<th class='bg-dark text-white fw-bold'>{args[2]}</th>\n</tr>\n'''
    return th

def dane(*kurs):
    for i in range(len(kurs)):
        t = f'''<tr>\n<td>{kurs[0][0]}</td>\n<td class='bg-dark text-white fw-bold'>{kurs[0][1]}</td>\n<td>{kurs[0][2]}</td>\n</tr>\n'''
        return t


def glowna():
    t = '<div class="container">\n'
    t += '<table class="table table-striped text-center table-dark">\n'
    t += '''<tr>\n<th class='bg-dark text-white fw-bold' colspan="3">Oczekiwane kursy</th>\n</tr>\n'''
    t = tytul('Regulaminowy czas')
    t += rodzaj('1','X','2')
    return t
