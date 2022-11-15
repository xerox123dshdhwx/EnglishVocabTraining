import random
import unidecode
from termcolor import colored

vocab_dict = {
    "A breakthrough": "une decouverte",
    "A casualty": "une victime",
    "A disability": "une infirmite",
    "A fire alarm": "une alerte incendie",
    "A hazard": "un risque",
    "A helmet": "un casque",
    "A physician": "un medecin",
    "A relief": "un soulagement",
    "A restricted area": "une zone interdite",
    "Sick leave": "un arret maladie",
    "A stretcher": "une civiere",
    "Affordable": "accessible",
    "An injury": "une blessure",
    "Caution": "attention",
    "Disabled": "invalide",
    "Dizziness/dizzy": "vertige",
    "Drugs": "des medicaments",
    "Exhausted": "epuise",
    "First aid kit": "trousse de premiers secours",
    "Current": "actuel",
    "Harmful": "dangereux",
    "Health benefits": "assurance maladie",
    "Healthy": "bon pour la sante",
    "Hurt/injured": "blesser",
    "Innocuous": "inoffensive",
    "No entrance": "entree interdite",
    "Noxious": "nocif",
    "Pain": "douleur",
    "Stamina": "endurance",
    "To be out sick": "etre en conge maladie",
    "To breathe": "respirer",
    "To call in sick": "appeler pour dire que l'on est malade",
    "To collapse": "s'effondrer",
    "To fall ill": "tomber malade",
    "To cough": "tousser",
    "To faint": "s'evanouir",
    "To heal": "guerir",
    "To prevent from": "empecher de",
    "To swell": "gonfler",
    "To undergo surgery": "subir une operation"
}

vocabAlreadyTranslated = []
bonne_rep, mauvaise_rep, x = 0, 0, 0
cpt = len(vocab_dict)

while x < cpt:
    res = key, val = random.choice(list(vocab_dict.items()))
    if (not res[0] in vocabAlreadyTranslated):
        rep = unidecode.unidecode(input(f"Traduire {colored(res[0], 'red')} : ")).lower()
        if (rep == res[1]):
            x += 1
            print("Bonne réponse !")
            bonne_rep += 1
            vocabAlreadyTranslated.append(res[0])
        else:
            print(f'Mauvaise réponse, Correction : {colored(res[1], "cyan")} ')
            mauvaise_rep += 1
        print(f'Fini à {(bonne_rep / cpt) * 100} % !')

print(f"Un total de {mauvaise_rep} de mauvaise réponse !")
