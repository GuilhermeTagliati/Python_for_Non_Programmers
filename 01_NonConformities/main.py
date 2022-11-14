import customtkinter
import os
import pandas

from PIL import Image, ImageTk
from views import main_page, dashboard_page

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
        self.ctkb_logo = customtkinter.CTkButton(
            master=self.ctkf_sidebar, image=self.img_logo, text="", fg_color="gray18", hover_color="gray18", corner_radius=10)
        self.ctkb_logo.grid(
            row=1, column=0, pady=App.CONTEXT, padx=App.CONTEXT)
        self.ctkb_create_menu = customtkinter.CTkButton(master=self.ctkf_sidebar,
                                                        text="Registro",
                                                        command=self.load_main_page, fg_color="grey30")
        self.ctkb_create_menu.grid(row=2, column=0, sticky="we")

        self.ctkb_dashboard_menu = customtkinter.CTkButton(master=self.ctkf_sidebar,
                                                           text="Dashboard",
                                                           command=self.load_dashboard_page, fg_color="grey30")
        self.ctkb_dashboard_menu.grid(row=3, column=0, sticky="we")
        # endregion

    def load_main_page(self):
        self.ctkf_main = customtkinter.CTkFrame(master=self)
        self.ctkf_main.grid(row=0, column=1, sticky="nswe",
                            padx=App.CONTEXT, pady=App.CONTEXT)
        self.ctkf_main = main_page.Main.load_main_page_view(
            app=App, ctk_frame=self.ctkf_main)

    def load_dashboard_page(self):
        self.ctkf_main = customtkinter.CTkFrame(master=self)
        self.ctkf_main.grid(row=0, column=1, sticky="nswe",
                            padx=App.CONTEXT, pady=App.CONTEXT)
        self.ctkf_main = dashboard_page.load_dashboard_page(
            app=App, ctk_frame=self.ctkf_main)

    def on_closing(self, event=0):
        self.destroy()

    def load_png_img(self, path, img_width, img_height):
        """ Load PNG from path"""
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((img_width, img_height)))

    def save_result():
        identification = App.ctks_identity.get()
        description = App.ctke_description.textbox.get("0.0", "end")
        rootcause = App.ctke_rootcause.textbox.get("0.0", "end")
        solution = App.ctke_solution.textbox.get("0.0", "end")
        critical = App.ctkcheck_critical.get()

        result_dict = {
            'id': str(identification).replace('\n', ''),
            'description': str(description).replace('\n', ''),
            'rootcause': str(rootcause).replace('\n', ''),
            'solution': str(solution).replace('\n', ''),
            'critical': str(critical).replace('\n', '')
        }
        df_result = pandas.DataFrame()
        if (os.stat("./data/data.csv").st_size == 0):
            df_result = pandas.DataFrame([result_dict])
        else:
            df_current = pandas.read_csv("./data/data.csv")
            df_result = pandas.concat(
                [df_current, pandas.DataFrame([result_dict])], axis=0)
        print(df_result)
        df_result.to_csv(r'data/data.csv', index=False)


if __name__ == "__main__":
    app = App()
    app.mainloop()
