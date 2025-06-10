import tkinter
from tkinter import messagebox
import customtkinter


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue") 

class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title("Score")
        self.root.geometry("1200x700")
        self.root.configure(bg="#fdf6e3") 
        self.frame_tengah = customtkinter.CTkFrame(root, fg_color="#fdf6e3")
        self.frame_tengah.pack(fill="both", expand=True)

        #Text welcome
        self.label_welcome = customtkinter.CTkLabel(self.frame_tengah,
                                                    text="Welcome",
                                                    font=("Times New Roman", 60, "bold"),
                                                    text_color="#d19a03")
        self.label_welcome.place(relx=0.5, rely=0.25, anchor="center")
        
        self.label_subtext = customtkinter.CTkLabel(self.frame_tengah,
                                                    text="to our projects",
                                                    font=("Arial", 25, "bold"),
                                                    text_color="#d19a03")
        self.label_subtext.place(relx=0.5, rely=0.32, anchor="center")

        # Tombol start
        self.button_start = customtkinter.CTkButton(self.frame_tengah,
                                                    text="Start",
                                                    font=("Arial", 20, "bold"),
                                                    command=self.sda,
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    corner_radius=30,
                                                    width=250,
                                                    height=50)
        self.button_start.place(relx=0.5, rely=0.6, anchor="center")

        # Tombol about us
        self.button_about = customtkinter.CTkButton(self.frame_tengah,
                                                    text="About Us",
                                                    font=("Arial", 20, "bold"),
                                                    command=self.aboutus,
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    corner_radius=30,
                                                    width=250,
                                                    height=50)
        self.button_about.place(relx=0.5, rely=0.7, anchor="center")

        # Frame about us
        self.frame_about = customtkinter.CTkFrame(self.root,fg_color="#fdf6e3")

        self.label_about = customtkinter.CTkLabel(self.frame_about,
                                                    text="Nama Anggota Kelompok",
                                                    font=("Times New Roman", 55, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_about.place(relx=0.5, rely=0.25, anchor="center")
        
        self.label_anggota1 = customtkinter.CTkLabel(self.frame_about,
                                                    text="Athallah Wildan Rafi (2417051004)",
                                                    font=("Times New Roman", 25, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_anggota1.place(relx=0.5, rely=0.35, anchor="center")

        self.label_anggota2 = customtkinter.CTkLabel(self.frame_about,
                                                    text="Wisnu Wira Winata (2417051035)",
                                                    font=("Times New Roman", 25, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_anggota2.place(relx=0.5, rely=0.4, anchor="center")

        self.label_anggota3 = customtkinter.CTkLabel(self.frame_about,
                                                    text="Rafael Putut Arli (2417051042)",
                                                    font=("Times New Roman", 25, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_anggota3.place(relx=0.5, rely=0.45, anchor="center")

        self.label_anggota4 = customtkinter.CTkLabel(self.frame_about,
                                                    text="Miqdad Dzakiy Arroyan (2417051044)",
                                                    font=("Times New Roman", 25, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_anggota4.place(relx=0.5, rely=0.5, anchor="center")

        # Tombol back AboutUs
        self.button_back1 = customtkinter.CTkButton(self.frame_about, text="Back",
                                                    font=("Times New Roman", 20, "bold"),
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    command=self.welcomepage)
        self.button_back1.place(relx=0.5, rely=0.8, anchor="center",
                                relwidth=0.2, relheight=0.04)

        # Frame SDA
        self.frame_sda = customtkinter.CTkFrame(self.root, fg_color="#fdf6e3")

        self.label_about = customtkinter.CTkLabel(self.frame_sda,
                                                    text="Score",
                                                    font=("Times New Roman", 55, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_about.place(relx=0.5, rely=0.25, anchor="center")

        # Tombol back Score
        self.button_back2 = customtkinter.CTkButton(self.frame_sda, text="Back",
                                                    font=("Times New Roman", 20, "bold"),
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    command=self.welcomepage)
        self.button_back2.place(relx=0.5, rely=0.8, anchor="center",
                                relwidth=0.2, relheight=0.04)

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

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Welcome(root)
    root.mainloop()
