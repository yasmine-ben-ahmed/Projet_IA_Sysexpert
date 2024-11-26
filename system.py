from experta import *
from PIL import Image
details_of_cars = []
details_map = {}
import os


def preprocess():
    global details_of_cars, details_map
    
    # Initialisation des variables globales si ce n'est pas déjà fait
    details_of_cars = []
    details_map = {}
    
    try:
        # Lecture du fichier principal contenant la liste des voitures
        with open("cars.txt") as cars:
            cars_list = [car.strip() for car in cars if car.strip()]  # Filtre les lignes vides
    except FileNotFoundError:
        print("Le fichier cars.txt est introuvable.")
        return

    for single_car in cars_list:
        try:
            # Lecture des détails pour chaque voiture
            file_path = f"Cars_details/Cars_info/{single_car}.txt"
            with open(file_path) as s_car_file:
                detail_list = [line.strip() for line in s_car_file if line.strip()]  # Filtre les lignes vides
                details_of_cars.append(detail_list)
                details_map[str(detail_list)] = single_car
        except FileNotFoundError:
            print(f"Le fichier {file_path} est introuvable. Voiture ignorée.")
        except Exception as e:
            print(f"Erreur lors de la lecture de {single_car}.txt : {e}")



def identify_car(*args):
    cars_list = []
    for a in args:
        cars_list.append(a)
    return details_map[str(cars_list)]


def if_not_matching(car):
    if car is None:
        print("Aucune voiture ne correspond exactement à vos critères.")
    else:
        print(f"🎉🎉 La voiture la plus proche selon votre choix est \"{car}\"")
        try:
            # Vérifiez le nom du fichier attendu
            filename = f"Cars_details/Cars_photos/{car}.jpg"
            if os.path.exists(filename):
                im = Image.open(filename)
                im.show()
            else:
                print(f"Image introuvable : {filename}")
        except Exception as e:
            print(f"Erreur lors de l'affichage de l'image : {e}")



