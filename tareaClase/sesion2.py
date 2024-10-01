import random as rd

class Sesion2:
    def __init__(self):
        self.vector = []
        self.matriz = []
        
    def llenarVector(self, tamano):
        for _ in range(tamano):
            n = int(input("Ingrese el numero: "))
            self.vector.append(n)
            
        self.vector.reverse()            
        
    def imprimirVector(self, objeto):
        print(objeto)

    def imprimirMatriz(self, matriz):
        for fila in matriz:
            print(fila)

    #Invierta un vector de tamaño n
    def ejercicio1(self):
        n = int(input("Ingrese el tamaño del vector: "))
        self.llenarVector(n)
        self.imprimir()
    
    #Hallar el elemento mayor y mostrar sus posicion
    def ejercicio2(self):
        self.ejercicio1()
        valor_max = max(self.vector)     
        for i, value in enumerate(self.vector):
            if(value == valor_max):
                posicion = i
                break 
        print(f"Valor máximo: {valor_max}\nPosición: {posicion}")        
    
    #Hallar el elemento menor y mostrar sus posicion       
    def ejercicio3(self):
        self.ejercicio1()
        valor_min = min(self.vector)     
        for i, value in enumerate(self.vector):
            if(value == valor_min):
                posicion = i
                break 
        print(f"Valor minimo: {valor_min}\nPosición: {posicion}")        
            
    #Llenar una matriz con los nombres y edades de n personas            
    def ejercicio4(self):
        n = int(input("Ingrese la cantidad de personas: "))
        for _ in range(n):
            nombre = input("Ingrese el nombre: ")
            edad = int(input("Ingrese la edad: "))
            self.matriz.append((nombre, edad))
        self.matriz.sort(key=lambda x:x[1])     
        print("Matriz Ordenada") 
        self.imprimir(self.matriz)        
                          
    #Ejercicio
    def ejercicio5(self):
        print("Matriz random")
        for _ in range(3):
            fila = []
            for _ in range(3):
                numeroRandom = rd.randint(0, 100)
                fila.append(numeroRandom) 
            self.matriz.append(fila)   
            
        self.imprimirMatriz(self.matriz)  

        valor_n_mayor = 0
        posicion = 0
               
        for i, fila in enumerate(self.matriz):
            for j, value in enumerate(fila):
                if value > valor_n_mayor:
                    valor_n_mayor = value
                    posicion = (i, j)
                    break 
        
        print(posicion)
                    
        for k in range(3):
            self.vector.append(self.matriz[k][k])
            
        self.imprimirVector(self.vector)   
        
         
            
if __name__ == "__main__":        
    sesion2 = Sesion2()
    sesion2.ejercicio5()
         