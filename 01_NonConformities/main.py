import customtkinter
import tkinter
from PIL import Image, ImageTk
import os

# region Initial Setup
PATH = os.path.dirname(os.path.realpath(__file__))  # Current File

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

# endregion


class App(customtkinter.CTk):
    # region Properties
    CONTEXT = 16
    WIDTH = 1280
    HEIGHT = 720
    # endregion

    def __init__(self):
        super().__init__()
        self.geometry("1280x720")  # Small Display
        self.title("Brains DP - Sistema de Abertura de Nao Conformidades")
        self.grid_rowconfigure(0, weight=self.CONTEXT, minsize=self.CONTEXT)
        self.grid_columnconfigure(0, weight=self.CONTEXT, minsize=self.CONTEXT)

        image = Image.open(
            PATH + "/assets/background.jpg").resize((self.WIDTH, self.HEIGHT))
        self.img_bg = ImageTk.PhotoImage(image)
        self.tkl_bg = tkinter.Label(master=self, image=self.img_bg)
        self.tkl_bg.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.ctkf_body = customtkinter.CTkFrame(
            master=self, corner_radius=15, fg_color="gray18")
        self.ctkf_body.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.ctkf_body.grid_columnconfigure(1, weight=1)
        self.ctkf_body.grid_columnconfigure(1, weight=1)

        self.img_logo = self.load_png_img("./assets/33.png", 280, 77)
        self.ctkb_logo = customtkinter.CTkButton(
            master=self.ctkf_body, image=self.img_logo, text="", fg_color="gray18", hover_color="gray18", corner_radius=10)
        self.ctkb_logo.grid(row=0, column=0, columnspan=1,
                            padx=20, pady=10, sticky="e")

        self.ctkl_h1 = customtkinter.CTkLabel(
            master=self.ctkf_body, fg_color="gray18", text="Sistema de nao Conformidades")
        self.ctkl_h1.grid(row=0, column=0, columnspan=1,
                          padx=20, pady=10, sticky="e")

    # region Utilities Functions
    def load_png_img(self, path, img_width, img_height):
        """ Load PNG from path"""
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((img_width, img_height)))
    # endregion


if __name__ == "__main__":
    app = App()
    app.mainloop()
