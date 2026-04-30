# Se utiliza una tupla para asegurar que el orden sea inmutable en tiempo de ejecución
panama_division = (
    "Bocas del Toro", "Coclé", "Colón", "Chiriquí", "Darién", 
    "Herrera", "Los Santos", "Panamá", "Veraguas", "Panamá Oeste", 
    "Guna Yala", "Emberá-Wounaan", "Ngäbe-Buglé", "Madugandí", "Wargandí"
)

print("Listado oficial de Provincias y Comarcas (Orden Protegido):")
for lugar in panama_division:
    print(f"- {lugar}")