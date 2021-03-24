import os
	
	#SE crea el grafo de ejemplo
	grafo = {'a': [('p',4), ('j',15), ('b',1)],
	       	'b': [('a',1), ('d',2), ('e',2), ('c',3)],
		'j': [('a',15)],
		'p': [('a', 4)],
		'd': [('b',2), ('g',3)],
		'e': [('b',2), ('g',4), ('f',5), ('c',2)],
		'c': [('b',3), ('e',2), ('f',5), ('i',20)],
		'g': [('d',3), ('e',4), ('f',10), ('h',1)],
		'f': [('g',10), ('e',5), ('c',5)],
		'i': [('c',20)],
		'h': [('g',1)] 
		}
	

	#MUESTRA EL GRAFO
	print("Grafo antes del recorrido: \n")
	for key, lista in grafo.items():
		print(key)
		print(lista)
	

	print()
	os.system("pause")
			
	visitados = []
	pila = []
	
    #Se ingresa el nodo del cual se quiere partir
	origen = input("Ingresa un nodo: ")
	print("\nLista de recorrido en profundidad\n")

	#1: Se pone el vertice al inicio de la ´pila
	pila.append(origen)
	
	#2: Se ejecuta siempre y cuando la pila no este vacía
	while pila:
		#3: se desapila un vertice para convertirlo en el actual
		actual = pila.pop()
		


		#4: En caso de que el vertice no haya sido visitado se imprime el actual
		if actual not in visitados:
		
			print("Vertice actual -> ", actual)
			
			#6: se coloca el vertice en la lista de vertices que ya han sido visitados
			visitados.append(actual)
		
		#7:se apila cada vertice que tiene como destino el vertice actual
		for key, lista in grafo[actual]:
			if key not in visitados:
				pila.append(key)
	

	print()
	os.system("pause")

