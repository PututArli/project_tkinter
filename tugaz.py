import tkinter
from tkinter import messagebox
import customtkinter


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue") 

class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
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
        self.frame_about = customtkinter.CTkFrame(self.root)

        self.canvas_about = customtkinter.CTkCanvas(self.frame_about, width=400, height=100, highlightthickness=0)
        self.canvas_about.place(relx=0.5, rely=0.2, anchor="center")
        self.canvas_about.create_text(200, 50, text="Perkenalan",
                                      font=("Times New Roman", 50, "bold"),
                                      fill="#d19a03")

        self.button_back1 = customtkinter.CTkButton(self.frame_about, text="Back",
                                                    font=("Times New Roman", 20, "bold"),
                                                    command=self.welcomepage)
        self.button_back1.place(relx=0.5, rely=0.8, anchor="center",
                                relwidth=0.2, relheight=0.04)

        # Frame SDA
        self.frame_sda = customtkinter.CTkFrame(self.root)

        self.canvas_sda = customtkinter.CTkCanvas(self.frame_sda, width=400, height=100, highlightthickness=0)
        self.canvas_sda.place(relx=0.5, rely=0.2, anchor="center")
        self.canvas_sda.create_text(200, 50, text="SDA",
                                    font=("Times New Roman", 50, "bold"),
                                    fill="#d19a03")

        self.button_back2 = customtkinter.CTkButton(self.frame_sda, text="Back",
                                                    font=("Times New Roman", 20, "bold"),
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

    def Login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "WisnuXiaomi" and password == "635":
            messagebox.showinfo("Login Sukses!", "Selamat datang")
        else:
            messagebox.showerror("Login Gagal", "Coba lagi!")

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Welcome(root)
    root.mainloop()
