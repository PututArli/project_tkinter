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


        self.bg_image = customtkinter.CTkImage(Image.open("D:/SDA TKINTER/project_tkinter/welcome.png"), size=(1200, 700))
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


        self.bg_image_about = customtkinter.CTkImage(Image.open("D:/SDA TKINTER/project_tkinter/anggota.png"), size=(1200, 700))
        self.bg_label_about = customtkinter.CTkLabel(self.frame_about, image=self.bg_image_about, text="")
        self.bg_label_about.place(relx=0.5, rely=0.5, anchor="center") 

        self.label_about = customtkinter.CTkLabel(self.frame_about,
                                                    text="Nama Anggota Kelompok",
                                                    font=("Times New Roman", 55, "bold"),
                                                    text_color="white",
                                                    fg_color="transparent")
        self.label_about.place(relx=0.5, rely=0.25, anchor="center")
        
        self.label_anggota1 = customtkinter.CTkLabel(self.frame_about,
                                                    text="Athallah Wildan Rafi (2417051004)",
                                                    font=("Times New Roman", 25, "bold"),
                                                    text_color="white",
                                                    fg_color="transparent")
        self.label_anggota1.place(relx=0.5, rely=0.35, anchor="center")

        self.label_anggota2 = customtkinter.CTkLabel(self.frame_about,
                                                    text="Wisnu Wira Winata (2417051035)",
                                                    font=("Times New Roman", 25, "bold"),
                                                    text_color="white",
                                                    fg_color="transparent")
        self.label_anggota2.place(relx=0.5, rely=0.4, anchor="center")

        self.label_anggota3 = customtkinter.CTkLabel(self.frame_about,
                                                    text="Rafael Putut Arli (2417051042)",
                                                    font=("Times New Roman", 25, "bold"),
                                                    text_color="white",
                                                    fg_color="transparent")
        self.label_anggota3.place(relx=0.5, rely=0.45, anchor="center")

        self.label_anggota4 = customtkinter.CTkLabel(self.frame_about,
                                                    text="Miqdad Dzakiy Arroyan (2417051044)",
                                                    font=("Times New Roman", 25, "bold"),
                                                    text_color="white",
                                                    fg_color="transparent")
        self.label_anggota4.place(relx=0.5, rely=0.5, anchor="center")

        # Tombol back AboutUs
        self.button_back1 = customtkinter.CTkButton(self.frame_about, 
                                            text="Back",
                                            font=("Times New Roman", 20, "bold"),
                                            fg_color="#d19a03",          
                                            hover_color="#f0b400",         
                                            text_color="white",
                                            corner_radius=30,
                                            command=self.welcomepage)
        self.button_back1.place(relx=0.5, rely=0.8, anchor="center",
                        relwidth=0.2, relheight=0.04)

        

        

        # Frame SDA
        self.frame_sda = customtkinter.CTkFrame(self.root,fg_color="black",width=1000,height=1000)

        self.frame_score_kiri = customtkinter.CTkFrame(self.frame_sda,fg_color="#005EFF",width=500,height=500)
        self.frame_score_kanan = customtkinter.CTkFrame(self.frame_sda,fg_color="#FF0000", width=500,height=500)
        self.frame_atas = customtkinter.CTkFrame(self.frame_sda,fg_color="#000000",width=500, height=100)

        # Score

        self.label_division = customtkinter.CTkLabel(self.frame_atas,
                                                    text="Division:",
                                                    font=("Comic Sans", 20, "bold"),
                                                    text_color="#ffffff",
                                                    fg_color="#000000")
        self.label_division.place(relx=0.4, rely=0.075)

        self.entry_division = customtkinter.CTkEntry(self.frame_atas, width=175,
                                                     font=("Comic Sans", 20, "bold"),
                                                     text_color="#FFFFFF",
                                                     fg_color="#000000")
        self.entry_division.place(relx=0.465, rely=0.075)
        # nama kiri
        self.label_name1 = customtkinter.CTkLabel(self.frame_atas,
                                                     text="Ao",
                                                    font=("Comic Sans", 50, "bold"),
                                                    text_color="#005EFF",
                                                    fg_color="#000000")
        self.label_name1.place(relx=0.025, rely=0.40)
        self.entry_name1 = customtkinter.CTkEntry(self.frame_atas, width=150,
                                                     font=("Comic Sans", 20, "bold"),
                                                     text_color="#ffffff",
                                                     fg_color="#000000")
        self.entry_name1.place(relx=0.070, rely=0.60)

        # score kiri
        self.label_score1 = customtkinter.CTkLabel(self.frame_score_kiri,
                                                     text="0",
                                                    font=("Comic Sans", 200, "bold"),
                                                    text_color="#ffffff",
                                                    fg_color="#005EFF")
        self.label_score1.place(relx=0.15, rely=0.195)

        self.button_score11 = customtkinter.CTkButton(self.frame_score_kiri, text="+1",
                                                    font=("Comic Sans", 20, "bold"),
                                                    fg_color="#25bc1f",
                                                    hover_color="#25e61e",
                                                    text_color="white",
                                                    command=self.add_kiri)
        self.button_score11.place(relx=0.165, rely=0.5, anchor="center",
                                relwidth=0.05, relheight=0.04)
        
        self.button_score12 = customtkinter.CTkButton(self.frame_score_kiri, text="-1",
                                                    font=("Comic Sans", 20, "bold"),
                                                    fg_color="#0c28b6",
                                                    hover_color="#0d2fd8",
                                                    text_color="white",
                                                    command=self.sub_kiri)
        self.button_score12.place(relx=0.265, rely=0.5, anchor="center",
                                relwidth=0.05, relheight=0.04)

        # nama kanan
        self.label_name2 = customtkinter.CTkLabel(self.frame_atas,
                                                     text="Aka",
                                                    font=("Comic Sans", 50, "bold"),
                                                    text_color="#ff0000",
                                                    fg_color="#000000")
        self.label_name2.place(relx=0.85, rely=0.40)
        self.entry_name2 = customtkinter.CTkEntry(self.frame_atas, width=150,
                                                     font=("Comic Sans", 20, "bold"),
                                                     text_color="#ffffff",
                                                     fg_color="#000000")
        self.entry_name2.place(relx=0.745, rely=0.60)
        
        # score kanan
        self.label_score2 = customtkinter.CTkLabel(self.frame_score_kanan,
                                                     text="0",
                                                    font=("Comic Sans", 200, "bold"),
                                                    text_color="#ffffff",
                                                    fg_color="#FF0000")
        self.label_score2.place(relx=0.685, rely=0.195)
        self.button_score21 = customtkinter.CTkButton(self.frame_score_kanan, text="+1",
                                                    font=("Comic Sans", 20, "bold"),
                                                    fg_color="#25bc1f",
                                                    hover_color="#25e61e",
                                                    text_color="white",
                                                    command=self.add_kanan)
        self.button_score21.place(relx=0.695, rely=0.5, anchor="center",
                                relwidth=0.05, relheight=0.04)
        
        self.button_score22 = customtkinter.CTkButton(self.frame_score_kanan, text="-1",
                                                    font=("Comic Sans", 20, "bold"),
                                                    fg_color="#0c28b6",
                                                    hover_color="#0d2fd8",
                                                    text_color="white",
                                                    command=self.sub_kanan)
        self.button_score22.place(relx=0.805, rely=0.5, anchor="center",
                                relwidth=0.05, relheight=0.04)

        # Tombol back Score
        self.button_back2 = customtkinter.CTkButton(self.frame_sda, text="Back",
                                                    font=("Comic Sans", 20, "bold"),
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    corner_radius= 30,
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
        self.frame_atas.pack(side="top",fill="x", expand=False)
        self.frame_score_kanan.pack(side= "right",fill="both", expand=True)
        self.frame_score_kiri.pack(side= "left",fill= "both" , expand=True)

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
