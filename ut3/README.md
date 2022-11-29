### Funciones de listas

prueba = [1,2,16,7,3,8,3,0,9]
prueba2 = [1,2,16,7,3,4,7,5,21,3]
palabra = "Hola"

+ prueba.extend(prueba2): Añade los elementos de la lista prueba2 a la lista prueba. Si se hiciera un prueba.append(prueba2) se añadiría la lista de elementos, no los elementos.
+ prueba.copy(): Copia los elementos de la lista prueba y da igual si la lisra prueba es modificada. También se puede usar prueba3 = prueba[:] para realizar una copia de ese estilo.
+ prueba.index(i): Obtiene el indice del elemento i
+ prueba.
+ list(range(10,0,-1))
+ prueba[0]: Accede al elemento 0 de la lista
+ prueba[-1:-4:-1]: Obtiene los elementos desde el indice -1 al -4 empezando por el final de la lista
+ prueba.reverse(): Invierte la lista original.
+ reversed(prueba): Invierta la lista, pero conserva la original.
+ prueba.append(i): Añade el elemento i al final de la lista
+ prueba.insert(5, i): Añade el elemento i en la posicion 5 de la lista.
+ prueba * 3: Los elementos de la lista prueba se ven multiplicados por 3
+ del prueba[3]: Remueve el elemento que se encuentra en el indice 3.
+ prueba.remove(2): Remueve el elemento de la lista cuyo valor sea 2.
+ prueba.pop(): Remueve el ultimo elemento de la lista.
+ prueba.pop(2): Remueve el elemento de la lista con indice 2.
+ prueba.clear(): Elimina todos los elementos de la lista. (No cambia de espacio de memoria)
+ prueba = []: Elimina todos los elementos de la lista. (Ocupa un nuevo espacio de memoria)
+ prueba.count(3) == 2: Cuenta todos los elementos 3 de la lista (en este caso 2).
+ "-".join(prueba): Funciona a la inversa que palabra.split(), split separa los elementos de una palabra y los convierte en una lista, join junta los elementos de una lista en una palabra.
+ sorted(prueba): Ordena los elementos de prueba sin modificar la lista original.
+ prueba.sort(): Ordena los elementos de prueba modificando la lista original
+ sorted(prueba, reverse=True): Ordena los elementos de prueba y le da la vuelta a la lista.
+ len(prueba): Mira la longitud de la lista.
+ for i,j in zip(prueba, prueba2): Coge un elemento de cada lista al mismo tiempo, y permite comparar el elemento prueba[i] con el elemento prueba2[j]
+ prueba3 = prueba: Cada elemento esta referenciado a el elemento equivalente de la lista prueba, por lo que si se modifica prueba, prueba3 también resulta modificada.
+ Veracidad multiple:
  + enough_letter = len(palabra) > 4 (True)
  + right_beggining = palabra.startswith("p") (False)
  + min_ys = palabra.count("y") >= 1 (False)
  + is_cool_word = any([enough_letter, right_beggining, min_ys]) == True
  + is_cool_word2 = all([enough_letter, right_beggining, min_ys]) == False
  + Para la veracidad multiple lo que se hace es comprobar varios elementos booleanos con las funcionaes **any** y **all**, any es True desde que uno de ellos los sea, en cambio en all tienen que ser todos los elementos True para que sea True esa condición.
+ Listas por comprensión:
  + prueba = [str(i) for i in prueba]: Convierte todos los elementos de prueba en strings
  + prueba2 = [str(j) for j in prueba2 if j > 4]: Convierte todos los elementos de prueba2 en strings solo si son mayores que 4.
+ sum(prueba): Devuelve la suma de todos los elementos de prueba.
+ min(prueba): Devuelve el elemento más pequeño de todos los elementos de prueba.
+ max(prueba): Devuelve el elemento más grande de todos los elementos de prueba.