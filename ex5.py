import requests

def pex5():
    for i in range(30):
        a = "https://pokeapi.co/api/v2/pokemon/" + str((i+1))
        res = requests.get(a)
        if res.status_code == 200:
            dades = res.json()
            nombre = dades["name"]
            tipos = [tipo["type"]["name"] for tipo in dades["types"]]
            print("El nom del pokémon és: {}".format(nombre))
            print("El seu tipus és: {}".format(", ".join(tipos)))
        else:
            print("No hi ha dades.")
            

