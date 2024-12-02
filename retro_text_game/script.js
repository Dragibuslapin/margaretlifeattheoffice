
const gameOutput = document.getElementById("game-output");
const gameInput = document.getElementById("game-input");

let typingSpeed = 50; // Speed of text animation
let gameState = 0; // Tracks the current state of the game

const scenes = [
    {
        text: "Nous sommes en 1980.\nMargaret est secrétaire d’une banque depuis plus de deux ans.\nElle a participé à la conception des ordinateurs UNIVAC I et l’IBM 650.\n\nVoulez-vous commencer le jeu ? (Oui/Non)",
        options: ["oui", "non"],
        nextScene: [1, -1],
    },
    {
        text: "(Vous êtes Margaret.)\nVous arrivez au bureau de la banque dans laquelle vous travaillez.\nComme à son habitude, votre chef passe à côté de vous et vous fait une remarque sur votre physique.\n\n1: Répondre poliment.\n2: Répliquer sèchement.",
        options: ["1", "2"],
        nextScene: [2, 3],
    },
    {
        text: "Vous avez choisi de répondre poliment.\nVotre patron vous ignore et continue sa journée.\nAprès avoir faussement remercié votre patron, vous vous installez sur votre bureau et commencer à regarder la pile de documents inintéressants à traiter.\nEt dire que vous avez fait tant d’années d’études et que vous avez travaillé sur des projets informatiques de grande ampleur.\nTous ça pour que de jeunes hommes fraichement diplômés, que vous avez formé en programmation, occupent les posts que vous espériez obtenir.\n(Vous parlez à vous-même)Il est que 9h du matin mais aucune envie de travailler...\nMais tu n'es pas obligée ? Souviens-toi les esquisses de programmes et d'objets que tu as dessiné.\nTu as développé tant de compétences en informatique, tu peux profiter des outils que tu as au travail pour concevoir et prototyper non ?\nOui, oui comme m'avait dit Grace Hopper, lorsqu'on travaillait sur l'UNIVAC  : “Oser et faire. Il est plus facile de demander le pardon après, que la permission avant.\nQue dois-je faire...\n\n1: Travailler sur les fiches de paies et CV à analyser.\n2: Commencer à élaborer le projet que vous avez en tête depuis un moment.",
        options: ["1"],
        nextScene: [3, 4],
    },
    {
        text: "Vous avez choisi de répliquer sèchement.\nVotre patron, vexé, vous menace de sanctions.\n\nFin du jeu.",
        options: ["2"],
        nextScene: [],
    },
    {
        text: "Vous vous mettez au travail et vous passez votre journée à trier les dossiers. À la fin de la journée, vous rentrez chez vous : encore une journée barbante de passée...\nFin du jeu.",
        options: ["1"],
        nextScene: [4, 5],
    },

     {
        text: "Pleins d’idées émergent : de surfaces haptiques sensibles, à des claviers aux touches molles et aux symboles abstraits, en passant par des interfaces laissant libre cours à l’imagination… Vous êtes lancées !\nVotre objectif imaginer un objet permettant une interaction entre l’ordinateur et l’humain d’une nouvelle manière.\nPourquoi pas se concentrer sur le clavier ? Et si les touches étaient non pas associés à des lettres et chiffres mais bien à un système symbolique atypique ? Vous aimeriez bien créer de nouveaux paradigmes d'intéractions homme-machine.\nPar quoi commencer ?\n\n1: Contacter grâce au système ARPAnet une de vos amies informaticienne pour échanger avec elle sur vos idées.\n2: Vous commencez à esquisser une idée de programme et clavier sur une feuille de brouillon.",
        options: ["2"],
        nextScene: [5, 6],
    },
    {
        text: "Vous avez choisi de répliquer sèchement.\nVotre patron, vexé, vous menace de sanctions.\n\nFin du jeu.",
        options: [""],
        nextScene: [],
    },
];

function typeText(text, callback) {
    let i = 0;
    const interval = setInterval(() => {
        gameOutput.textContent += text[i];
        i++;
        if (i >= text.length) {
            clearInterval(interval);
            callback();
        }
    }, typingSpeed);
}

function loadScene(sceneIndex) {
    gameState = sceneIndex;
    const scene = scenes[sceneIndex];
    gameOutput.textContent = "";
    typeText(scene.text, () => {
        if (scene.options.length > 0) {
            gameInput.disabled = false;
            gameInput.focus();
        }
    });
}

gameInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        const input = gameInput.value.toLowerCase().trim();
        gameInput.value = "";
        const scene = scenes[gameState];
        const optionIndex = scene.options.indexOf(input);
        if (optionIndex !== -1) {
            const nextScene = scene.nextScene[optionIndex];
            if (nextScene !== -1) {
                loadScene(nextScene);
            } else {
                gameOutput.textContent += "\n\nMerci d'avoir joué !";
                gameInput.disabled = true;
            }
        } else {
            gameOutput.textContent += "\nCommande non reconnue.";
        }
    }
});

// Load the first scene
loadScene(0);
