from matplotlib import pyplot as plt
import benchmarking as bm
#from bechmarking import Benchmarking
from metodo_ordenamiento import MetodoOrdenamiento
# Archivo pricipal
if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodoOrdenamiento()
    
    
    ##tam = 1000
    tamanios = [50,100,200]
    resultados= []
    ##resultados=[]
    #arreglo_base = bench.build_arregglo(tamanios)
    ##key = "burbuja",
    ##value = metodosO.sort_bubble
    metodos_dic = {
        "burbuja": metodosO.sort_bubble,
        "burbuja mejorado":metodosO.sort_burbuja_mejorado_optimizado,
        "seleccion": metodosO.sort_seleccion,
        "shell": metodosO.sort_shell
    }
    tiempos_by_metodo ={nombre:[]for nombre in metodos_dic.keys()}
    for tam in tamanios:
        arreglo_base = bench.build_arregglo(tam)
        for nombre, metodo_funcion in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(metodo_funcion,arreglo_base.copy())
            resultados.append((tam,nombre,tiempo_resultado)) 
            tiempos_by_metodo[nombre].append(tiempo_resultado)
    for tam , nombre , tiempo_resultado in resultados:
        print(f"-Tamaño-:{tam} , --Nombre Metodo--:{nombre},-Tiempo-:{tiempo_resultado: .6f}segundos")       
   # for nombre, metodo_funcion in metodos_dic.items():
   #     tiempo_resultado = bench.contar_con_nano_time_(metodo_funcion,arreglo_base)
   #    tupla_resultado = (tamanios,nombre,tiempo_resultado)
   #    resultados.append(tupla_resultado)
   #     print(f"Tamaño:{tamanios},nombre_metodo:{nombre},tiempo:{tiempo:.6f},segundos")
   #Preparar datos para ser graficado
   #Crear un diciconario o mapa para almacenar resultados por metodos
    tiempos_by_metodo = {
       "burbuja":[],
       "burbuja mejorado":[],
       "seleccion":[],
       "shell": [] ,
       }
    
    for tam,nombre,tiempo in resultados: 
        tiempos_by_metodo[nombre].append(tiempo)
        
    plt.figure(figsize=(10,6))
    
    for nombre,tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios,tiempos,label= nombre, marker="s")
        
    plt.title("Comparacion de tiempo para cada metodod de ordenamiento")
    plt.xlabel("Tamaño de los arreglos")
    plt.ylabel("Tiempo de ejecucion (s)")    
    plt.legend()
    plt.grid(True)
    plt.show()