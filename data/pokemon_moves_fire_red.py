# pokemon_moves_fire_red.py
# Contains move data for FireRed/LeafGreen Pokémon teams
# Gen III mechanics: Physical/Special based on type

class Move:
    """Represents a Pokémon move with Gen III attributes"""
    def __init__(self, name, move_type, category, power, accuracy, pp, description, in_game_effect=None):
        self.name = name
        self.type = move_type  # Fire, Water, etc.
        self.category = category  # "Physical", "Special", or "Status"
        self.power = power  # None for status moves
        self.accuracy = accuracy  # Percentage (0-100) or None for always-hit moves
        self.pp = pp  # Power Points
        self.description = description
        self.in_game_effect = in_game_effect  # Additional effects like "May burn"
    
    def __str__(self):
        if self.category == "Status":
            return f"{self.name} ({self.type}) - {self.category} - Acc: {self.accuracy or 'N/A'}% - PP: {self.pp}"
        else:
            return f"{self.name} ({self.type}) - {self.category} - Power: {self.power} - Acc: {self.accuracy or 'N/A'}% - PP: {self.pp}"

# ===== CHARIZARD'S MOVES =====
CHARIZARD_MOVES = [
    Move("Flamethrower", "Fire", "Special", 95, 100, 15, 
         "A powerful fire attack that may inflict a burn.", "10% burn chance"),
    
    Move("Wing Attack", "Flying", "Physical", 60, 100, 35,
         "Strikes the foe with wings.", None),
    
    Move("Fly", "Flying", "Physical", 70, 95, 15,
         "Flies up on turn 1, strikes turn 2. Can be used outside of battle to fly to any visited town.",
         "Two-turn move, evades first turn"),
    
    Move("Dragon Rage", "Dragon", "Special", None, 100, 10,
         "Inflicts exactly 40 HP damage regardless of type or stats.", "Always does 40 damage")
]

# ===== BLASTOISE'S MOVES =====
BLASTOISE_MOVES = [
    Move("Hydro Pump", "Water", "Special", 120, 80, 5,
         "Blasts water at high power.", None),
    
    Move("Surf", "Water", "Special", 95, 100, 15,
         "A wave hits all Pokémon in battle. Can be used outside of battle to travel across water.",
         "Hits all adjacent foes in double battles"),
    
    Move("Ice Beam", "Ice", "Special", 95, 100, 10,
         "Blasts the foe with an icy beam. May freeze it.", "10% freeze chance"),
    
    Move("Bite", "Dark", "Physical", 60, 100, 25,
         "Bites with vicious fangs. May cause flinching.", "30% flinch chance")
]

# ===== NIDOKING'S MOVES =====
NIDOKING_MOVES = [
    Move("Earthquake", "Ground", "Physical", 100, 100, 10,
         "A powerful quake, but has no effect on flying foes.", "Hits all adjacent Pokémon"),
    
    Move("Thunderbolt", "Electric", "Special", 95, 100, 15,
         "A strong electrical attack that may cause paralysis.", "10% paralysis chance"),
    
    Move("Ice Beam", "Ice", "Special", 95, 100, 10,
         "Blasts the foe with an icy beam. May freeze it.", "10% freeze chance"),
    
    Move("Slash", "Normal", "Physical", 70, 100, 20,
         "Slashes with claws, etc. Has a high critical-hit ratio.", "High crit ratio (12.5%)")
]

# ===== VENUSAUR'S MOVES =====
VENUSAUR_MOVES = [
    Move("Solar Beam", "Grass", "Special", 120, 100, 10,
         "Absorbs light on turn 1, attacks on turn 2. Instant in sunny weather.",
         "Two-turn move unless sun is active"),
    
    Move("Earthquake", "Ground", "Physical", 100, 100, 10,
         "A powerful quake, but has no effect on flying foes.", "Hits all adjacent Pokémon"),
    
    Move("Bite", "Dark", "Physical", 60, 100, 25,
         "Bites with vicious fangs. May cause flinching.", "30% flinch chance"),
    
    Move("Slash", "Normal", "Physical", 70, 100, 20,
         "Slashes with claws, etc. Has a high critical-hit ratio.", "High crit ratio (12.5%)")
]

# ===== ALAKAZAM'S MOVES =====
ALAKAZAM_MOVES = [
    Move("Psychic", "Psychic", "Special", 90, 100, 10,
         "A powerful psychic attack that may lower the foe's Special Defense.", "10% chance to lower Sp. Def by 1 stage"),
    
    Move("Thunderbolt", "Electric", "Special", 95, 100, 15,
         "A strong electrical attack that may cause paralysis.", "10% paralysis chance"),
    
    Move("Ice Beam", "Ice", "Special", 95, 100, 10,
         "Blasts the foe with an icy beam. May freeze it.", "10% freeze chance"),
    
    Move("Slash", "Normal", "Physical", 70, 100, 20,
         "Slashes with claws, etc. Has a high critical-hit ratio.", "High crit ratio (12.5%)")
]

