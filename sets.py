
# sets
# no guarda ningun orden

planetas = {"Marte", "Venus", "Júpiter"}
print(planetas)
print(len(planetas))

# revisar si un elemento esta presente
print("Marte" in planetas)

# agregar elementos
planetas.add("Tierra")
print(planetas)

# no soporta duplicados
planetas.add("Tierra")
print(planetas)

# eliminar un elemento - arroja error si no existe
planetas.remove("Tierra")
print(planetas)

# discard elimina sin arrojar error
planetas.discard("Jupiter")
print(planetas)

# limpiar set
planetas.clear()
print(planetas)

# eliminar set
del planetas
#print(planetas)
