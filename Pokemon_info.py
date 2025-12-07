import requests, random
API = "https://pokeapi.co/api/v2/"

def getPokemonInfo(Name):
    url = f"{API}/pokemon/{Name}"
    response = requests.get(url)
    if response.status_code == 200:
        Pokemondata = response.json()
        return Pokemondata
    else:
        print("No data found")

Pokemon_name = input("Enter your Pokemon name : ").lower()
Pokemon_info = getPokemonInfo(Pokemon_name)
if not Pokemon_info:
    print("That's not a Pokemon")
    exit()
all_moves = Pokemon_info.get("moves", [])
if len(all_moves) >= 4:
    random_moves = random.sample(all_moves, 4)
else:
    random_moves = all_moves
move_names = [m['move']['name'] for m in random_moves]

Pokemon_info = getPokemonInfo(Pokemon_name)
all_abilities = Pokemon_info.get("abilities", [])
if len(all_abilities) >= 2:
    random_ability = random.sample(all_abilities, 2)
else:
    random_ability = all_abilities
all_abilities = [a['ability']['name'] for a in all_abilities]

if Pokemon_info:
    print(f"Name   : {Pokemon_info["name"].capitalize()}")
    print(f"Id     : {Pokemon_info["id"]}")
    print(f"Height : {Pokemon_info["height"]/10}")
    print(f"Weight : {Pokemon_info["weight"]/10}")
    move_names = [m['move']['name'] for m in random_moves]
    print(f"Moves : {move_names}")  
    print(f"Abilities : {all_abilities}")


