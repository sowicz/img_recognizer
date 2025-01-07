import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Recognizer")
        self.root.geometry("800x600")
        self.root.rowconfigure(1, weight=1)  # Środkowy wiersz (podział na kolumny) elastyczny
        self.root.columnconfigure(0, weight=1)  # Ustawienie kolumny głównej jako elastycznej

        # Ramka dla sekcji input
        self.input_frame = tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10)
        self.input_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Etykiety i pola tekstowe w ramce
        self.label1 = tk.Label(self.input_frame, text="Liczba 1:")
        self.label1.grid(row=0, column=0, pady=5, sticky="w")

        self.entry1 = tk.Entry(self.input_frame)
        self.entry1.grid(row=0, column=1, pady=5)

        self.label2 = tk.Label(self.input_frame, text="Liczba 2:")
        self.label2.grid(row=1, column=0, pady=5, sticky="w")

        self.entry2 = tk.Entry(self.input_frame)
        self.entry2.grid(row=1, column=1, pady=5)

        # Przycisk do obliczenia sumy
        self.calc_button = tk.Button(self.input_frame, text="Oblicz sumę", command=self.calculate_sum)
        self.calc_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Przycisk wczytania obrazu
        self.load_image_button = tk.Button(self.input_frame, text="Wczytaj obraz", command=self.load_image)
        self.load_image_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Pole na wynik
        self.result_label = tk.Label(self.input_frame, text="Wynik: ")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

        # Ramka dla sekcji obrazu
        self.pic_frame = tk.Frame(root, borderwidth=2, relief="groove")
        self.pic_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.root.columnconfigure(1, weight=3)  # Ustawienie szerokości 3/5 dla ramki obrazu
        self.root.rowconfigure(0, weight=1)

        # Canvas do wyświetlania obrazka
        self.canvas = tk.Canvas(self.pic_frame, bg="gray")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Paski przewijania
        self.scroll_x = tk.Scrollbar(self.pic_frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(self.pic_frame, orient="vertical", command=self.canvas.yview)
        


        # Ustawienie pasków przewijania
        self.scroll_x.pack(side="bottom", fill="x")
        self.scroll_y.pack(side="right", fill="y")  # Pasek pionowy na całą wysokość ramki obrazu
        
        # Przypięcie pasków do prawej strony i dolnej krawędzi
        self.scroll_x.place(relx=0, rely=1, relwidth=1, anchor="sw")  # Przypięcie paska poziomego do dołu
        self.scroll_y.place(relx=1, rely=0, relheight=1, anchor="ne")  # Przypięcie paska pionowego do prawej strony


        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        # Sekcja logów
        self.logs_frame = tk.Frame(root, borderwidth=2, relief="groove")
        self.logs_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.logs_frame.rowconfigure(1, weight=1)
        self.logs_frame.columnconfigure(0, weight=1)

        # Label nad logami
        self.logs_label = tk.Label(self.logs_frame, text="Logi:")
        self.logs_label.pack(anchor="nw", padx=5, pady=5)

        # Pole tekstowe na logi
        self.logs_text = tk.Text(self.logs_frame, height=5)
        self.logs_text.pack(fill="both", expand=True)

    def calculate_sum(self):
        try:
            # Pobranie wartości z pól tekstowych
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())

            # Obliczenie sumy
            result = num1 + num2

            # Wyświetlenie wyniku
            self.result_label.config(text=f"Wynik: {result}")
            self.add_log(f"Obliczono sumę: {num1} + {num2} = {result}")
        except ValueError:
            # Obsługa błędu w przypadku nieprawidłowego wejścia
            messagebox.showerror("Błąd", "Proszę podać poprawne liczby!")
            self.add_log("Błąd: Niepoprawne dane wejściowe!")

    def load_image(self):
        try:
            # Ścieżka do obrazu (przykładowa)
            image_path = "full_screen.png"

            # Otwórz obraz
            image = Image.open(image_path)

            # Konwersja obrazu do formatu obsługiwanego przez tkinter
            self.photo = ImageTk.PhotoImage(image)

            # Usuń poprzednie elementy z canvas
            self.canvas.delete("all")

            # Wyświetlenie obrazu na canvas
            self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

            # Ustaw rozmiar canvas na rozmiar obrazu
            self.canvas.config(scrollregion=self.canvas.bbox("all"))
            self.add_log(f"Wczytano obraz: {image_path}")
        except Exception as e:
            # Obsługa błędów (np. brak pliku obrazu)
            messagebox.showerror("Błąd", f"Nie udało się wczytać obrazu:\n{e}")
            self.add_log(f"Błąd wczytywania obrazu: {e}")

    def add_log(self, message):
        """Dodaje wpis do logów."""
        self.logs_text.insert("end", f"{message}\n")
        self.logs_text.see("end")  # Przewiń do ostatniego wpisu


if __name__ == "__main__":
    root = tk.Tk()
    app = UserInterface(root)
    root.mainloop()
