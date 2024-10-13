"""
    Cambiar palabra del archivo fichero.txt por otra palabra.

    fichero_leer = open("fichero.txt","r") -> abre el archivo en modo lectura  ("r" lectura, "w" write )
    texto = fichero_leer.read() -> lee el contenido del archivo
    fichero_leer.close() = Cierra el archivo

    fichero_escribir = open("fichero.txt","w") -> abre el archivo en modo escritura.
    fichero_escribir.write() -> escribe el contenido del archivo.
    fiechero_escribir.close() -> Cierra el archivo
"""
import sys

argumentos = sys.argv
print ('los argumentos de la llamada son', argumentos)
print ('la palabra a buscar es' , argumentos[2])
print ('la palabra sustituta' , argumentos[3])
print ('el fichero es', argumentos[1])

archivo_txt = argumentos[1]
palabra_buscar = argumentos[2]
palabra_nueva = argumentos [3]

#Abrir archivo
#leer el contenido del archivo y guardarlo en una variable (string)
#cierro archivo
#fichero_leer = open("fichero.txt","r")
#texto = fichero_leer.read()
#fichero_leer.close()
with open(archivo_txt,'r') as fichero:
    original = fichero.read()

#Buscar la palabra que quiero cambiar
#¿Debes iterar?
#Sustituir la palabra por la nueva
#no necesita iterar, basta con usar replace
#https://docs.python.org/es/3/library/stdtypes.html#str.replace
nuevo_texto = original.replace(palabra_buscar,palabra_nueva)

#Abrir el fiechero
#escribir nuevo contenido (string)
#cerrar el fichero

#fichero_escribir = open("fichero.txt","w")
#fichero_escribir.write(nuevo_texto)
#fichero_escribir.close()

with open(archivo_txt,'w') as archivo:
    archivo.write(nuevo_texto)
