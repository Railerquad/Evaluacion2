import requests
import random
import string

API_URL = "http://localhost:5000/api/v1/books"

autores = ["Juan_Uribe", "Carlos_Soto", "Maria_Perez", "Andrea_Rojas"]
palabras = ["Redes", "Ciberseguridad", "Python", "APIs", "Routing", "Switching", "Cloud"]

def generar_isbn():
    return "".join(random.choices(string.digits, k=9))

def agregar_50_libros():
    print("--- Agregando 50 libros aleatorios a la biblioteca ---")
    for i in range(1, 51):
        libro_id = 7 + i
        titulo = f"{random.choice(palabras)} {random.choice(palabras)} Vol. {i}"
        autor = random.choice(autores)
        isbn = generar_isbn()

        payload = {
            "id": libro_id,
            "titulo": titulo,
            "autor": autor,
            "isbn": isbn
        }

        res = requests.post(API_URL, json=payload)
        if res.status_code in [200, 201]:
            print(f"[{i}/50] Libro ID {libro_id} agregado con éxito.")

def listar_todo():
    print("\n--- Listando la totalidad de los libros creados ---")
    res = requests.get(API_URL)
    if res.status_code == 200:
        libros = res.json()
        print(f"Total de libros en el catálogo: {len(libros)}\n")
        for l in libros:
            print(f"ID: {l.get('id')} | Título: {l.get('titulo')} | Autor: {l.get('autor')} | ISBN: {l.get('isbn')}")

if __name__ == "__main__":
    agregar_50_libros()
    listar_todo()
