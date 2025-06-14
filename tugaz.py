import tkinter
from tkinter import messagebox
import customtkinter
from PIL import Image
import time, os, csv


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue") 

class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Score")
        self.root.configure(bg="#fdf6e3") 
        self.frame_tengah = customtkinter.CTkFrame(root, fg_color="#ebd6bd")
        self.frame_tengah.pack(fill="both", expand=True)


        self.bg_image = customtkinter.CTkImage(Image.open("welcome.png"), size=(1920, 1080))
        self.bg_label = customtkinter.CTkLabel(self.frame_tengah, image=self.bg_image, text="")
        self.bg_label.place(relx=0.5, rely=0.5, anchor="center")

        self.kiri_score = 0
        self.kanan_score = 0

        self.running = False
        self.start_timer = 0
        self.waktu = 180
        self.match_count = 1

        self.status_ao = "Normal"
        self.status_aka = "Normal"

        #Text welcome
        self.label_welcome = customtkinter.CTkLabel(self.frame_tengah,
                                                    text="Welcome",
                                                    font=("Times New Roman", 100, "bold"),
                                                    text_color="#d19a03",
                                                    bg_color="#f5f6ec")
        self.label_welcome.place(relx=0.5, rely=0.25, anchor="center")
        
        self.label_subtext = customtkinter.CTkLabel(self.frame_tengah,
                                                    text="to our projects",
                                                    font=("Arial", 55, "bold"),
                                                    text_color="#d19a03",
                                                    bg_color="#f5f6ec")
        self.label_subtext.place(relx=0.5, rely=0.35, anchor="center")

        # Tombol start
        self.button_start = customtkinter.CTkButton(self.frame_tengah,
                                                    text="Start",
                                                    font=("Arial", 40, "bold"),
                                                    command=self.sda,
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    corner_radius=30,
                                                    width=250,
                                                    height=70)
        self.button_start.place(relx=0.5, rely=0.7, anchor="center")

        # Tombol about us
        self.button_about = customtkinter.CTkButton(self.frame_tengah,
                                                    text="About Us",
                                                    font=("Arial", 40, "bold"),
                                                    command=self.aboutus,
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    corner_radius=30,
                                                    width=250,
                                                    height=70)
        self.button_about.place(relx=0.5, rely=0.8, anchor="center")

        self.button_exit = customtkinter.CTkButton(self.frame_tengah,
                                                    text="Exit",
                                                    font=("Arial", 40, "bold"),
                                                    command=self.exit,
                                                    fg_color="#d19a03",
                                                    hover_color="#f0b400",
                                                    text_color="white",
                                                    corner_radius=30,
                                                    width=250,
                                                    height=70)
        self.button_exit.place(relx=0.5, rely=0.9, anchor="center")

        # Frame about us
        self.frame_about = customtkinter.CTkFrame(self.root,fg_color="#4e503f")


        self.bg_image_about = customtkinter.CTkImage(Image.open("anggota.png"), size=(1920, 1080))
        self.bg_label_about = customtkinter.CTkLabel(self.frame_about, image=self.bg_image_about, text="")
        self.bg_label_about.place(relx=0.5, rely=0.5, anchor="center") 

    
        # Tombol back AboutUs
        self.button_back1 = customtkinter.CTkButton(self.frame_about, 
                                            text="Back",
                                            font=("Comic Sans", 30, "bold"),
                                            fg_color="#4e503f",          
                                            hover_color="#353434",         
                                            text_color="white",
                                            corner_radius=35,
                                            command=self.welcomepage)
        self.button_back1.place(relx=0.88, rely=0.95, anchor="center",
                        relwidth=0.1, relheight=0.04)

        

        # Frame SDA
        self.frame_sda = customtkinter.CTkFrame(self.root,fg_color="black",width=1000,height=1000)

        self.frame_score_kiri = customtkinter.CTkFrame(self.frame_sda,fg_color="#005EFF",width=500,height=500)
        self.bg_image_benderakiri = customtkinter.CTkImage(Image.open("blue flag.png"), size=(250, 250))
        self.bg_label_benderakiri = customtkinter.CTkLabel(self.frame_score_kiri, image=self.bg_image_benderakiri, text="")
        self.bg_label_benderakiri.place(relx=0.7, rely=0.4, anchor="center")

        self.frame_score_kanan = customtkinter.CTkFrame(self.frame_sda,fg_color="#FF0000", width=500,height=500)
        self.bg_image_benderakanan = customtkinter.CTkImage(Image.open("red flag.png"), size=(250, 250))
        self.bg_label_benderakanan = customtkinter.CTkLabel(self.frame_score_kanan, image=self.bg_image_benderakanan, text="")
        self.bg_label_benderakanan.place(relx=0.3, rely=0.4, anchor="center")

        self.frame_atas = customtkinter.CTkFrame(self.frame_sda,fg_color="#000000",width=500, height=100)
        self.frame_bawah = customtkinter.CTkFrame(self.frame_sda, fg_color="#000000",width=500, height=100)
    


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
                                                    font=("Comic Sans", 250, "bold"),
                                                    text_color="#ffffff",
                                                    fg_color="#005EFF")
        self.label_score1.place(relx=0.15, rely=0.195)

        self.button_score11 = customtkinter.CTkButton(self.frame_score_kiri, text="+1",
                                                    font=("Comic Sans", 30, "bold"),
                                                    fg_color="#25bc1f",
                                                    hover_color="#25e61e",
                                                    text_color="white",
                                                    command=self.add_kiri)
        self.button_score11.place(relx=0.165, rely=0.55, anchor="center",
                                relwidth=0.05, relheight=0.04)
        
        self.button_score12 = customtkinter.CTkButton(self.frame_score_kiri, text="-1",
                                                    font=("Comic Sans", 30, "bold"),
                                                    fg_color="#0c28b6",
                                                    hover_color="#0d2fd8",
                                                    text_color="white",
                                                    command=self.sub_kiri)
        self.button_score12.place(relx=0.265, rely=0.55, anchor="center",
                                relwidth=0.05, relheight=0.04)
        
        self.labeltimerkiri = customtkinter.CTkLabel(self.frame_score_kiri,
                                                 text= "03:00",
                                                 font=("Comic Sans", 70),
                                                 text_color="white")
        self.labeltimerkiri.place(relx=0.665, rely=0.75, anchor="center",relwidth=0.55, relheight=0.14)
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
                                                    font=("Comic Sans", 250, "bold"),
                                                    text_color="#ffffff",
                                                    fg_color="#FF0000")
        self.label_score2.place(relx=0.685, rely=0.195)
        self.button_score21 = customtkinter.CTkButton(self.frame_score_kanan, text="+1",
                                                    font=("Comic Sans", 30, "bold"),
                                                    fg_color="#25bc1f",
                                                    hover_color="#25e61e",
                                                    text_color="white",
                                                    command=self.add_kanan)
        self.button_score21.place(relx=0.695, rely=0.55, anchor="center",
                                relwidth=0.05, relheight=0.04)
        
        self.button_score22 = customtkinter.CTkButton(self.frame_score_kanan, text="-1",
                                                    font=("Comic Sans", 30, "bold"),
                                                    fg_color="#0c28b6",
                                                    hover_color="#0d2fd8",
                                                    text_color="white",
                                                    command=self.sub_kanan)
        self.button_score22.place(relx=0.805, rely=0.55, anchor="center",
                                relwidth=0.05, relheight=0.04)
        
        self.labeltimerkanan = customtkinter.CTkLabel(self.frame_score_kanan,
                                                 text= "03:00",
                                                 font=("Comic Sans", 70),
                                                 text_color="white")
        self.labeltimerkanan.place(relx=0.345, rely=0.75, anchor="center",relwidth=0.55, relheight=0.14)

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
        
        #tombol kiri
        self.button_timer_start = customtkinter.CTkButton(self.frame_bawah,
                                                    text= "Start",
                                                    font=("Comic Sans",24,"bold"),
                                                    command=self.start_timer_fn,
                                                    width= 100,
                                                    corner_radius=10,
                                                    fg_color="#25bc1f",
                                                    hover_color="#25e61e")
        self.button_timer_start.pack(side="left",padx=80)


        self.button_shikkaku_ao = customtkinter.CTkButton(self.frame_bawah, text="Shikkaku",
                                                          font=("Arial", 24, "bold"),
                                                          fg_color="#0047ab", text_color="white",
                                                          width=100, corner_radius=10,
                                                          command=self.shikaku_ao)
        self.button_shikkaku_ao.pack(side="left", padx=80)

        self.button_kikken_ao = customtkinter.CTkButton(self.frame_bawah, text="Kikken",
                                                        font=("Arial", 24, "bold"),
                                                        fg_color="#0047ab", text_color="white",
                                                        width=100, corner_radius=10,
                                                        command=self.kikken_ao)
        self.button_kikken_ao.pack(side="left", padx=80)

        # Tombol Done di tengah
        self.button_done = customtkinter.CTkButton(self.frame_bawah, text="Done",
                                                   font=("Arial", 24, "bold"),
                                                   fg_color="limegreen", text_color="white",
                                                   width=140, corner_radius=10,
                                                   command=self.done)
        self.button_done.pack(side="left", padx=80, pady=10)

        # Tombol kanan
        self.button_shikkaku_aka = customtkinter.CTkButton(self.frame_bawah, text="Shikkaku",
                                                           font=("Arial", 24 , "bold"),
                                                           fg_color="#FF0000", text_color="white",
                                                           width=100, corner_radius=10,
                                                           command=self.shikaku_aka,
                                                           hover_color="#8b0000")
        self.button_shikkaku_aka.pack(side="left", padx=80)

        self.button_kikken_aka = customtkinter.CTkButton(self.frame_bawah, text="Kikken",
                                                         font=("Arial", 24 , "bold"),
                                                         fg_color="#FF0000", text_color="white",
                                                         width=100, corner_radius=10,
                                                         command=self.kikken_aka,
                                                         hover_color="#8b0000")
        self.button_kikken_aka.pack(side="left", padx=80)

        self.button_reset = customtkinter.CTkButton(self.frame_bawah, text="Reset",
                                                    font=("Arial", 24, "bold"),
                                                    command= self.reset_timer,
                                                    fg_color="red", text_color="white",
                                                    width=100, corner_radius=10)
        self.button_reset.pack(side="left", padx=80, pady=10)

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
        self.frame_bawah.pack(side="bottom", fill="x", expand=False)
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

    def shikaku_ao(self):
        self.status_ao = "Shikkaku"
        self.kiri_score = 0
        messagebox.showinfo("Shikkaku Ao", "Ao didiskualifikasi. Aka menang otomatis.")
        self.label_score1.configure(text="0")

    def kikken_ao(self):
        self.status_ao = "Kikken"
        self.kiri_score = 0
        messagebox.showinfo("Kikken Ao","Peserta tidak dapat hadir")
        self.label_score1.configure(text="0")

    def shikaku_aka(self):
        self.status_aka = "Shikkaku"
        self.kanan_score = 0
        messagebox.showinfo("Shikkaku Aka", "Aka didiskualifikasi. Ao menang otomatis.")
        self.label_score2.configure(text="0")

    def kikken_aka(self):
        self.status_aka = "Kikken"
        self.kanan_score = 0
        self.label_score2.configure(text="0")

    def done(self):
        division = self.entry_division.get()
        nama1 = self.entry_name1.get()
        nama2 = self.entry_name2.get()
        
        if not division or not nama1 or not nama2:
            messagebox.showwarning("Input Error", "Isi semua kolom!.")
            return
        
        score_ao = self.kiri_score
        score_aka = self.kanan_score

        if self.status_ao in ["Shikkaku", "Kikken"]:
            hasil = f"{nama2} (Aka) menang karena {self.status_ao.lower()} Ao"
        elif self.status_aka in ["Shikkaku", "Kikken"]:
            hasil = f"{nama1} (Ao) menang karena {self.status_aka.lower()} Aka"
        elif score_ao > score_aka:
            hasil = f"{nama1} (Ao) adalah pemenangnya!"
        elif score_ao < score_aka:
            hasil = f"{nama2} (Aka) adalah pemenangnya!"
        else:
            hasil = "Seri!"

        nama_file = "hasil_match.csv"
        file_ada = os.path.isfile(nama_file)
        with open(nama_file, mode="a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_ada:
                writer.writerow([
                    "Match", "Division", "Ao (Blue)", "Score Ao", 
                    "Aka (Red)", "Score Aka", "Hasil Akhir"])
               
            writer.writerow([
                self.match_count, division, nama1, score_ao, nama2, score_aka, hasil])
        
        messagebox.showinfo("Hasil Pertandingan:",
                            f"Match: {self.match_count}\nDivisi: {division}\n"
                            f"{nama1} (Ao): {score_ao} Poin\n{nama2} (Aka): {score_aka} Poin\n"
                            f"Hasil Akhir: {hasil}")
        
        self.match_count += 1

        self.status_ao = "Normal"
        self.status_aka = "Normal"
        self.running = False
        
        
    def start_time(self):
        if self.running:
            self.running = True
            self.start_timer_kiri = time.time() - self.start_time
            self.start_timer_kanan = time.time() - self.start_time

    
    def start_timer_fn(self):
        if not self.running:
            self.running = True
            self.start_time_value = time.time() 
            self.update_time()

    def update_time(self):
        if self.running:
            waktu = time.time() - self.start_time_value
            sisa = max(0,self.waktu - waktu)  
            total_detik= int(sisa + 0.5)
            minutes = int(sisa // 60)
            seconds = int(sisa % 60)
            if sisa <=0 :
                self.labeltimerkiri.configure(text="00:00")
                self.labeltimerkanan.configure(text="00:00")
                self.running = False
                return
            self.labeltimerkiri.configure(text=f"{minutes:02}:{seconds:02}")
            self.labeltimerkanan.configure(text=f"{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_time)
    def reset_timer(self):
        self.running = False
        self.waktu = 180
        self.labeltimerkiri.configure(text="03:00")
        self.labeltimerkanan.configure(text="03:00")
        self.kanan_score = 0
        self.kiri_score = 0
        self.label_score1.configure(text="0")
        self.label_score2.configure(text="0")

    def exit(self):
        root.destroy()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Welcome(root)
    root.mainloop()
