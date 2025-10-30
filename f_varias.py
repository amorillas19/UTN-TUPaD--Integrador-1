def limpiar_string (a:str)->str:
    
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("'", "")
    a = a.strip().split(",")
    a = a[0]

    return a

if __name__ == "__main__":

    limpiar_string("['Europe', 'Asia']")