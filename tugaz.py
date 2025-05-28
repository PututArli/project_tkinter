import tkinter
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Login Page")
app.geometry("800x500")

title = customtkinter.CTkLabel(app, text="Login Page", font=("Arial", 20, "bold"))
title.pack(pady=20, padx=10)




app.mainloop()
