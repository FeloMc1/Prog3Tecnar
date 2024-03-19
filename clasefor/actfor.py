vuelo = {'Aerolinea':'Avianca','Vuelo':'AV3102','Origen':'CTG','Destino':'MED','Tipo_Maleta':["Cabina","Mano","Bodega"]}

for  key, value in vuelo.items():
    print(value)
for maleta in vuelo['Tipo_Maleta']:
    print(maleta)
