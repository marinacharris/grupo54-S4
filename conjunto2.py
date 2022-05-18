#operaciones de los conjuntos
# operadores    métodos                 descripción
# | (alt +124)  union                   Unión
# &             intersecction           Intersección
# -             difference              Diferencia
# ^             symmetric_difference    Diferencia simétrica

cultivosZonaA = {'papa', 'maíz', 'trigo'}
cultivosZonaB = {'plátano', 'maíz', 'caña'}

print(cultivosZonaA | cultivosZonaB)
print(cultivosZonaA.union(cultivosZonaB))
print(cultivosZonaA & cultivosZonaB)
print(cultivosZonaA.intersection(cultivosZonaB))
print(cultivosZonaA - cultivosZonaB)
print(cultivosZonaA ^ cultivosZonaB)