# ===== PIKACHU'S MOVES (Note: Pikachu cannot normally learn Fly or Slash in Gen III) =====
PIKACHU_MOVES = [
    Move("Thunderbolt", "Electric", "Special", 95, 100, 15,
         "A strong electrical attack that may cause paralysis.", "10% paralysis chance"),
    
    Move("Slash", "Normal", "Physical", 70, 100, 20,
         "Slashes with claws, etc. Has a high critical-hit ratio.", "High crit ratio (12.5%)"),
    
    Move("Bite", "Dark", "Physical", 60, 100, 25,
         "Bites with vicious fangs. May cause flinching.", "30% flinch chance"),
    
    Move("Fly", "Flying", "Physical", 70, 95, 15,
         "Flies up on turn 1, strikes turn 2. Can be used outside of battle to fly to any visited town.",
         "Two-turn move, evades first turn")
]

# ===== POKÉMON CLASSES =====
class Pokemon:
    """Represents a Pokémon with its moveset"""
    def __init__(self, name, moves_list):
        self.name = name
        self.moves = moves_list
    
    def display_moveset(self):
        """Prints the Pokémon's name and all its moves"""
        print(f"\n{'='*50}")
        print(f"{self.name.upper()}")
        print(f"{'='*50}")
        for i, move in enumerate(self.moves, 1):
            print(f"{i}. {move}")
            print(f"   Description: {move.description}")
            if move.in_game_effect:
                print(f"   Effect: {move.in_game_effect}")
        print()

# ===== CREATE POKÉMON INSTANCES =====
charizard = Pokemon("Charizard", CHARIZARD_MOVES)
blastoise = Pokemon("Blastoise", BLASTOISE_MOVES)
nidoking = Pokemon("Nidoking", NIDOKING_MOVES)
venusaur = Pokemon("Venusaur", VENUSAUR_MOVES)
alakazam = Pokemon("Alakazam", ALAKAZAM_MOVES)
pikachu = Pokemon("Pikachu", PIKACHU_MOVES)

# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("POKÉMON FIRERED/LEAFGREEN TEAM MOVESETS")
    print("=" * 50)
    print("Note: Pikachu cannot normally learn Fly or Slash in Gen III")
    print("These moves would require special conditions or hacking.")
    print("=" * 50)
    
    # Display all Pokémon movesets
    pokemon_team = [charizard, blastoise, nidoking, venusaur, alakazam, pikachu]
    
    for pokemon in pokemon_team:
        pokemon.display_moveset()
    
    # Example usage: Check type effectiveness
    print("\nType Effectiveness Example:")
    print("-" * 30)
    
    # Show which moves are super effective against Charizard
    target_type = ["Fire", "Flying"]  # Charizard's types
    super_effective_types = {
        "Fire": ["Water", "Rock", "Ground"],
        "Flying": ["Electric", "Ice", "Rock"]
    }
    
    print(f"Moves super effective against {pokemon_team[0].name}:")
    for pokemon in pokemon_team:
        for move in pokemon.moves:
            if (move.type in super_effective_types.get("Fire", []) or 
                move.type in super_effective_types.get("Flying", [])):
                print(f"  {pokemon.name}'s {move.name} ({move.type})")

# ===== ADDITIONAL UTILITY FUNCTIONS =====
def get_move_by_name(move_name):
    """Search for a move by name across all Pokémon"""
    all_moves = []
    for pokemon in [charizard, blastoise, nidoking, venusaur, alakazam, pikachu]:
        all_moves.extend(pokemon.moves)
    
    for move in all_moves:
        if move.name.lower() == move_name.lower():
            return move
    return None

def get_pokemon_with_move(move_name):
    """Find which Pokémon have a specific move"""
    pokemon_with_move = []
    for pokemon in [charizard, blastoise, nidoking, venusaur, alakazam, pikachu]:
        for move in pokemon.moves:
            if move.name.lower() == move_name.lower():
                pokemon_with_move.append(pokemon.name)
                break
    return pokemon_with_move

# Export all moves for easy importing
ALL_MOVES = {
    "Flamethrower": CHARIZARD_MOVES[0],
    "Wing Attack": CHARIZARD_MOVES[1],
    "Fly": CHARIZARD_MOVES[2],
    "Dragon Rage": CHARIZARD_MOVES[3],
    "Hydro Pump": BLASTOISE_MOVES[0],
    "Surf": BLASTOISE_MOVES[1],
    "Ice Beam": BLASTOISE_MOVES[2],
    "Bite": BLASTOISE_MOVES[3],
    "Earthquake": NIDOKING_MOVES[0],
    "Thunderbolt": NIDOKING_MOVES[1],
    "Ice Beam (Nidoking)": NIDOKING_MOVES[2],
    "Slash (Nidoking)": NIDOKING_MOVES[3],
    "Solar Beam": VENUSAUR_MOVES[0],
    "Earthquake (Venusaur)": VENUSAUR_MOVES[1],
    "Bite (Venusaur)": VENUSAUR_MOVES[2],
    "Slash (Venusaur)": VENUSAUR_MOVES[3],
    "Psychic": ALAKAZAM_MOVES[0],
    "Thunderbolt (Alakazam)": ALAKAZAM_MOVES[1],
    "Ice Beam (Alakazam)": ALAKAZAM_MOVES[2],
    "Slash (Alakazam)": ALAKAZAM_MOVES[3],
    "Thunderbolt (Pikachu)": PIKACHU_MOVES[0],
    "Slash (Pikachu)": PIKACHU_MOVES[1],
    "Bite (Pikachu)": PIKACHU_MOVES[2],
    "Fly (Pikachu)": PIKACHU_MOVES[3]
}