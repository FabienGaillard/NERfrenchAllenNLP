import random

type_rue = ["RUE", "PCE", "BOULEVARD", "SQUARE", "AVENENUE", "CENTRE"]
societes = [
    "LEROYMERLIN",
    "AUCHAN",
    "CHEZFREDERIQUE",
    "CLAIRDELUNE",
    "SOFTAKA",
    "TRAITEUR",
    "INTERFLORA",
    "ROBERT",
    "BOUCHERIE",
    "LAVERIE",
    "BLANCHISSERIE",
    "HOTEL",
    "PIZZERIA",
    "INDEE",
    "CONCEPTION",
    "CHARCUTERIE",
    "DIDIER",
    "OLLYHOCK",
    "PATACREP",
    "NEXUS",
    "SHAMROCK",
]
type_societe = [
    "EI",
    "EIRL",
    "EURL",
    "SARL",
    "SA",
    "SAS",
    "SASU",
    "SNC",
    "SCOP",
    "SCA",
    "SCS",
]
arrondissements = [
    "13001",
    "13002",
    "13003",
    "13004",
    "13005",
    "13006",
    "13007",
    "13007",
    "13008",
    "13009",
    "13010",
]
debut_rue = [
    "ALBERT",
    "BENOIT",
    "ROGER",
    "MARQUIS",
    "ORIANT",
    "JOSEPH",
    "CAMILLE",
    "FRANCOIS",
    "ROBERT",
    "VICTOR",
    "ALAIN",
    "FABIEN",
    "PRADO",
    "PARADIS",
    "BOURSE",
    "BERTON",
    "BRAVET" "MICHEL",
    "PASCAL",
    "VIRGILE",
    "FERRARI" "NAU",
    "EMERY",
    "JEAN",
    "EDOUARD",
    "GILLES",
    "HELENE",
]
fin_rue = [
    "",
    "",
    "",
    "DUPUIS",
    "HUGO",
    "GALLAN",
    "PAURIOL",
    "BAILLE",
    "GAULLE",
    "SAID",
    "KENEDY",
    "HOLLANDE",
    "MACON",
    "DESERT",
    "FRANGIN",
    "CHAVE",
    "MANIERE",
    "LACEPEDE",
    "TEISSERE",
    "HAGUEUNAU",
    "AMIS",
    "HEGER",
]


def numero_rue():
    return random.randint(1, 101)


def random_arrete():
    arr = random.randint(10, 500)
    if arr > 99:
        arrete = "%d_00%d" % (random.randint(2008, 2021), arr)
        return arrete
    else:
        arrete = "%d_000%d" % (random.randint(2008, 2021), arr)
        return arrete


def nom_famille():
    return "nom_famille"


def prenom():
    return "prenom"


def random_year():
    j = random.randint(1, 31)
    m = random.randint(1, 12)
    a = random.randint(2009, 2020)
    jour = "%d" % j
    mois = "%d" % m
    annee = "%d" % a
    if j < 10:
        jour = "0%d" % j
    if m < 10:
        mois = "0%d" % m
    date = jour + "/" + mois + "/" + annee
    return date


