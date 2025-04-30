import time
import random
from metodo_ordenamiento import MetodoOrdenamiento
class Benchmarking:
    
    def __init__(self):
        print("BenchMarking instanciado")
        mO = MetodoOrdenamiento()
        arreglo = self.build_arregglo(10000)
        tareaB = lambda: self.mO.sort_bubble(arreglo)
        tareaBM = lambda: self.mO.sort_burbuja_mejorado_optimixado(arreglo)
        tareaS = lambda: self.mO.sort_seleccion(arreglo)
        tiempoM = self.contar_con_current_time_milles(tarea)
        tiempoN = self.contar_con_nano_time_(tarea)
        
        print(f"tiempo en milisegundos:{tiempoM * 1000} ms")
        print(f"tiempo en milisegundos:{tiempoN * 1_000_000_000.0} ns")
        
        
        
    
    def build_arregglo(self,tamano):
        arreglo = []
        for i in range (tamano):
            numero = random.randint(0,9999) #si incluye el ultimo numero
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
        return(fin-inicio)
        
       
    def contar_con_nano_time_(self,tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return ( fin - inicio) / 1_000_000_000.0
        