import java.util.Random;

public class Benchmarking {
    
    private MetodosOrdenamiento mOrdenamiento;
    
    public  Benchmarking(){

        long currentMills = System.currentTimeMillis();
        
        long currentNano = System.nanoTime();

        System.out.println(currentMills);
        System.out.println(currentNano);

        mOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(1000000);
        Runnable tarea =() -> mOrdenamiento.burbujaTradicional(arreglo);

        double tiempoDuracionMillis = medirConCurrentTimeMills(tarea);
        double tiempoDuracionNano = medirConNanoTime(tarea);

        System.out.println("tiempo en milisegundos: "+ tiempoDuracionMillis);
        System.out.println("tiempo en nanosegundos: "+ tiempoDuracionNano);



    }
    private int [] generarArregloAleatorio(int tamano){
        int[] array = new int[tamano];
        Random random = new Random();
        for(int i = 0 ;i < tamano;i++){
            array[i]=random.nextInt(1000000);

        }
        return array;
    }
    public double medirConCurrentTimeMills(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 10000.0;
        return tiempoSegundos;
    }
    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }
   
    
}
