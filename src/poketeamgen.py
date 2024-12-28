from bs4 import BeautifulSoup
import requests
import random

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_National_Pokédex_number"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

pokemon_db = []

gens = soup.find_all("table", {"class": "roundy"})
for gen in gens:
    table = gen.find("tbody")
    all_pokemon = table.find_all("tr", {"style": "background:#FFF"})
    for pokemon in all_pokemon:
        info = pokemon.find_all("td")
        name = info[2].find("a").text
        pokemon_db.append(name)

print("Welcome to the pokemon team generator.")
while True:
    userinput = input("How many pokemon would you like on your team? ")
    try:
        numpokemon = int(userinput)
    except ValueError:
        ("Answer must be a number!")
        continue
    if numpokemon > 6 or numpokemon < 1 :
        print("Invalid number. Value must be between 1 and 6")
        continue
    print()
    for i in range(numpokemon):
        print(pokemon_db[random.randint(0, len(pokemon_db))])
    break

print("\nSuccess!")