class findYourCar(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        print("🚗✨ 🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗 ✨🚗\n")
        print("🚗✨ Bienvenue dans l'Assistant Intelligent pour Trouver Votre Voiture ✨🚗\n")
        print("🌟 Préparez-vous à découvrir la voiture parfaite pour vous ! 🌟\n")
        print("🛠️  Répondez simplement aux questions suivantes pour que nous puissions vous aider :\n")
        print("-" * 100)

        yield Fact(action="find_car")

    # Budget Category: Only one question will be asked, and the rest will default to "non."
    @Rule(Fact(action='find_car'), NOT(Fact(BE=W())), NOT(Fact(BM=W())), NOT(Fact(BF=W())), salience=18)
    def Question_budget(self):
        budget = input("🔑 Avez-vous un budget élevé, moyen ou faible? (répondez avec 'élevé', 'moyen', ou 'faible') ~> ").strip().lower()
        if budget == "élevé":
            self.declare(Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"))
        elif budget == "moyen":
            self.declare(Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"))
        elif budget == "faible":
            self.declare(Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"))
        else:
            print("Réponse non valide, tout est défini à 'non'.")
            self.declare(Fact(BE="non"), Fact(BM="non"), Fact(BF="non"))

    # Fuel Category: Only one question will be asked, and the rest will default to "non."
    @Rule(Fact(action='find_car'), NOT(Fact(CE=W())), NOT(Fact(CD=W())), salience=17)
    def Question_fuel(self):
        fuel = input("🔑 Préférez-vous que la voiture consomme l'essence ou le diesel? (répondez avec 'essence' ou 'diesel') ~> ").strip().lower()
        if fuel == "essence":
            self.declare(Fact(CE="oui"), Fact(CD="non"))
        elif fuel == "diesel":
            self.declare(Fact(CE="non"), Fact(CD="oui"))
        else:
            print("Réponse non valide, tout est défini à 'non'.")
            self.declare(Fact(CE="non"), Fact(CD="non"))

    @Rule(Fact(action='find_car'), NOT(Fact(P5=W())), NOT(Fact(P2=W())), salience=16)
    def Question_places(self):
        places = input("🔑 Voulez-vous une voiture avec 5 places ou 2 places? (répondez avec '5' ou '2') ~> ").strip()
        if places == "5":
            self.declare(Fact(P5="oui"), Fact(P2="non"))
        elif places == "2":
            self.declare(Fact(P5="non"), Fact(P2="oui"))
        else:
            print("Réponse non valide, tout est défini à 'non'.")
            self.declare(Fact(P5="non"), Fact(P2="non"))

    @Rule(Fact(action='find_car'), NOT(Fact(V2=W())), NOT(Fact(V4=W())), salience=15)
    def Question_doors(self):
        doors = input("🔑 Préférez-vous une voiture avec 2 portes ou 4 portes? (répondez avec '2' ou '4') ~> ").strip()
        if doors == "2":
            self.declare(Fact(V2="oui"), Fact(V4="non"))
        elif doors == "4":
            self.declare(Fact(V2="non"), Fact(V4="oui"))
        else:
            print("Réponse non valide, tout est défini à 'non'.")
            self.declare(Fact(V2="non"), Fact(V4="non"))

    # Catégorie pour les boîtes de vitesse : une seule question posée, les autres sont définies par défaut sur "non"
    @Rule(Fact(action='find_car'), NOT(Fact(A=W())), NOT(Fact(M=W())), salience=14)
    def Question_transmission(self):
        transmission = input("🔑 Préférez-vous une voiture avec une boîte de vitesse automatique ou manuelle? (répondez avec 'auto' ou 'manuelle') ~> ").strip().lower()
        if transmission == "auto":
            self.declare(Fact(A="oui"), Fact(M="non"))
        elif transmission == "manuelle":
            self.declare(Fact(A="non"), Fact(M="oui"))
        else:
            print("Réponse non valide, tout est défini à 'non'.")
            self.declare(Fact(A="non"), Fact(M="non"))


    @Rule(Fact(action='find_car'), NOT(Fact(MA=W())), salience=13)
    def Question_11(self):
        self.declare(
            Fact(MA=input("🔑 Vous voulez des équipement de motorisation avancé ? (répondez avec oui/non) ~> ")))

    @Rule(Fact(action='find_car'), NOT(Fact(SA=W())), salience=12)
    def Question_12(self):
        self.declare(
            Fact(SA=input("🔑 Vous voulez des équipement de sécurité avancé ? (répondez avec oui/non) ~> ")))

    @Rule(Fact(action='find_car'), NOT(Fact(CA=W())), salience=11)
    def Question_13(self):
        self.declare(
            Fact(CA=input("🔑 Vous voulez des équipement de confort avancée ? (répondez avec oui/non) ~> ")))

    # Catégorie pour les couleurs : une seule question posée, les autres sont définies par défaut sur "non"
    @Rule(Fact(action='find_car'), 
        NOT(Fact(C1=W())), 
        NOT(Fact(C2=W())), 
        NOT(Fact(C3=W())), 
        NOT(Fact(C4=W())), 
        salience=10)
    def Question_couleurs(self):
        couleur = input(
            "🔑 Quelle couleur préférez-vous pour votre voiture? (répondez avec 'rouge', 'bleu', 'noir', ou 'blanc') ~> "
        ).strip().lower()
        
        if couleur == "rouge":
            self.declare(Fact(C1="oui"), Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
        elif couleur == "bleu":
            self.declare(Fact(C1="non"), Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
        elif couleur == "noir":
            self.declare(Fact(C1="non"), Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
        elif couleur == "blanc":
            self.declare(Fact(C1="non"), Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
        else:
            print("Réponse non valide, toutes les couleurs sont définies à 'non'.")
            self.declare(Fact(C1="non"), Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))


    @Rule(Fact(action='find_car'), 
        NOT(Fact(Voyage=W())), 
        NOT(Fact(Travail=W())), 
        NOT(Fact(Loisir=W())), 
        NOT(Fact(Familiale=W())), 
        salience=9)
    def Question_besoin(self):
        # Question pour Voyage
        voyage = input("🔑 Avez-vous besoin de cette voiture pour un *voyage* ? (oui/non) ~> ").strip().lower()
        if voyage == "oui":
            self.declare(Fact(Voyage="oui"))
        else:
            self.declare(Fact(Voyage="non"))
        
        # Question pour Travail
        travail = input("🔑 Avez-vous besoin de cette voiture pour le *travail* ? (oui/non) ~> ").strip().lower()
        if travail == "oui":
            self.declare(Fact(Travail="oui"))
        else:
            self.declare(Fact(Travail="non"))
        
        # Question pour Loisir
        loisir = input("🔑 Avez-vous besoin de cette voiture pour les *loisirs* ? (oui/non) ~> ").strip().lower()
        if loisir == "oui":
            self.declare(Fact(Loisir="oui"))
        else:
            self.declare(Fact(Loisir="non"))
        
        # Question pour Familiale
        familiale = input("🔑 Avez-vous besoin de cette voiture pour un usage *familial* ? (oui/non) ~> ").strip().lower()
        if familiale == "oui":
            self.declare(Fact(Familiale="oui"))
        else:
            self.declare(Fact(Familiale="non"))


    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_1(self):
        self.declare(Fact(car="lamborghini_Rouge"))
        im = Image.open("Cars_details/Cars_photos/lamborghini_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_2(self):
        self.declare(Fact(car="lamborghini_Bleu"))
        im = Image.open("Cars_details/Cars_photos/lamborghini_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_3(self):
        self.declare(Fact(car="lamborghini_Noir"))
        im = Image.open("Cars_details/Cars_photos/lamborghini_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_4(self):
        self.declare(Fact(car="lamborghini_Blanc"))
        im = Image.open("Cars_details/Cars_photos/lamborghini_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_5(self):
        self.declare(Fact(car="ferrari_Rouge"))
        im = Image.open("Cars_details/Cars_photos/ferrari_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_6(self):
        self.declare(Fact(car="ferrari_Bleu"))
        im = Image.open("Cars_details/Cars_photos/ferrari_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_7(self):
        self.declare(Fact(car="ferrari_Noir"))
        im = Image.open("Cars_details/Cars_photos/ferrari_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_8(self):
        self.declare(Fact(car="ferrari_Blanc"))
        im = Image.open("Cars_details/Cars_photos/ferrari_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_9(self):
        self.declare(Fact(car="porche_Rouge"))
        im = Image.open("Cars_details/Cars_photos/porche_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_10(self):
        self.declare(Fact(car="porche_Bleu"))
        im = Image.open("Cars_details/Cars_photos/porche_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_11(self):
        self.declare(Fact(car="porche_Noir"))
        im = Image.open("Cars_details/Cars_photos/porche_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_12(self):
        self.declare(Fact(car="porche_Blanc"))
        im = Image.open("Cars_details/Cars_photos/porche_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_13(self):
        self.declare(Fact(car="mercedes_Rouge"))
        im = Image.open("Cars_details/Cars_photos/mercedes_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_14(self):
        self.declare(Fact(car="mercedes_Bleu"))
        im = Image.open("Cars_details/Cars_photos/mercedes_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_15(self):
        self.declare(Fact(car="mercedes_Noir"))
        im = Image.open("Cars_details/Cars_photos/mercedes_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_16(self):
        self.declare(Fact(car="mercedes_Blanc"))
        im = Image.open("Cars_details/Cars_photos/mercedes_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_17(self):
        self.declare(Fact(car="range_rover_Rouge"))
        im = Image.open("Cars_details/Cars_photos/range_rover_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_18(self):
        self.declare(Fact(car="range_rover_Bleu"))
        im = Image.open("Cars_details/Cars_photos/range_rover_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_19(self):
        self.declare(Fact(car="range_rover_Noir"))
        im = Image.open("Cars_details/Cars_photos/range_rover_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_20(self):
        self.declare(Fact(car="range_rover_Blanc"))
        im = Image.open("Cars_details/Cars_photos/range_rover_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_21(self):
        self.declare(Fact(car="BMW_Rouge"))
        im = Image.open("Cars_details/Cars_photos/BMW_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_22(self):
        self.declare(Fact(car="BMW_Bleu"))
        im = Image.open("Cars_details/Cars_photos/BMW_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_23(self):
        self.declare(Fact(car="BMW_Noir"))
        im = Image.open("Cars_details/Cars_photos/BMW_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_24(self):
        self.declare(Fact(car="BMW_Blanc"))
        im = Image.open("Cars_details/Cars_photos/BMW_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_25(self):
        self.declare(Fact(car="audi_Rouge"))
        im = Image.open("Cars_details/Cars_photos/audi_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_26(self):
        self.declare(Fact(car="audi_Bleu"))
        im = Image.open("Cars_details/Cars_photos/audi_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_27(self):
        self.declare(Fact(car="audi_Noir"))
        im = Image.open("Cars_details/Cars_photos/audi_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_28(self):
        self.declare(Fact(car="audi_Blanc"))
        im = Image.open("Cars_details/Cars_photos/audi_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_29(self):
        self.declare(Fact(car="wallyscar_Rouge"))
        im = Image.open("Cars_details/Cars_photos/wallyscar_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_30(self):
        self.declare(Fact(car="wallyscar_Bleu"))
        im = Image.open("Cars_details/Cars_photos/wallyscar_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_31(self):
        self.declare(Fact(car="wallyscar_Noir"))
        im = Image.open("Cars_details/Cars_photos/wallyscar_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_32(self):
        self.declare(Fact(car="wallyscar_Blanc"))
        im = Image.open("Cars_details/Cars_photos/wallyscar_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_33(self):
        self.declare(Fact(car="KIA_Rouge"))
        im = Image.open("Cars_details/Cars_photos/KIA_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_34(self):
        self.declare(Fact(car="KIA_Bleu"))
        im = Image.open("Cars_details/Cars_photos/KIA_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_35(self):
        self.declare(Fact(car="KIA_Noir"))
        im = Image.open("Cars_details/Cars_photos/KIA_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_36(self):
        self.declare(Fact(car="KIA_Blanc"))
        im = Image.open("Cars_details/Cars_photos/KIA_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_37(self):
        self.declare(Fact(car="mazda_Rouge"))
        im = Image.open("Cars_details/Cars_photos/mazda_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_38(self):
        self.declare(Fact(car="mazda_Bleu"))
        im = Image.open("Cars_details/Cars_photos/mazda_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_39(self):
        self.declare(Fact(car="mazda_Noir"))
        im = Image.open("Cars_details/Cars_photos/mazda_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="non"))
    def car_40(self):
        self.declare(Fact(car="mazda_Blanc"))
        im = Image.open("Cars_details/Cars_photos/mazda_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_41(self):
        self.declare(Fact(car="peugeot_Rouge"))
        im = Image.open("Cars_details/Cars_photos/peugeot_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_42(self):
        self.declare(Fact(car="peugeot_Bleu"))
        im = Image.open("Cars_details/Cars_photos/peugeot_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_43(self):
        self.declare(Fact(car="peugeot_Noir"))
        im = Image.open("Cars_details/Cars_photos/peugeot_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_44(self):
        self.declare(Fact(car="peugeot_Blanc"))
        im = Image.open("Cars_details/Cars_photos/peugeot_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2=""),
          Fact(A="non"), Fact(M="oui"), Fact(MA=""),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_45(self):
        self.declare(Fact(car="volkswagen_Rouge"))
        im = Image.open("Cars_details/Cars_photos/volkswagen_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2=""),
          Fact(A="non"), Fact(M="oui"), Fact(MA=""),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_46(self):
        self.declare(Fact(car="volkswagen_Bleu"))
        im = Image.open("Cars_details/Cars_photos/volkswagen_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2=""),
          Fact(A="non"), Fact(M="oui"), Fact(MA=""),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_47(self):
        self.declare(Fact(car="volkswagen_Noir"))
        im = Image.open("Cars_details/Cars_photos/volkswagen_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2=""),
          Fact(A="non"), Fact(M="oui"), Fact(MA=""),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="oui"), Fact(Travail="non"), Fact(Loisir="oui"), Fact(Familiale="oui"))
    def car_48(self):
        self.declare(Fact(car="volkswagen_Blanc"))
        im = Image.open("Cars_details/Cars_photos/volkswagen_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_49(self):
        self.declare(Fact(car="renault_Rouge"))
        im = Image.open("Cars_details/Cars_photos/renault_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_50(self):
        self.declare(Fact(car="renault_Bleu"))
        im = Image.open("Cars_details/Cars_photos/renault_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_51(self):
        self.declare(Fact(car="renault_Noir"))
        im = Image.open("Cars_details/Cars_photos/renault_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_52(self):
        self.declare(Fact(car="renault_Blanc"))
        im = Image.open("Cars_details/Cars_photos/renault_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_53(self):
        self.declare(Fact(car="fiat_Rouge"))
        im = Image.open("Cars_details/Cars_photos/fiat_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_54(self):
        self.declare(Fact(car="fiat_Bleu"))
        im = Image.open("Cars_details/Cars_photos/fiat_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_55(self):
        self.declare(Fact(car="fiat_Noir"))
        im = Image.open("Cars_details/Cars_photos/fiat_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_56(self):
        self.declare(Fact(car="fiat_Blanc"))
        im = Image.open("Cars_details/Cars_photos/fiat_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_57(self):
        self.declare(Fact(car="citroen_Rouge"))
        im = Image.open("Cars_details/Cars_photos/citroen_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_58(self):
        self.declare(Fact(car="citroen_Bleu"))
        im = Image.open("Cars_details/Cars_photos/citroen_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_59(self):
        self.declare(Fact(car="citroen_Noir"))
        im = Image.open("Cars_details/Cars_photos/citroen_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"),
          Fact(Voyage="non"), Fact(Travail="oui"), Fact(Loisir="non"), Fact(Familiale="oui"))
    def car_60(self, car):
        self.declare(Fact(car="citroen_Blanc"))
        #print("La voiture convenable pour vous est  \""+car+"\"\n")
        im = Image.open("Cars_details/Cars_photos/citroen_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'), Fact(car=MATCH.car), salience=-998)
    def car(self, car):
        a = car
        print("✅ La voiture convenable pour vous est  \""+a+"\"\n")

    @Rule(Fact(action='find_car'),
          Fact(BE=MATCH.BE),
          Fact(BM=MATCH.BM),
          Fact(BF=MATCH.BF),
          Fact(CE=MATCH.CE),
          Fact(CD=MATCH.CD),
          Fact(P5=MATCH.P5),
          Fact(P2=MATCH.P2),
          Fact(V4=MATCH.V4),
          Fact(V2=MATCH.V2),
          Fact(A=MATCH.A),
          Fact(M=MATCH.M),
          Fact(MA=MATCH.MA),
          Fact(SA=MATCH.SA),
          Fact(CA=MATCH.CA),
          Fact(C1=MATCH.C1),
          Fact(C2=MATCH.C2),
          Fact(C3=MATCH.C3),
          Fact(C4=MATCH.C4),
          Fact(Voyage=MATCH.Voyage),
          Fact(Travail=MATCH.Travail),
          Fact(Loisir=MATCH.Loisir),
          Fact(Familiale=MATCH.Familiale),
          NOT(Fact(car=MATCH.car)), salience=-999)
    def not_matched(self, BE, BM, BF, CE, CD, P5, P2, V4, V2, A, M, MA, SA, CA, C1, C2, C3, C4, Voyage, Travail, Loisir, Familiale):
        print("❌ Il n'y a pas une voiture pour vos critére ,")
        listofcar = [BE, BM, BF, CE, CD, P5, P2,
                     V4, V2, A, M, MA, SA, CA, C1, C2, C3, C4, Voyage, Travail, Loisir, Familiale]
        max_count = 0
        max_car = ""
        for key, val in details_map.items():
            count = 0
            temp = eval(key)
            for i in range(0, len(listofcar)):
                if (temp[i] == listofcar[i]):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_car = val
        if_not_matching(max_car)


if __name__ == "__main__":
    preprocess()
    engine = findYourCar()
    while (1):
        engine.reset()  # prepare
        engine.run()
        print("----------------Voulez-vous rechoisir une autre voiture (oui/non)----------------")
        if input() == "non":
            print("🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗")
            print("🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗 Merci d'avoir passé ce test 🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗 ")
            print("🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗")
            break
