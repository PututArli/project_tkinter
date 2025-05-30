import tkinter
from tkinter import ttk, messagebox,Label
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")

class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1200x700")

        self.frame_kiri = customtkinter.CTkFrame(root,width = 400 , height= 500, fg_color="transparent")
        self.frame_kiri.pack(side="left", fill="both", expand=True)

        img_kiri = Image.open("blur.jpg")
        img_kiri = img_kiri.resize((2000,2000))
        self.bg_kiri_image = ImageTk.PhotoImage(img_kiri)

        self.bg_kiri_label = Label(self.frame_kiri, image=self.bg_kiri_image)
        self.bg_kiri_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_kanan = customtkinter.CTkFrame(root,width = 400 , height= 500)
        self.frame_kanan.pack(side="left", fill="both", expand=True)

        img_kanan = Image.open("awan.png")
        img_kanan = img_kanan.resize((2000,2000))
        self.bg_kanan_image = ImageTk.PhotoImage(img_kanan)

        self.bg_kanan_label = Label(self.frame_kanan, image=self.bg_kanan_image)
        self.bg_kanan_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.tengah_framekiri = customtkinter.CTkFrame(self.frame_kiri)
        self.tengah_framekiri.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.45, relheight=0.455)
        
        self.label_judul = customtkinter.CTkLabel(self.tengah_framekiri, text="SIGN IN", font=("Times New Roman", 20, "bold"))
        self.label_judul.place(relx=0.5, rely=0.1, anchor="center")

        self.entry_username = customtkinter.CTkEntry(self.tengah_framekiri,placeholder_text="Username", width=200)
        self.entry_username.place(relx=0.5, rely=0.25, anchor="center", relwidth=0.9, relheight=0.1)

        self.entry_password = customtkinter.CTkEntry(self.tengah_framekiri, width=200, placeholder_text="Password", show="*")
        self.entry_password.place(relx=0.5, rely=0.425, anchor="center", relwidth=0.9, relheight=0.1)

        self.canvas_welcome = customtkinter.CTkCanvas(self.frame_kanan,width = 400, height= 100,highlightthickness=0)
        self.canvas_welcome.place(relx=0.5, rely=0.45, anchor="center")
        self.canvas_welcome.create_image(0 , 0 ,image=self.bg_kanan_image, anchor="nw")
        
        self.canvas_welcome.create_text(200,50,text="Welcome",font=("Times New Roman", 50, "bold"),fill="black")

        self.canvas_subtext1 = customtkinter.CTkCanvas(self.frame_kanan,width = 400, height= 50,highlightthickness=0)
        self.canvas_subtext1.place(relx=0.5, rely=0.522, anchor="center")
        self.canvas_subtext1.create_image(0 , 0 ,image=self.bg_kanan_image, anchor="nw")        

        self.canvas_subtext1.create_text(200,25,text="to our projects",font=("Times New Roman", 25 , "bold"),fill="black")

        self.button_login = customtkinter.CTkButton(self.tengah_framekiri , text= "Login",font=("Times New Roman", 20, "bold"), command=self.Login)
        self.button_login.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.9, relheight=0.1)

    def Login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "WisnuXiaomi" and password == "635":
            messagebox.showinfo("Login Sukses!", "selamat datang")
        else:
            messagebox.showerror("Login Gagal", "coba lagi!")
        
    
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Welcome(root)
    root.mainloop()