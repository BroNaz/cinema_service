
def data_check(date:str) -> bool:
    try:
        d = datetime.datetime.strptime(date, '%Y').date()
        res = d.year >= 1900
    except:
        return False
    return res 

def person_preparation(person:str) -> list():
    res = person.split(' ',2)
    if len(res) < 2: 
        res.append('')
    return res 

def is_number(var):
    try:
        if var == int(var):
            return True
    except Exception:
        return False