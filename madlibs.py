#juego de madlibs
#versiculo de la biblia 
#concatenando strings 
''' 16 Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna.
'''
palabra = " Porque de tal ________ amó Dios al mundo, que ha dado a su Hijo _________, para que todo aquel que en él cree, _____________________________________."

print(palabra)

work01 = input("Es un sinonimo de forma: ")
work02 = input("Es un sinonimo de único: ")
frase01 = input("Es una frase buena para evangelizar: ")
if work01 == "manera" and work02 == "unigénito" and frase01 == "no se pierda mas tenga vida eterna":
    print("buen juego")
else:
    print("intenta de nuevo")

madlibs = f" Porque de tal {work01} amó Dios al mundo, que ha dado a su Hijo {work02}, para que todo aquel que en él cree, {frase01}."
print(madlibs)