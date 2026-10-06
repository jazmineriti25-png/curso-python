precio = 100
descuento = 0.15
precio_final = precio * (1 - descuento)

es_elegible = (precio_final > 50) and not (descuento == 0)

print(f"Precio con descuento: ${precio_final}")
print(f"¿Aplica a promoción?: {es_elegible}")