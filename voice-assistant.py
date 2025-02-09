import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox


language_options = {
    "English": "en-US",
    "বাংলা": "bn-IN",
    "Hindi": "hi-IN",
    "Spanish": "es-ES",
    "French": "fr-FR"
}


def start_recognition():
    selected_language = language_var.get()  
    language_code = language_options.get(selected_language, "en-US")  # ভাষার কোড পাওয়া

    recognizer = sr.Recognizer()

    output_text.delete(1.0, tk.END)  

    try:
        with sr.Microphone() as source:
            print(f"Say something in {selected_language}...(say 'exit' to stop)")
            output_text.insert(tk.END, f"Say something in {selected_language}...\n")
            recognizer.adjust_for_ambient_noise(source)  
            audio = recognizer.listen(source)
            print("Listening...")

        text = recognizer.recognize_google(audio, language=language_code)
        print(f"You Said: {text}")
        output_text.insert(tk.END, f"You Said ({selected_language}): {text}\n")

        if text.lower() == "exit":
            output_text.insert(tk.END, "Exiting program...\n")

    except sr.UnknownValueError:
        output_text.insert(tk.END, "Sorry, I could not understand. Try again.\n")
    except sr.RequestError:
        output_text.insert(tk.END, "Could not request results. Check your internet connection.\n")


root = tk.Tk()
root.title("Jarvis Voice Assistant with Language Selection")
root.geometry("500x400")

language_var = tk.StringVar()
language_var.set("English")  # ডিফল্ট ভাষা ইংরেজি

language_menu = tk.OptionMenu(root, language_var, *language_options.keys())
language_menu.pack(pady=20)

start_button = tk.Button(root, text="Start Recognition", command=start_recognition)
start_button.pack(pady=10)

output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=20)

root.mainloop()
