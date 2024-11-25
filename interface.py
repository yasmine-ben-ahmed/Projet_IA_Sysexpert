import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class CarRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Recommendation System")
        self.root.geometry("600x700")
        self.root.configure(bg="#f7f7f7")  # Couleur de fond claire

        # Variables pour stocker les réponses
        self.answers = {
            "budget": None,
            "fuel": None,
            "places": None,
            "doors": None,
            "transmission": None,
            "motor_advanced": None,
            "safety_advanced": None,
            "comfort_advanced": None,
            "color": None,
            "needs": {"Voyage": None, "Travail": None, "Loisir": None, "Familiale": None},
        }

        # Widgets
        self.label = tk.Label(
            self.root,
            text="Bienvenue dans le système de recommandation de voitures!",
            font=("Helvetica", 18, "bold"),
            fg="#4b6584",
            bg="#f7f7f7",
        )
        self.label.pack(pady=20)

        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 14),
            fg="#2d3436",
            bg="#f7f7f7",
        )
        self.question_label.pack(pady=10)

        self.button_frame = tk.Frame(self.root, bg="#f7f7f7")
        self.button_frame.pack(pady=20)

        self.image_label = tk.Label(self.root, bg="#f7f7f7")
        self.image_label.pack(pady=20)

        # Questions
        self.questions = [
            {"text": "Avez-vous un budget élevé, moyen ou faible?", "type": "choice", "options": ["élevé", "moyen", "faible"], "key": "budget"},
            {"text": "Préférez-vous que la voiture consomme l'essence ou le diesel?", "type": "choice", "options": ["essence", "diesel"], "key": "fuel"},
            {"text": "Voulez-vous une voiture avec 5 places ou 2 places?", "type": "choice", "options": ["5", "2"], "key": "places"},
            {"text": "Préférez-vous une voiture avec 2 portes ou 4 portes?", "type": "choice", "options": ["2", "4"], "key": "doors"},
            {"text": "Préférez-vous une boîte de vitesse automatique ou manuelle?", "type": "choice", "options": ["auto", "manuelle"], "key": "transmission"},
            {"text": "Avez-vous besoin de motorisation avancée?", "type": "yesno", "key": "motor_advanced"},
            {"text": "Avez-vous besoin de sécurité avancée?", "type": "yesno", "key": "safety_advanced"},
            {"text": "Avez-vous besoin de confort avancé?", "type": "yesno", "key": "comfort_advanced"},
            {"text": "Quelle couleur préférez-vous? (rouge, bleu, noir, blanc)", "type": "choice", "options": ["Rouge", "Bleu", "Noir", "Blanc"], "key": "color"},
            {"text": "Avez-vous besoin de cette voiture pour un voyage?", "type": "yesno", "key": "Voyage"},
            {"text": "Avez-vous besoin de cette voiture pour le travail?", "type": "yesno", "key": "Travail"},
            {"text": "Avez-vous besoin de cette voiture pour les loisirs?", "type": "yesno", "key": "Loisir"},
            {"text": "Avez-vous besoin de cette voiture pour un usage familial?", "type": "yesno", "key": "Familiale"},
        ]

        self.current_question_index = 0
        self.show_question()

    def show_question(self):
        # Efface tous les anciens widgets dans le button_frame
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        # Vérifie si on est à la fin des questions
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question["text"])

            if question["type"] == "choice":
                # Création dynamique de boutons pour les options
                for option in question["options"]:
                    button = tk.Button(
                        self.button_frame,
                        text=option.capitalize(),
                        command=lambda opt=option: self.answer_question(opt),
                        font=("Helvetica", 12),
                        bg="#74b9ff",
                        fg="white",
                        relief="flat",
                        padx=15,
                        pady=5,
                    )
                    button.pack(side=tk.LEFT, padx=10)
            else:  # Type "yesno"
                # Boutons Oui / Non
                self.yes_button = tk.Button(
                    self.button_frame,
                    text="Oui",
                    command=lambda: self.answer_question("oui"),
                    font=("Helvetica", 12),
                    bg="#55efc4",
                    fg="white",
                    relief="flat",
                    padx=15,
                    pady=5,
                )
                self.no_button = tk.Button(
                    self.button_frame,
                    text="Non",
                    command=lambda: self.answer_question("non"),
                    font=("Helvetica", 12),
                    bg="#ff7675",
                    fg="white",
                    relief="flat",
                    padx=15,
                    pady=5,
                )
                self.yes_button.pack(side=tk.LEFT, padx=10)
                self.no_button.pack(side=tk.LEFT, padx=10)
        else:
            self.display_result()

    def answer_question(self, answer):
        # Sauvegarde la réponse et passe à la question suivante
        question = self.questions[self.current_question_index]
        key = question["key"]

        if key in self.answers["needs"]:
            self.answers["needs"][key] = answer
        else:
            self.answers[key] = answer

        self.current_question_index += 1
        self.show_question()

    def display_result(self):
        # Base de données des voitures
        cars = [
            # Lamborghini
            *[
                {"model": f"lamborghini_{color.capitalize()}", "budget": "élevé", "fuel": "essence", "places": "2", "doors": "2", "transmission": "auto", "advanced_motor": "oui", "advanced_safety": "non", "advanced_comfort": "oui", "color": color, "Voyage": "non", "Travail": "non", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            
            # Ferrari
            *[
                {"model": f"ferrari_{color.capitalize()}", "budget": "élevé", "fuel": "essence", "places": "2", "doors": "2", "transmission": "auto", "advanced_motor": "oui", "advanced_safety": "oui", "advanced_comfort": "oui", "color": color, "Voyage": "non", "Travail": "non", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],

            # Porsche
            *[
                {"model": f"porche_{color.capitalize()}", "budget": "élevé", "fuel": "diesel", "places": "5", "doors": "4", "transmission": "auto", "advanced_motor": "oui", "advanced_safety": "oui", "advanced_comfort": "oui", "color": color, "Voyage": "non", "Travail": "non", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],

            # BMW
            *[
                {"model": f"BMW_{color.capitalize()}", "budget": "moyen", "fuel": "essence", "places": "5", "doors": "4", "transmission": "auto", "advanced_motor": "oui", "advanced_safety": "oui", "advanced_comfort": "oui", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],

            # KIA
            *[
                {"model": f"KIA_{color.capitalize()}", "budget": "faible", "fuel": "diesel", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "non", "color": color, "Voyage": "oui", "Travail": "non", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],

            # Mazda
            *[
                {"model": f"Mazda_{color.capitalize()}", "budget": "moyen", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "oui", "color": color, "Voyage": "non", "Travail": "non", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],

            # Renault
            *[
                {"model": f"Renault_{color.capitalize()}", "budget": "faible", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "non", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "non", "Familiale": "oui"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],

             # Citroen
            *[
                {"model": f"Citroen_{color.capitalize()}", "budget": "faible", "fuel": "disel", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "non", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "non", "Familiale": "oui"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            
            # Audi
            *[
                {"model": f"Audi_{color.capitalize()}", "budget": "moyen", "fuel": "essence", "places": "5", "doors": "4", "transmission": "auto", "advanced_motor": "non", "advanced_safety": "oui", "advanced_comfort": "non", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            # Ferrari
            *[
                {"model": f"Ferrari_{color.capitalize()}", "budget": "élevé", "fuel": "essence", "places": "2", "doors": "2", "transmission": "auto", "advanced_motor": "oui", "advanced_safety": "non", "advanced_comfort": "non", "color": color, "Voyage": "non", "Travail": "non", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            # Fiat
            *[
                {"model": f"Fiat_{color.capitalize()}", "budget": "faible", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "non", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "non", "Familiale": "oui"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            # Mercedes
            *[
                {"model": f"Mercedes_{color.capitalize()}", "budget": "élevé", "fuel": "essence", "places": "5", "doors": "4", "transmission": "auto", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "oui", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            # Peugeot
            *[
                {"model": f"Peugeot_{color.capitalize()}", "budget": "faible", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "non", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "non", "Familiale": "oui"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            # Range_rover
            *[
                {"model": f"Range_rover_{color.capitalize()}", "budget": "élevé", "fuel": "disel", "places": "5", "doors": "4", "transmission": "auto", "advanced_motor": "non", "advanced_safety": "oui", "advanced_comfort": "oui", "color": color, "Voyage": "oui", "Travail": "non", "Loisir": "oui", "Familiale": "oui"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            # Volkswagen
            *[
                {"model": f"Volkswagen_{color.capitalize()}", "budget": "moyen", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "oui", "color": color, "Voyage": "oui", "Travail": "non", "Loisir": "oui", "Familiale": "oui"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
             #Wallyscar
            *[
                {"model": f"Wallyscar_{color.capitalize()}", "budget": "moyen", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "non", "color": color, "Voyage": "non", "Travail": "non", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ]
        ]




        # Filtrage basé sur les réponses utilisateur
        matching_cars = [
            car for car in cars
            if car["budget"] == self.answers["budget"]
            and car["fuel"] == self.answers["fuel"]
            and car["places"] == self.answers["places"]
            and car["doors"] == self.answers["doors"]
            and car["transmission"] == self.answers["transmission"]
            and car["advanced_motor"] == self.answers.get("motor_advanced", "non")
            and car["advanced_safety"] == self.answers.get("safety_advanced", "non")
            and car["advanced_comfort"] == self.answers.get("comfort_advanced", "non")
            and car["color"] == self.answers["color"]
            and (
                self.answers.get("Voyage", "non") == "non" or car.get("Voyage", "non") == "oui"
            )
            and (
                self.answers.get("Travail", "non") == "non" or car.get("Travail", "non") == "oui"
            )
            and (
                self.answers.get("Loisir", "non") == "non" or car.get("Loisir", "non") == "oui"
            )
            and (
                self.answers.get("Familiale", "non") == "non" or car.get("Familiale", "non") == "oui"
            )
        ]



        # Sélection de la première voiture correspondante ou d'un modèle par défaut
        if matching_cars:
            recommended_car = matching_cars[0]["model"]
        else:
            recommended_car = "mazda_Rouge"  # Par défaut si aucune correspondance trouvée

        # Affichage de la voiture recommandée
        self.question_label.config(text="Voici la voiture recommandée :")
        self.button_frame.pack_forget()
        try:
            img = Image.open(f"Cars_details/Cars_photos/{recommended_car}.jpg")
            img = img.resize((400, 300), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
        except FileNotFoundError:
            messagebox.showerror("Erreur", f"L'image pour {recommended_car} est introuvable!")


# Lancement de l'application
root = tk.Tk()
app = CarRecommendationApp(root)
root.mainloop()
