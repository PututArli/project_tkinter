import tkinter
from tkinter import messagebox
import customtkinter
from PIL import Image


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue") 

class Welcome:
    def __init__(self, root):
        self.root = root
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Score")
        self.root.configure(bg="#fdf6e3") 
        self.frame_tengah = customtkinter.CTkFrame(root, fg_color="#ebd6bd")
        self.frame_tengah.pack(fill="both", expand=True)


        self.bg_image = customtkinter.CTkImage(Image.open("welcome.png"), size=(1200, 700))
        self.bg_label = customtkinter.CTkLabel(self.frame_tengah, image=self.bg_image, text="")
        self.bg_label.place(relx=0.5, rely=0.5, anchor="center")

        self.kiri_score = 0
        self.kanan_score = 0


        #Text welcome
        self.label_welcome = customtkinter.CTkLabel(self.frame_tengah,
                                                    text="Welcome",
                                                    font=("Times New Roman", 60, "bold"),
                                                    text_color="#d19a03",
                                                    bg_color="#f5f6ec")
        self.label_welcome.place(relx=0.5, rely=0.3, anchor="center")
        
        self.label_subtext = customtkinter.CTkLabel(self.frame_tengah,
                                                    text="to our projects",
                                                    font=("Arial", 25, "bold"),
                                                    text_color="#d19a03",
                                                    bg_color="#f5f6ec")
        self.label_subtext.place(relx=0.5, rely=0.37, anchor="center")

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
        self.button_start.place(relx=0.5, rely=0.7, anchor="center")

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
        self.button_about.place(relx=0.5, rely=0.8, anchor="center")

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

        # Score
        self.label_about = customtkinter.CTkLabel(self.frame_sda,
                                                    text="Score",
                                                    font=("Times New Roman", 30, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_about.place(relx=0.5, rely=0.045, anchor="center")

        self.label_division = customtkinter.CTkLabel(self.frame_sda,
                                                     text="Division:",
                                                    font=("Times New Roman", 20, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_division.place(relx=0.4, rely=0.075)

        self.entry_division = customtkinter.CTkEntry(self.frame_sda, width=175,
                                                     font=("Times New Roman", 20, "bold"),
                                                     text_color="#d19a03",
                                                     fg_color="#fdf6e3")
        self.entry_division.place(relx=0.465, rely=0.075)

        # nama kiri
        self.label_name1 = customtkinter.CTkLabel(self.frame_sda,
                                                     text="Name",
                                                    font=("Times New Roman", 20, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_name1.place(relx=0.125, rely=0.1)
        self.entry_name1 = customtkinter.CTkEntry(self.frame_sda, width=150,
                                                     font=("Times New Roman", 20, "bold"),
                                                     text_color="#d19a03",
                                                     fg_color="#fdf6e3")
        self.entry_name1.place(relx=0.085, rely=0.135)

        # score kiri
        self.label_score1 = customtkinter.CTkLabel(self.frame_sda,
                                                     text="0",
                                                    font=("Times New Roman", 200, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_score1.place(relx=0.1, rely=0.195)
        self.button_score11 = customtkinter.CTkButton(self.frame_sda, text="+1",
                                                    font=("Times New Roman", 20, "bold"),
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    command=self.add_kiri)
        self.button_score11.place(relx=0.115, rely=0.5, anchor="center",
                                relwidth=0.05, relheight=0.04)
        
        self.button_score12 = customtkinter.CTkButton(self.frame_sda, text="-1",
                                                    font=("Times New Roman", 20, "bold"),
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    command=self.sub_kiri)
        self.button_score12.place(relx=0.185, rely=0.5, anchor="center",
                                relwidth=0.05, relheight=0.04)

        # nama kanan
        self.label_name2 = customtkinter.CTkLabel(self.frame_sda,
                                                     text="Name",
                                                    font=("Times New Roman", 20, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_name2.place(relx=0.8, rely=0.1)
        self.entry_name2 = customtkinter.CTkEntry(self.frame_sda, width=150,
                                                     font=("Times New Roman", 20, "bold"),
                                                     text_color="#d19a03",
                                                     fg_color="#fdf6e3")
        self.entry_name2.place(relx=0.76, rely=0.135)
        
        # score kanan
        self.label_score2 = customtkinter.CTkLabel(self.frame_sda,
                                                     text="0",
                                                    font=("Times New Roman", 200, "bold"),
                                                    text_color="#d19a03",
                                                    fg_color="#fdf6e3")
        self.label_score2.place(relx=0.785, rely=0.195)
        self.button_score21 = customtkinter.CTkButton(self.frame_sda, text="+1",
                                                    font=("Times New Roman", 20, "bold"),
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    command=self.add_kanan)
        self.button_score21.place(relx=0.795, rely=0.5, anchor="center",
                                relwidth=0.05, relheight=0.04)
        
        self.button_score22 = customtkinter.CTkButton(self.frame_sda, text="-1",
                                                    font=("Times New Roman", 20, "bold"),
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    command=self.sub_kanan)
        self.button_score22.place(relx=0.865, rely=0.5, anchor="center",
                                relwidth=0.05, relheight=0.04)


        # Tombol back Score
        self.button_back2 = customtkinter.CTkButton(self.frame_sda, text="Back",
                                                    font=("Times New Roman", 20, "bold"),
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    command=self.welcomepage)
        self.button_back2.place(relx=0.95, rely=0.05, anchor="center",
                                relwidth=0.05, relheight=0.04)

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

    def add_kiri(self):
        self.kiri_score += 1
        self.label_score1.configure(text=str(self.kiri_score))

    def sub_kiri(self):
        self.kiri_score = max(0, self.kiri_score - 1)
        self.label_score1.configure(text=str(self.kiri_score))

    def add_kanan(self):
        self.kanan_score += 1
        self.label_score2.configure(text=str(self.kanan_score))

    def sub_kanan(self):
        self.kanan_score = max(0, self.kanan_score - 1)
        self.label_score2.configure(text=str(self.kanan_score))

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Welcome(root)
    root.mainloop()
