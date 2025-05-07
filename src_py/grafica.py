import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]
# Crear grafico de lineas
plt.plot(x, y, label = "Linea", color= "blue")
#Agrgar parametros
plt.title("Mi primer grafico")
plt.xlabel("Eje de la x")
plt.ylabel("Eje de las y")

plt.legend()
plt.grid(True)

plt.show()
