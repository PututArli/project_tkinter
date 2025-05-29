import tkinter
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("800x500")

        self.label_judul = customtkinter.CTkLabel(root, text="Login Page", font=("Arial", 20, "bold"))
        self.label_judul.pack(pady=20, padx=10)

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Login(root)
    root.mainloop()