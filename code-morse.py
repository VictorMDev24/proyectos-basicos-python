#programa al el cuaul el usuario le pasa un taxto y el programa lo transforma en morse

def a_morse(user):
    dic_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
    return ' '.join(dic_morse[c])
    for c in user.upper():
        if c in dic_morse:
            return dic_morse[c]
        else:
            return c       

user  = input("Introduce el texto a convertir en morse: ")
print(a_morse(user))