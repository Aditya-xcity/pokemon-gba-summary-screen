from flask import Flask, render_template, jsonify

from data.pokemon_constants import (
    pokemonNicknames,
    pokemonIdMap,
    POKEMON_ABILITIES,
    trainerMemo
)

from data.reference import POKEMON_IMAGES, POKEMON_CRY
from data.pokemon_moves_fire_red import (
    CHARIZARD_MOVES,
    BLASTOISE_MOVES,
    NIDOKING_MOVES,
    VENUSAUR_MOVES,
    ALAKAZAM_MOVES,
    PIKACHU_MOVES
)

app = Flask(__name__)


def build_pokemon(name, dex, moves):
    key = name.lower()

    return {
        "name": name.capitalize(),
        "dex": dex,
        "nickname": pokemonNicknames[key],
        "trainer": "adi",
        "id_number": pokemonIdMap[key],
        "level": 50,
        "item": "None",

        "trainer_memo": trainerMemo[key]["trainer_memo"],

        "type1": moves[0].type if moves else "None",
        "type2": None,

        "ability": POKEMON_ABILITIES[key]["ability"],
        "ability_desc": POKEMON_ABILITIES[key]["description"],

        "image": f"/static/Images/{POKEMON_IMAGES[key]}",
        "cry": f"/static/sound/{POKEMON_CRY[key]}",

        "stats": {
            "hp": 150,
            "attack": 120,
            "defence": 100,
            "sp_atk": 140,
            "speed": 120
        },

        "moves": [
            {
                "name": m.name,
                "power": m.power,
                "accuracy": m.accuracy,
                "pp": m.pp,
                "description": m.description,
                "effect": m.in_game_effect
            }
            for m in moves
        ]
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/pokemon")
def api_pokemon():
    return jsonify([
        build_pokemon("charizard", 6, CHARIZARD_MOVES),
        build_pokemon("blastoise", 9, BLASTOISE_MOVES),
        build_pokemon("nidoking", 34, NIDOKING_MOVES),
        build_pokemon("venusaur", 3, VENUSAUR_MOVES),
        build_pokemon("alakazam", 65, ALAKAZAM_MOVES),
        build_pokemon("pikachu", 25, PIKACHU_MOVES),
    ])


if __name__ == "__main__":
    app.run(debug=True)