def new_text(path_to_save, number_of_documents):
    for i in range(number_of_documents):
        file_name = "addons_%d.txt" % i
        path = path_to_save + file_name
        f = open(path, "w")
        f.write("La O \nSociété O\n")
        f.write(
            random.choice(societes)
            + " I-ORG\n"
            + random.choice(type_societe)
            + " I-ORG\n"
        )
        f.write(
            ", O\nest O\nautorisé(e) O\nà O\noccuper O\nun O\nemplacement O\npublic O\nau O\ndroit O\nde O\nson O\ncommerce O\n"
        )
        f.write("%d I-LOC\n" % numero_rue())
        f.write(random.choice(type_rue) + " I-LOC\n")
        f.write(random.choice(debut_rue) + " I-LOC\n")
        fin = random.choice(fin_rue)
        if fin != "":
            f.write(fin + " I-LOC\n")
        f.write(random.choice(arrondissements) + " I-LOC\n")
        f.write(
            "MARSEILLE I-LOC\nen O\nvue O\nd' O\ny O\ninstaller O\n: O\nFace O\nau O\nn° I-LOC\n"
        )
        f.write("%d I-LOC\n" % numero_rue())
        f.write(
            ": O\nune O\nterrasse O\nsimple O\nsans O\ndélimitation O\nni O\ncouverture O\nni O\nécran O\ndétachée O\ndu O\ncommerce O\nFaçade O\n: O\n"
        )
        f.write("%d," % random.randint(1, 10))
        f.write(
            "%d0 I-SAI\nm I-SAI\nSaillie I-SAI\n/ O\nLargeur I-LRG\n: O\n"
            % random.randint(1, 10)
        )
        f.write("%d," % random.randint(1, 10))
        f.write("%d0 I-LRG\nm I-LRG\nSuperficie I-SUP\n: O\n" % random.randint(1, 10))
        f.write(
            "%d I-SUP\nm² I-SUP\nFace O\nau O\nau O\nn° I-LOC\n" % random.randint(1, 61)
        )
        f.write("%d I-LOC\n" % numero_rue())
        f.write(
            ": O\nune O\nterrasse O\nsimple O\nsans O\ndélimitation O\nni O\ncouverture O\nni O\nécran O\ndétachée O\ndu O\ncommerce O\nFaçade O\n: O\n"
        )
        f.write("%d," % random.randint(1, 10))
        f.write(
            "%d0 I-SAI\nm I-SAI\nSaillie I-SAI\n/ O\nLargeur I-LRG\n: O\n"
            % random.randint(1, 10)
        )
        f.write("%d," % random.randint(1, 10))
        f.write("%d0 I-LRG\nm I-LRG\nSuperficie I-SUP\n: O\n" % random.randint(1, 10))
        f.write("%d I-SUP\nm² I-SUP\nSuivant O\nplan O\n. O\n" % random.randint(1, 61))
        f.write(
            "L' O\nexploitation O\nde O\nl' O\nétablissement O\nsusmentionné O\ndoit O\nêtre O\nconforme O\naux O\nnormes O\nsanitaires O\nen O\nvigueur O\n. O\n\n"
        )
        f.write(
            "Toute O\ninfraction O\nen O\nmatière O\nd' O\nhygiène O\nou O\nnon-respect O\ndes O\ndispositions O\nréglementaires O\nconstatés O\nlors O\ndes O\ncontrôles O\nréalisés O\npar O\nles O\nAdministrations O\n"
        )
        f.write(
            "compétentes O\npourra O\nentraîner O\nla O\nrévocation O\nde O\nl' O\nautorisation O\nd' O\noccupation O\ndu O\ndomaine O\npublic O\n. O\n"
        )

        f.write("N° I-ART\n")
        f.write(random_arrete())
        f.write("_VDM I-ART\n")  #  2018_00086_VDM I-ART\
        f.write(
            "Arreté O\nOportant O\nautorisation O\nd' O\noccupation O\ndu O\ndomaine O\npublic O\n- O\nTerasses O\n- O\n"
        )
        f.write("%d I-LOC\n" % numero_rue())
        f.write(random.choice(type_rue).lower() + " I-LOC\n")
        f.write(random.choice(debut_rue).lower() + " I-LOC\n")
        fin = random.choice(fin_rue).lower()
        if fin != "":
            f.write(fin + " I-LOC\n")
        f.write(random.choice(arrondissements) + " I-LOC\n")
        f.write("- O\n")
        f.write(
            random.choice(societes).lower()
            + " I-ORG\n"
            + random.choice(type_societe).lower()
            + " I-ORG\n"
        )
        f.write("- O\n")
        f.write("compte I-CMP\n")
        f.write("n° I-CMP\n")
        f.write("%d/0%d I-CMP\n" % (random.randint(10000, 60000), random.randint(1, 9)))
        f.write(". O\n")

        f.write(
            "Vu O\nla O\ndemande O\n%d/%d I-DMD\n"
            % (random.randint(2009, 2021), random.randint(1000, 5000))
        )
        f.write("reçue O\nle O\n")

        f.write(random_year() + " I-DAT\n")
        f.write("présentée O\npar O\n")
        f.write(
            random.choice(societes)
            + " I-ORG\n"
            + random.choice(type_societe)
            + " I-ORG\n"
        )
        f.write(", O\nreprésentée O\npar O\n")
        f.write(nom_famille() + " I-PER\n" + prenom() + " I-PER\n")
        f.write(", O\ndomiciliée O\n")
        f.write("%d I-LOC\n" % numero_rue())
        f.write(random.choice(type_rue).lower() + " I-LOC\n")
        f.write(random.choice(debut_rue).lower() + " I-LOC\n")
        fin = random.choice(fin_rue).lower()
        if fin != "":
            f.write(fin + " I-LOC\n")
        f.write(random.choice(arrondissements) + " I-LOC\n")
        f.write("Marseille I-LOC\n")
        f.write(
            "en O\nvue O\nd' O\noccuper O\nun O\nemplacement O\npublic O\nà O\nl' O\nadresse O\nsuivante O\n: O\n"
        )
        f.write("%d I-LOC\n" % numero_rue())
        f.write(random.choice(type_rue) + " I-LOC\n")
        f.write(random.choice(debut_rue) + " I-LOC\n")
        fin = random.choice(fin_rue)
        if fin != "":
            f.write(fin + " I-LOC\n")
        f.write(random.choice(arrondissements) + " I-LOC\n")
        f.write("MARSEILLE I-LOC\n")
        f.write(". O")
        f.close()


validation = "addons_validation/"
train = "addons_train/"


new_text(validation, 2000)
new_text(train, 2000)
