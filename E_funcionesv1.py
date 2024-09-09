print("manejo de funciones")
def hola_mundo():
    print("hola aqui estoy deontro de la funcion")
def mensa(msg):
    print(msg)
def escribeNC(nombre, apellido):
    print(nombre,apellido)
    print(f"tu nombre completo es {nombre}{apellido}")
def suma2numeros(n1,n2):
    s=n1+n2
    return f"la suma de {n1}+{n2} es de:",s
#llamando a la funcion
hola_mundo()
mensa("hola whatsaap") #llama a mensa con 1 parametro
mensa("el profe me sorprendio enviando mensajes") #llama a mensa con 1 parametro
escribeNC("Diana","Cardenas")
print("funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))