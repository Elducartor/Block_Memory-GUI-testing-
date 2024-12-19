"""
I found this game in an "offline game" app.
I want to code it by my self to lern a little bit of GUI-Coding.
"""
import customtkinter as ctk
current_mode = "light"
def change_color():
    global current_mode
    if current_mode == "light":
        current_mode = "dark"
        return ctk.set_appearance_mode("dark")
    if current_mode == "dark":
        current_mode = "light"
        return ctk.set_appearance_mode("light")
ctk.set_appearance_mode("current_mode")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x600")
app.title("Block Memory Game")
color_changer = ctk.CTkButton(app,text="Background color change", command=lambda:change_color())
color_changer.pack(side=ctk.LEFT)
color_changer.configure(fg_color="dark blue")
app.mainloop()
