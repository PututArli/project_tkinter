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


        self.frame_kiri = customtkinter.CTkFrame(root, width=400, height=500)
        self.frame_kiri.pack(side="left", fill="both", expand=True)

        self.frame_kanan = customtkinter.CTkFrame(root, width=400, height=500, fg_color="purple")
        self.frame_kanan.pack(side="right", fill="both", expand=True)

        self.label_judul = customtkinter.CTkLabel(self.frame_kiri, text="SIGN IN", font=("Arial", 20, "bold"))
        self.label_judul.pack(pady=20, padx=10)

        self.tengah_framekiri = customtkinter.CTkFrame(self.frame_kiri)
        self.tengah_framekiri.pack(expand = True)

        self.button = customtkinter.CTkButton(self.tengah_framekiri , text= "Login")
        self.button.pack(anchor = "center")

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Login(root)
    root.mainloop()