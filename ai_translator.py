import tkinter as tk
from tkinter import ttk
from googletrans import Translator
import threading

# Initialize the translator
translator = Translator()

# Function to translate text in a separate thread (faster performance)
def translate_text():
    input_text = input_box.get("1.0", tk.END).strip()
    selected_lang = lang_var.get()

    # Use Urdu script for Punjabi
    target_lang = "ur" if selected_lang == "Punjabi" else language_dict[selected_lang]

    if input_text:
        translated_text = translator.translate(input_text, dest=target_lang).text
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated_text)

# Function to run translation in a separate thread (prevents UI lag)
def threaded_translation(event=None):
    threading.Thread(target=translate_text, daemon=True).start()

# Language mapping (Punjabi forced to Urdu script)
language_dict = {
    "Urdu": "ur",
    "Sindhi": "sd",
    "Balochi": "ur",  # No direct support, so using Urdu
    "Punjabi": "pa",  # Forces Punjabi in Urdu script
    "Pashto": "ps"
}

# Create GUI window
root = tk.Tk()
root.title("Real-Time AI Translator")
root.geometry("600x400")

# Language Selection
lang_var = tk.StringVar(value="Urdu")
ttk.Label(root, text="Select Language:").pack(pady=5)
lang_menu = ttk.Combobox(root, textvariable=lang_var, values=list(language_dict.keys()), state="readonly")
lang_menu.pack(pady=5)

# Input Text Box
ttk.Label(root, text="Enter Text (English):").pack()
input_box = tk.Text(root, height=5, width=50)
input_box.pack(pady=5)
input_box.bind("<KeyRelease>", threaded_translation)  # Faster translation

# Output Text Box
ttk.Label(root, text="Translated Text:").pack()
output_box = tk.Text(root, height=5, width=50, state="normal")
output_box.pack(pady=5)

# Run GUI
root.mainloop()
