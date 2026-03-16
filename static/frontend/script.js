// ================= AUDIO =================
const clickSound = new Audio("/static/sound/blip.wav");
clickSound.volume = 0.6;

let cryAudio = null;

function playClick() {
    clickSound.currentTime = 0;
    clickSound.play();
}

function playCry(src) {
    if (cryAudio) {
        cryAudio.pause();
        cryAudio.currentTime = 0;
    }
    cryAudio = new Audio(src);
    cryAudio.play();
}

// ================= JUMP ANIMATION =================
function jump(element) {
    if (!element) return;
    element.classList.remove("jump");
    void element.offsetWidth; // force reflow
    element.classList.add("jump");
}

// ================= STAT BOX =================
function statBox(label, value) {
    return `
        <div class="stat-box">
            <div class="stat-label">${label}</div>
            <div class="stat-value">${value}</div>
        </div>
    `;
}

// ================= STATE =================
let pokemons = [];
let pIndex = 0;
let card = 1;       // 1 = INFO, 2 = SKILLS, 3 = MOVES
let moveIndex = 0;

// ================= FETCH DATA =================
fetch("/api/pokemon")
    .then(res => res.json())
    .then(data => {
        pokemons = data;
        loadPokemon();
        render();
    });

// ================= LOAD POKÉMON =================
function loadPokemon() {
    const p = pokemons[pIndex];

    pokemonName.textContent = p.name;
    pokemonLevel.textContent = "Lv " + p.level;
    pokemonImage.src = p.image;

    moveIndex = 0;

    playCry(p.cry);

    // 🔥 Jump effects
    jump(pokemonImage);
    jump(pokemonName);
}

// ================= RENDER UI =================
function render() {
    const p = pokemons[pIndex];

    // ---------- INFO ----------
    infoDex.textContent = p.dex;
    infoNickname.textContent = p.nickname;
    infoOT.textContent = p.trainer;
    infoId.textContent = p.id_number;
    infoItem.textContent = p.item;
    infoType.textContent = p.type1 + (p.type2 ? " · " + p.type2 : "");

    // ---------- STATS (BOXED) ----------
    statsContainer.innerHTML = `
        <div class="stats-grid">
            ${statBox("HP", p.stats.hp)}
            ${statBox("ATK", p.stats.attack)}
            ${statBox("DEF", p.stats.defence)}
            ${statBox("SPA", p.stats.sp_atk)}
            ${statBox("SPD", p.stats.speed)}
        </div>
    `;

    skillAbility.textContent = p.ability;

    // ---------- MOVES ----------
    moveList.innerHTML = p.moves.map((m, i) =>
        `<div class="move ${i === moveIndex ? "selected" : ""}">${m.name}</div>`
    ).join("");

    // ---------- DESCRIPTION PANEL ----------
    if (card === 3) {
        const m = p.moves[moveIndex];
        spriteDescription.innerHTML = `
            <b>${m.name}</b><br>
            ${m.description}
            ${m.effect ? `<br><em>${m.effect}</em>` : ""}
        `;
        jump(spriteDescription);
    }
    else if (card === 2) {
        spriteDescription.innerHTML = `
            <b>Ability: ${p.ability}</b><br>
            ${p.ability_desc}
        `;
        jump(spriteDescription);
    }
    else {
        spriteDescription.innerHTML = `
            <b>Trainer Memo</b><br>
            ${p.trainer_memo.replace(/\n/g, "<br>")}
        `;
        jump(spriteDescription);
    }

    // ---------- BOARD SWITCH ----------
    infoBoard.classList.toggle("active", card === 1);
    skillsBoard.classList.toggle("active", card === 2);
    movesBoard.classList.toggle("active", card === 3);

    cardLabel.textContent = ["INFO", "SKILLS", "MOVES"][card - 1];
    uiBoard.src = `/static/Images/boards/board_${cardLabel.textContent.toLowerCase()}.png`;
}

// ================= KEYBOARD CONTROLS =================
document.addEventListener("keydown", e => {
    playClick();

    // MOVE SELECTION (MOVES CARD)
    if (card === 3 && (e.key === "ArrowUp" || e.key === "ArrowDown")) {
        const total = pokemons[pIndex].moves.length;
        moveIndex = (moveIndex + (e.key === "ArrowDown" ? 1 : -1) + total) % total;
        render();
        return;
    }

    switch (e.key) {
        case "ArrowUp":
            pIndex = (pIndex + 1) % pokemons.length;
            loadPokemon();
            render();
            break;

        case "ArrowDown":
            pIndex = (pIndex - 1 + pokemons.length) % pokemons.length;
            loadPokemon();
            render();
            break;

        case "ArrowLeft":
            card = card === 1 ? 3 : card - 1;
            render();
            break;

        case "ArrowRight":
            card = card === 3 ? 1 : card + 1;
            render();
            break;

        case "Enter":
        case "z":
            playCry(pokemons[pIndex].cry);
            jump(pokemonImage);
            break;
    }
});
