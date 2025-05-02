import bechmarking as bm
#from bechmarking import Benchmarking
from metodo_ordenamiento import MetodoOrdenamiento
# Archivo pricipal
if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodoOrdenamiento()
    
    
    ##tam = 1000
    tamanios = [5000,10000,20000]
    ##resultados=[]
    #arreglo_base = bench.build_arregglo(tamanios)
    for tam in tamanios:
        arrreglo_base = bench.build_arregglo(tamanios)
       
    
    
    key = "burbuja",
    value = metodosO.sort_bubble
    
    metodos_dic = {
        "burbuja": metodosO.sort_bubble,
        "burbuja mejorado":metodosO.sort_burbuja_mejorado_optimizado,
        "seleccion": metodosO.sort_seleccion,
        "shell": metodosO.sort_shell
    }
    resultados =[]
    for nombre, metodo_funcion in metodos_dic.items():
            
            tiempo_resultado = bench.contar_con_nano_time_(lambda: metodo_funcion(arrreglo_base))
            
            tupla_resultado = (tamanios, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)
   # for nombre, metodo_funcion in metodos_dic.items():
   #     tiempo_resultado = bench.contar_con_nano_time_(metodo_funcion,arreglo_base)
   #    tupla_resultado = (tamanios,nombre,tiempo_resultado)
   #    resultados.append(tupla_resultado)
    for tamanios ,nombre ,tiempo  in resultados:
        print(f"Tamaño:{tamanios},nombre_metodo:{nombre},tiempo:{tiempo:.6f},segundos")
    