import time
import random
from metodo_ordenamiento import MetodoOrdenamiento
class Benchmarking:
    
    def __init__(self):
        print("BenchMarking instanciado")
    def medir_tiempo(self,funcion,arreglo):
        inicio= time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio
        
        
        
        #mO = MetodoOrdenamiento()
        #arreglo = self.build_arregglo(10000)
        #tareaB = lambda: self.mO.sort_bubble(arreglo)
        #tareaBM = lambda: self.mO.sort_burbuja_mejorado_optimixado(arreglo)
        #tareaSe = lambda: self.mO.sort_seleccion(arreglo)
        #tareaSh = lambda: self.mO.sort_shell(arreglo)
        
        
        #tiempoN = self.contar_con_nano_time_(tareaB)
        #tiempoN1 = self.contar_con_nano_time_(tareaBM)
        #tiempoN2 = self.contar_con_nano_time_(tareaSe)
        #tiempoN3 = self.contar_con_nano_time_(tareaSh)
        
        #print(f"Tiempo en nanosegundos burbuja {tiempoN}")
        #print(f"Tiempo en nanosegundos burbuja mejorado {tiempoN1}")
        #print(f"Tiempo en nanosegundos seleccion {tiempoN2}")
        #print(f"Tiempo en nanosegundos shell {tiempoN3}")
        
     
        
        
    
    def build_arregglo(self,tamanio):
        arreglo = []
        for i in range (tamanio):
            numero = random.randint(0,99999) #si incluye el ultimo numero
            arreglo.append(numero)
        return arreglo    
    #import time
    #milisegundo en segundos con # x = time.time()
    #nanosegundo con # x = time.time_ns()
    #ejecutar es tarea()
    
    def contar_con_current_time_milles(self,tarea):
        inicio = time.time ()
        tarea()
        fin = time.time ()
        tiempo_segundos = fin - inicio
        return(tiempo_segundos)
        
       
    def contar_con_nano_time_(self,tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        tiempo_segundos = (fin - inicio) / 1_000_000_000.0
        return (tiempo_segundos) 
    
        