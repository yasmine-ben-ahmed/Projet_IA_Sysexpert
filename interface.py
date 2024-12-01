import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class CarRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IntelliCarManager System")
        self.root.geometry("800x900")
        self.root.configure(bg="#818d8c")  

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

        # Page de bienvenue
        self.show_welcome_screen()

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

    def show_welcome_screen(self):
        
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set a modern background color
        self.root.configure(bg="#0a0f19")

        # Welcome message
        welcome_label = tk.Label(
            self.root,
            text="Bienvenue dans Intellicar\nWhere Intelligence Meets Your Journey!",
            font=("Helvetica", 20, "bold"),
            fg="#ffffff",
            bg="#0a0f19",
            justify="center",
        )
        welcome_label.pack(pady=30)

        # Image de bienvenue
        try:
            img = Image.open("image_cars.jpg")  # Replace with the path to your image
            img = img.resize((600, 400), Image.Resampling.LANCZOS)
            welcome_img = ImageTk.PhotoImage(img)
            image_label = tk.Label(self.root, image=welcome_img, bg="#1e272e")
            image_label.image = welcome_img  # Keep a reference to avoid garbage collection
            image_label.pack(pady=20)
        except FileNotFoundError:
            error_label = tk.Label(
                self.root,
                text="Image de bienvenue introuvable.",
                font=("Helvetica", 12, "italic"),
                fg="#e84118",
                bg="#1e272e",
            )
            error_label.pack(pady=20)

        # Button for starting
        start_button = tk.Button(
            self.root,
            text="Commencer",
            command=self.start_questions,
            font=("Helvetica", 16, "bold"),
            bg="#626869",
            fg="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",  # Hand cursor for modern touch
        )
        start_button.pack(pady=40)
        start_button.bind("<Enter>", lambda e: start_button.config(bg="#404d51"))  # Hover effect
        start_button.bind("<Leave>", lambda e: start_button.config(bg="#404d51"))



    def start_questions(self):
        # Efface l'écran de bienvenue
        for widget in self.root.winfo_children():
            widget.destroy()

        # Définir le fond de la fenêtre principale pour correspondre à la carte
        self.root.config(bg="#1e272e")

        # Ajoute les widgets pour les questions (si ce n'est pas déjà fait)
        if not hasattr(self, 'question_label'):
            self.question_label = tk.Label(
                self.root,
                text="",
                font=("Helvetica", 14),
                fg="#2d3436",
                bg="#1e272e",  # Assurez-vous que le fond est le même que celui de la carte
            )
            self.question_label.pack(pady=10)

        # Créer le frame des boutons et l'image (une seule fois)
        if not hasattr(self, 'button_frame'):
            self.button_frame = tk.Frame(self.root, bg="#1e272e")
            self.button_frame.pack(pady=20)

        if not hasattr(self, 'image_label'):
            self.image_label = tk.Label(self.root, bg="#1e272e")
            self.image_label.pack(pady=20)

        self.show_question()

    def show_question(self):
        # Efface l'écran actuel sans toucher à question_label
        for widget in self.root.winfo_children():
            if widget != self.question_label and widget != self.button_frame and widget != self.image_label:
                widget.destroy()

        # Vérifie s'il y a encore des questions
        if self.current_question_index >= len(self.questions):
            self.display_result()  # Affiche l'écran de résultat si plus de questions
            return

        # Crée une carte avec un cadre centré
        card_frame = tk.Frame(
            self.root,
            bg="#1e272e",  # Utilise la même couleur que celle du fond de la fenêtre
            bd=2,
            relief="ridge",
            padx=20,
            pady=20,
        )
        card_frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=400)

        # Crée un cadre pour les questions et les boutons (cette fois centré)
        content_frame = tk.Frame(card_frame, bg="#1e272e")
        content_frame.pack(expand=True)  # Expand to fill the card frame

        # Crée une étiquette pour la question
        question_label = tk.Label(
            content_frame,
            text=self.questions[self.current_question_index]["text"],
            font=("Helvetica", 16, "bold"),
            fg="#ffffff",
            bg="#1e272e",
            wraplength=600,  # Ajuste pour les longs textes
            justify="center",
        )
        question_label.pack(pady=20)

        # Crée un cadre pour les boutons à l'intérieur de la carte
        button_frame = tk.Frame(content_frame, bg="#1e272e")
        button_frame.pack(pady=20)

        # Génère des boutons en fonction du type de question
        question = self.questions[self.current_question_index]
        if question["type"] == "choice":
            # Crée un bouton pour chaque option
            for option in question["options"]:
                button = tk.Button(
                    button_frame,
                    text=option.capitalize(),
                    command=lambda opt=option: self.answer_question(opt),
                    font=("Helvetica", 14, "bold"),
                    bg="#404d51",  # Couleur par défaut du bouton
                    fg="#ffffff",
                    relief="flat",
                    bd=0,
                    padx=20,
                    pady=10,
                    cursor="hand2",
                )
                button.pack(side=tk.LEFT, padx=15)
                # Effet de survol
                button.bind("<Enter>", lambda e, b=button: b.config(bg="#626869"))
                button.bind("<Leave>", lambda e, b=button: b.config(bg="#404d51"))
        else:  # Type de question Oui/Non
            yes_button = tk.Button(
                button_frame,
                text="Oui",
                command=lambda: self.answer_question("oui"),
                font=("Helvetica", 14, "bold"),
                bg="#404d51",
                fg="#ffffff",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                cursor="hand2",
            )
            no_button = tk.Button(
                button_frame,
                text="Non",
                command=lambda: self.answer_question("non"),
                font=("Helvetica", 14, "bold"),
                bg="#404d51",
                fg="#ffffff",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                cursor="hand2",
            )
            yes_button.pack(side=tk.LEFT, padx=15)
            no_button.pack(side=tk.LEFT, padx=15)
            # Effet de survol pour les boutons Oui/Non
            yes_button.bind("<Enter>", lambda e: yes_button.config(bg="#626869"))
            yes_button.bind("<Leave>", lambda e: yes_button.config(bg="#404d51"))
            no_button.bind("<Enter>", lambda e: no_button.config(bg="#626869"))
            no_button.bind("<Leave>", lambda e: no_button.config(bg="#404d51"))

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
                {"model": f"Fiat_{color.capitalize()}", "budget": "faible", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "oui", "advanced_comfort": "non", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "non", "Familiale": "oui"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            # Mercedes
            *[
                {"model": f"Mercedes_{color.capitalize()}", "budget": "élevé", "fuel": "essence", "places": "5", "doors": "4", "transmission": "auto", "advanced_motor": "non", "advanced_safety": "non", "advanced_comfort": "oui", "color": color, "Voyage": "non", "Travail": "oui", "Loisir": "oui", "Familiale": "non"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
            # Peugeot
            *[
                {"model": f"Peugeot_{color.capitalize()}", "budget": "faible", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "non", "advanced_safety": "oui", "advanced_comfort": "oui", "color": color, "Voyage": "oui", "Travail": "oui", "Loisir": "non", "Familiale": "oui"}
                for color in ["Rouge", "Bleu", "Noir", "Blanc"]
            ],
 
            # Volkswagen
            *[
                {"model": f"Volkswagen_{color.capitalize()}", "budget": "moyen", "fuel": "essence", "places": "5", "doors": "4", "transmission": "manuelle", "advanced_motor": "oui", "advanced_safety": "oui", "advanced_comfort": "oui", "color": color, "Voyage": "oui", "Travail": "non", "Loisir": "oui", "Familiale": "oui"}
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


        # Selection of the first matching car or a default model
        if matching_cars:
            recommended_car = matching_cars[0]["model"]
        else:
            recommended_car = "mazda_Noir"  # Default if no match is found

        # Format the recommended car's name
        formatted_car_name = recommended_car.replace("_", " ").title()

        # Clear previous content and center everything
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create a frame to center content
        center_frame = tk.Frame(self.root, bg="#1e272e")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Display the thank-you message
        thank_label = tk.Label(
            center_frame,
            text="Merci d'avoir utilisé notre système de recommandation !",
            font=("Helvetica", 16, "bold"),
            fg="#ffffff",
            bg="#1e272e",
            wraplength=600,
            justify="center",
        )
        thank_label.pack(pady=10)

        # Display the recommendation message
        recommendation_label = tk.Label(
            center_frame,
            text=f"Voici la voiture recommandée : {formatted_car_name}",
            font=("Helvetica", 14),
            fg="#ffffff",
            bg="#1e272e",
            wraplength=600,
            justify="center",
        )
        recommendation_label.pack(pady=10)

        # Display the car image
        try:
            img = Image.open(f"Cars_details/Cars_photos/{recommended_car}.jpg")
            img = img.resize((400, 300), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            image_label = tk.Label(center_frame, image=img, bg="#1e272e")
            image_label.image = img
            image_label.pack(pady=10)
        except FileNotFoundError:
            messagebox.showerror("Erreur", f"L'image pour {recommended_car} est introuvable!")

        # Frame for buttons
        button_frame = tk.Frame(center_frame, bg="#1e272e")
        button_frame.pack(pady=20)

        # Button to quit the application
        exit_button = tk.Button(
            button_frame,
            text="Quitter",
            command=self.root.quit,
            font=("Helvetica", 14, "bold"),
            bg="#ff4d4d",
            fg="#ffffff",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
        )
        exit_button.pack(side=tk.LEFT, padx=10)

        # Button to start the questions again
        restart_button = tk.Button(
            button_frame,
            text="Recommencer",
            command=lambda: self.restart_questions(),
            font=("Helvetica", 14, "bold"),
            bg="#404d51",
            fg="#ffffff",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
        )
        restart_button.pack(side=tk.LEFT, padx=10)

        # Hover effects for buttons
        for button in [exit_button, restart_button]:
            button.bind("<Enter>", lambda e, btn=button: btn.config(bg="#626869"))
            button.bind("<Leave>", lambda e, btn=button: btn.config(bg="#404d51"))

    def restart_questions(self):
        """Restart the questionnaire process."""
        # Clear any necessary data or states
        self.current_question_index = 0  # Reset the question index (if used)
        self.collected_answers = []  # Reset user answers (if used)

        # Clear the screen and start questions
        for widget in self.root.winfo_children():
            widget.destroy()
        self.start_questions()  # Assumes this method starts the questionnaire


# Lancement de l'application
root = tk.Tk()
app = CarRecommendationApp(root)
root.mainloop()
