secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

number = int(input("Introduce un número entero: "))

while number != 777:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!") 
    
    number = int(input("Introduce un número entero: "))
    
else:
    print(secret_number, "¡Bien hecho, muggle! Eres libre ahora")