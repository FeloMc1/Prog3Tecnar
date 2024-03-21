#primer punto
lista = list()

#segundo punto
lista1 = ["Carros", "Casas", "Celulares", "Tiendas", "Colegios", "Marcas", "Perros"]
#tercer punto
print(len(lista1))

#cuarto punto
primer = lista1[0]
central = lista1[3]
ultimo = lista1[6]
print(primer, central, ultimo)

#quinto punto
tipos_datos_mezclados = ("Felipe","22","170","Soltero","Nelson Mandela")
print(tipos_datos_mezclados)

#sexto punto
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#septimo punto
it_companies.append("LinkedIn")
print(it_companies)
#Octavo punto
if it_companies.index("Google"):
    print("Sí existe la empresa google ")

#Noveno punto
it_companies.sort()
print(it_companies)

#Décimo punto
it_companies.reverse()
print(it_companies) 

#Onceavo punto
it_companies.pop(0)
print(it_companies)

#doceavo punto
it_companies.clear()
print(it_companies)
