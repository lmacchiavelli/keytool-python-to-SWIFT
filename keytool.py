"""
#input testo

#inserimento gruppi di keyword

# titolo
# corpo

#associare gruppi di keyword

----
#menu crea gruppo
#Aggiungo keyword al gruppo
#edito il documento che evidenzia le yeyword in base al gruppo associato
----

dizionario gruppo
associo lista keyword al gruppo
edito il gruppo


----
#creo gruppi --> dico
"""


  
# # inititialising json object 
# ini_string = {'nikhil': 1, 'akash' : 5,  
#               'manjeet' : 10, 'akshat' : 15} 
  
# # printing initial json 
# ini_string = json.dumps(ini_string) 
# print ("initial 1st dictionary", ini_string) 
# print ("type of ini_object", type(ini_string)) 
  
# converting string to json 

  
# printing final result 

gruppi = []

def creaGruppi():
	
	#cliclo continuo finchè non digito exit
	index = 0
	while True:
		#Resetto le keyword
		keyword = []
		#Prendo Input per nome del gruppo ad esempio h1, h2 , titolo
		inputGruppo = input("Inserisci il nome del gruppo es: H1 : ")
		#creo un index incrementale da assegnare al gruppo
		index += 1

		if inputGruppo != '<':
			#assegno le keyword create al gruppo
			gruppi.append({
				"id": index,
				"name": inputGruppo,
				"keyword" : keyword,
			})
			while True:
				
				inputKey = input("Keyword")
				
				if inputKey != '<':
					keyword.append(inputKey)
				else:
					break
		else:
			creaContenuti()
			break
			

def creaContenuti():
	for i in gruppi:
		print(i["name"])

creaGruppi()
creaContenuti()
# print(gruppi)

