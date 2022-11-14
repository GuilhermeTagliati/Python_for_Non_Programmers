import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

PATH = os.path.dirname(os.path.realpath(__file__))  # Current Work Directory


class App(customtkinter.CTk):

    CONTEXT = 16
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # region LAYOUT CONFIGURATION
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.ctkf_sidebar = customtkinter.CTkFrame(master=self,
                                                   width=180,
                                                   corner_radius=0)
        self.ctkf_sidebar.grid(row=0, column=0, sticky="nswe",
                               padx=App.CONTEXT, pady=App.CONTEXT)

        self.ctkf_main = customtkinter.CTkFrame(master=self)
        self.ctkf_main.grid(row=0, column=1, sticky="nswe",
                            padx=App.CONTEXT, pady=App.CONTEXT)
        # endregion

        # region SIDEBAR CONFIGURATION
        
        self.ctkf_sidebar.grid_rowconfigure(0, minsize=10)
        self.ctkf_sidebar.grid_rowconfigure(5, weight=1)
        self.ctkf_sidebar.grid_rowconfigure(8, minsize=20)
        self.ctkf_sidebar.grid_rowconfigure(11, minsize=10)

        self.img_logo = self.load_png_img("./assets/33.png", 210, 57)
        self.ctkb_logo = customtkinter.CTkButton(master=self.ctkf_sidebar, image=self.img_logo, text="", fg_color="gray18", hover_color="gray18", corner_radius=10)
        self.ctkb_logo.grid(row=1, column=0, pady=App.CONTEXT, padx=App.CONTEXT)
        self.ctkb_create_menu = customtkinter.CTkButton(master=self.ctkf_sidebar,
                                                text="Registro",
                                                command=self.button_event, fg_color="grey30")
        self.ctkb_create_menu.grid(row=2, column=0, sticky="we")
        # endregion

        # region MAIN BODY CONFIGURATION
        self.ctkf_main.grid_rowconfigure(0, minsize=10)
        self.ctkf_main.grid_rowconfigure(1, weight=1)
        self.ctkf_main.grid_columnconfigure(0, weight=1)

        self.ctkl_page_title = customtkinter.CTkLabel(master=self.ctkf_main,
                                              text="Sistema de Abertura de Nao Conformidades V2",
                                              text_font=("Bebas Neue", 2*App.CONTEXT)) 
        self.ctkl_page_title.grid(row=0, column=0, pady=App.CONTEXT, padx=App.CONTEXT)
        
        self.ctkf_form_content = customtkinter.CTkFrame(master=self.ctkf_main)
        self.ctkf_form_content.grid(row=1, column=0, sticky="nswe",
                            padx=App.CONTEXT, pady=App.CONTEXT)
        
        #endregion

        #region FORM
        self.ctkf_form_content.grid_columnconfigure(0, weight=1)
        self.ctkf_form_content.grid_columnconfigure(1, weight=1)
        self.ctkf_form_content.grid_rowconfigure(0, minsize=10)     # empty row with minsize as spacing


        self.ctkl_identity = customtkinter.CTkLabel(master=self.ctkf_form_content,
                                              text="Identificacao",
                                              text_font=("Roboto Medium", -16)) 
        self.ctkl_identity.grid(row=1, column=0,  sticky="w", pady=10, padx=0)

        self.ctks_identity = customtkinter.CTkOptionMenu(master=self.ctkf_form_content,
                                                         values=["Light", "Dark", "System"])
        self.ctks_identity.grid(row=2, column=0,  sticky="we", pady=10, padx=20)
        
        self.ctkl_description = customtkinter.CTkLabel(master=self.ctkf_form_content,
                                              text="Descricao",
                                              text_font=("Roboto Medium", -16)) 
        self.ctkl_description.grid(row=3, column=0,  sticky="w", pady=10, padx=0)
        self.ctke_description = customtkinter.CTkTextbox(master=self.ctkf_form_content,
                                            height=App.CONTEXT*5, fg_color="grey25")
        self.ctke_description.insert("0.0","Escreva aqui a descricao da nao conformidade")
        self.ctke_description.grid(row=4, column=0,  sticky="we", pady=10, padx=20)

        self.ctkl_rootcause = customtkinter.CTkLabel(master=self.ctkf_form_content,
                                              text="Analise de Causa Raiz",
                                              text_font=("Roboto Medium", -16)) 
        self.ctkl_rootcause.grid(row=3, column=1,  sticky="w", pady=10, padx=20)
        self.ctke_rootcause = customtkinter.CTkTextbox(master=self.ctkf_form_content,
                                            height=App.CONTEXT*5, fg_color="grey25")
        self.ctke_rootcause.insert("0.0","Escreva aqui a sua analise de causa raiz")
        self.ctke_rootcause.grid(row=4, column=1,  sticky="we", pady=10, padx=20)

        self.ctkl_solution = customtkinter.CTkLabel(master=self.ctkf_form_content,
                                              text="Acoes corretivas",
                                              text_font=("Roboto Medium", -16)) 
        self.ctkl_solution.grid(row=5, column=0,  sticky="w", pady=10, padx=20)

        self.ctke_solution = customtkinter.CTkTextbox(master=self.ctkf_form_content,
                                            height=App.CONTEXT*5, fg_color="grey25")
        self.ctke_solution.insert("0.0","Escreva aqui as acoes tomadas para solucionar o problema")
        self.ctke_solution.grid(row=6, column=0,  sticky="we", pady=10, padx=20)

        self.ctkcheck_critical = customtkinter.CTkCheckBox(master=self.ctkf_form_content,
                                                     text="Critico")
        self.ctkcheck_critical.grid(row=6, column=1,  sticky="we", pady=10, padx=20)


        self.ctkb_create = customtkinter.CTkButton(master=self.ctkf_form_content,
                                                text="Criar",
                                                command=self.button_event)
        self.ctkb_create.grid(row=7, column=0, pady=10, padx=20, sticky="nsew")                           
        #endregion


    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()

    def load_png_img(self, path, img_width, img_height):
        """ Load PNG from path"""
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((img_width, img_height)))


if __name__ == "__main__":
    app = App()
    app.mainloop()
