
inscripciones = []

while True:
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    Ciudad_origen = input("Ingrese su ciudad de origen: ")
    Ins_Videojuego = input("Ingrese el videojuego al que desea inscribirse: \n 1.Fornite  \n 2.League of Legends  \n 3.Valorant \n")

    

    inscripcion = {
        'Nombre': nombre,
        'Apellido': apellido,
        'Ciudad de Origen': Ciudad_origen,
        'Videojuego': Ins_Videojuego
    }

    inscripciones.append(inscripcion)

    
    continuar =input("¿Desea agregar otra inscripcion? (si/no)")
    if continuar == "no":
        break

for inscripcion in inscripciones:
    print(inscripcion)

archivo = open("inscripciones.doxc", "w")

for inscripcion in inscripciones:
    archivo.write(f"Nombre: {inscripcion['Nombre']}\n")
    archivo.write(f"Apellido: {inscripcion['Apellido']}\n")
    archivo.write(f"Ciudad de Origen: {inscripcion['Ciudad de Origen']}\n")
    archivo.write(f"Videojuego: {inscripcion['Videojuego']}\n")
    archivo.write('\n')  # Agregar una línea en blanco entre inscripciones

# Cerrar el archivo para guardar los cambios
archivo.close()

print("Inscripciones guardadas en 'inscripciones.doxc'.")