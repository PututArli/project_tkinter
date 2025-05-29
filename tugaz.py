import tkinter
from tkinter import ttk, messagebox,Label
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("800x500")


        self.frame_kiri = customtkinter.CTkFrame(root,width = 400 , height= 500, fg_color="transparent")
        self.frame_kiri.pack(side="left", fill="both", expand=True)

        img = Image.open("blur.jpg")
        img = img.resize((2000,2000))
        self.bg_image = ImageTk.PhotoImage(img)

        self.bg_label = Label(self.frame_kiri, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_kanan = customtkinter.CTkFrame(root,width = 400 , height= 500,  fg_color="#3f174f")
        self.frame_kanan.pack(side="left", fill="both", expand=True)

        self.tengah_framekiri = customtkinter.CTkFrame(self.frame_kiri)
        self.tengah_framekiri.pack(expand = True)
        
        self.label_judul = customtkinter.CTkLabel(self.tengah_framekiri, text="SIGN IN", font=("Times New Roman", 20, "bold"))
        self.label_judul.pack(pady=20, padx=10)

        self.entry_username = customtkinter.CTkEntry(self.tengah_framekiri,placeholder_text="Username", width=200)
        self.entry_username.pack(pady=(0,15), padx=20)

        self.entry_password = customtkinter.CTkEntry(self.tengah_framekiri, width=200,placeholder_text="Password", show="*")
        self.entry_password.pack(pady=(15,0), padx=30)

        self.label_welcome = customtkinter.CTkLabel(self.frame_kanan, text="Welcome", font=("Times New Roman", 50, "bold"))
        self.label_welcome.place(relx=0.5, rely=0.3, anchor="center")

        self.button = customtkinter.CTkButton(self.tengah_framekiri , text= "Login")
        self.button.pack(anchor = "center", pady=(30,20), padx=40)
    
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Login(root)
    root.mainloop()