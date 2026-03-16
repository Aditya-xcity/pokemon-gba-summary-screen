from models.attack import Attack
from models.card1 import Card1
from models.card2 import Card2
from models.card3 import Card3
from models.pokemon import Pokemon


# ================= MOVES =================
flamethrower = Attack("Flamethrower", 90, 100, "Burns the target", 15)
wing_attack  = Attack("Wing Attack", 60, 100, "Flying attack", 35)
fly_move     = Attack("Fly", 90, 95, "Two-turn attack", 15)
dragon_rage  = Attack("Dragon Rage", 0, 100, "Fixed damage", 10)

hydro_pump = Attack("Hydro Pump", 110, 80, "Water blast", 5)
surf       = Attack("Surf", 90, 100, "Hits all Pokémon", 15)
ice_beam   = Attack("Ice Beam", 90, 100, "May freeze", 10)
bite       = Attack("Bite", 60, 100, "May cause flinch", 25)

earthquake  = Attack("Earthquake", 100, 100, "Ground shock", 10)
thunderbolt = Attack("Thunderbolt", 90, 100, "Electric blast", 15)
solar_beam  = Attack("Solar Beam", 120, 100, "Charges then attacks", 10)
psychic     = Attack("Psychic", 90, 100, "Psychic force", 10)
slash       = Attack("Slash", 70, 100, "High critical ratio", 20)


# ================= POKÉMON LIST (ONLY 6) =================
POKEMONS = [

    # 🔥 CHARIZARD
    Pokemon(
        Card1(6, "Charizard", "Fire", "Flying", 72, "Lonely", "Leftovers"),
        Card2(216, 187, 135, 185, 195, "Blaze", 381083, 12962),
        Card3(flamethrower, wing_attack, fly_move, dragon_rage)
    ),

    # 💧 BLASTOISE
    Pokemon(
        Card1(9, "Blastoise", "Water", None, 70, "Bold", "Mystic Water"),
        Card2(218, 170, 200, 175, 150, "Torrent", 365000, 12000),
        Card3(hydro_pump, surf, ice_beam, bite)
    ),

    # 🐊 NIDOKING
    Pokemon(
        Card1(34, "Nidoking", "Poison", "Ground", 48, "Adamant", "Soft Sand"),
        Card2(162, 140, 100, 110, 112, "Poison Point", 115000, 49),
        Card3(earthquake, thunderbolt, ice_beam, slash)
    ),

    # 🌿 VENUSAUR
    Pokemon(
        Card1(3, "Venusaur", "Grass", "Poison", 50, "Calm", "Miracle Seed"),
        Card2(160, 100, 120, 140, 100, "Overgrow", 119000, 51),
        Card3(solar_beam, earthquake, bite, slash)
    ),

    # 🧠 ALAKAZAM
    Pokemon(
        Card1(65, "Alakazam", "Psychic", None, 50, "Timid", "Twisted Spoon"),
        Card2(135, 85, 75, 175, 150, "Synchronize", 130000, 51),
        Card3(psychic, thunderbolt, ice_beam, slash)
    ),

    # ⚡ PIKACHU
    Pokemon(
        Card1(25, "Pikachu", "Electric", None, 45, "Jolly", "Light Ball"),
        Card2(120, 90, 60, 95, 130, "Static", 90000, 46),
        Card3(thunderbolt, slash, bite, fly_move)
    )
]
