import tkinter
from tkinter import ttk, messagebox,Label
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("blue")

class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1200x700")

        self.frame_tengah = customtkinter.CTkFrame(root,width = 400 , height= 500, fg_color="transparent")
        self.frame_tengah.pack(fill="both", expand=True)

        img_tengah = Image.open("blur.jpg")
        img_tengah = img_tengah.resize((2000,2000))
        self.bg_tengah_image = ImageTk.PhotoImage(img_tengah)

        self.bg_tengah_label = Label(self.frame_tengah, image=self.bg_tengah_image)
        self.bg_tengah_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.canvas_welcome = customtkinter.CTkCanvas(self.frame_tengah,width = 400, height= 100,highlightthickness=0)
        self.canvas_welcome.place(relx=0.5, rely=0.25, anchor="center")
        
        self.canvas_welcome.create_text(200,50,text="Welcome",font=("Times New Roman", 50, "bold"),fill="#d19a03")

        self.canvas_subtext1 = customtkinter.CTkCanvas(self.frame_tengah,width = 400, height= 50,highlightthickness=0)
        self.canvas_subtext1.place(relx=0.5, rely=0.323, anchor="center")  

        self.canvas_subtext1.create_text(200,25,text="to our projects",font=("Arial", 25 , "bold"),fill="#d19a03")

        self.button_start = customtkinter.CTkButton(self.frame_tengah , text= "Start",font=("Times New Roman", 20, "bold"), command=self.sda)
        self.button_start.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.2, relheight=0.04)

        self.button_about = customtkinter.CTkButton(self.frame_tengah , text= "About Us",font=("Times New Roman", 20, "bold"), command=self.aboutus)
        self.button_about.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.2, relheight=0.04)


        self.frame_about = customtkinter.CTkFrame(self.root)

        self.canvas_about = customtkinter.CTkCanvas(self.frame_about,width = 400, height= 100,highlightthickness=0)
        self.canvas_about.place(relx=0.5, rely=0.2, anchor="center")
        self.canvas_about.create_text(200,50,text="Perkenalan",font=("Times New Roman", 50, "bold"),fill="#d19a03")

        self.button_back1 = customtkinter.CTkButton(self.frame_about , text= "Back",font=("Times New Roman", 20, "bold"), command=self.welcomepage)
        self.button_back1.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.2, relheight=0.04)


        self.frame_sda = customtkinter.CTkFrame(self.root)

        self.canvas_sda = customtkinter.CTkCanvas(self.frame_sda,width = 400, height= 100,highlightthickness=0)
        self.canvas_sda.place(relx=0.5, rely=0.2, anchor="center")
        self.canvas_sda.create_text(200,50,text="SDA",font=("Times New Roman", 50, "bold"),fill="#d19a03")

        self.button_back2 = customtkinter.CTkButton(self.frame_sda , text= "Back",font=("Times New Roman", 20, "bold"), command=self.welcomepage)
        self.button_back2.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.2, relheight=0.04)



    def welcomepage(self):
        self.frame_about.pack_forget()
        self.frame_sda.pack_forget()
        self.frame_tengah.pack(fill="both", expand=True)

    def aboutus(self):
        self.frame_tengah.pack_forget()
        self.frame_about.pack(fill="both", expand=True)

    def sda(self):
        self.frame_tengah.pack_forget()
        self.frame_sda.pack(fill="both", expand=True)


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