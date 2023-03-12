celular1 = {
    'Categoria': 'Celulares',
    'Modelo': 'Samsung S23 Ultra',
    'Precio': '31,000'
}

celular2 = {
    'Categoria': 'Celulares',
    'Modelo': 'iPhone 14 Pro Max',
    'Precio': '31,000'
}

del celular1

del celular2["Categoria"]
celular2.pop("Precio")
print(celular2)

for x, y in celular2.items():
    print(x, ": ", y)