import tkinter.messagebox
import customtkinter

class Main():

    def load_main_page_view(app, ctk_frame):
        ctk_frame.grid_rowconfigure(0, minsize=10)
        ctk_frame.grid_rowconfigure(1, weight=1)
        ctk_frame.grid_columnconfigure(0, weight=1)

        app.ctkl_page_title = customtkinter.CTkLabel(master=ctk_frame,
                                                    text="Sistema de Abertura de Nao Conformidades V2",
                                                    text_font=("Bebas Neue", 2*app.CONTEXT))
        app.ctkl_page_title.grid(
            row=0, column=0, pady=app.CONTEXT, padx=app.CONTEXT)

        app.ctkf_form_content = customtkinter.CTkFrame(master=ctk_frame)
        app.ctkf_form_content.grid(row=1, column=0, sticky="nswe",
                                padx=app.CONTEXT, pady=app.CONTEXT)

        # endregion

        # region FORM
        app.ctkf_form_content.grid_columnconfigure(0, weight=1)
        app.ctkf_form_content.grid_columnconfigure(1, weight=1)
        app.ctkf_form_content.grid_rowconfigure(
            0, minsize=10)     # empty row with minsize as spacing

        app.ctkl_identity = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text="Identificacao",
                                                text_font=("Roboto Medium", -16))
        app.ctkl_identity.grid(row=1, column=0,  sticky="w", pady=10, padx=0)

        app.ctks_identity = customtkinter.CTkOptionMenu(master=app.ctkf_form_content,
                                                        values=["Light", "Dark", "System"])
        app.ctks_identity.grid(row=2, column=0,  sticky="we", pady=10, padx=20)

        app.ctkl_description = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                    text="Descricao",
                                                    text_font=("Roboto Medium", -16))
        app.ctkl_description.grid(row=3, column=0,  sticky="w", pady=10, padx=0)
        app.ctke_description = customtkinter.CTkTextbox(master=app.ctkf_form_content,
                                                        height=app.CONTEXT*5, fg_color="grey25")
        app.ctke_description.insert(
            "0.0", "Escreva aqui a descricao da nao conformidade")
        app.ctke_description.grid(row=4, column=0,  sticky="we", pady=10, padx=20)

        app.ctkl_rootcause = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                    text="Analise de Causa Raiz",
                                                    text_font=("Roboto Medium", -16))
        app.ctkl_rootcause.grid(row=3, column=1,  sticky="w", pady=10, padx=20)
        app.ctke_rootcause = customtkinter.CTkTextbox(master=app.ctkf_form_content,
                                                    height=app.CONTEXT*5, fg_color="grey25")
        app.ctke_rootcause.insert(
            "0.0", "Escreva aqui a sua analise de causa raiz")
        app.ctke_rootcause.grid(row=4, column=1,  sticky="we", pady=10, padx=20)

        app.ctkl_solution = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text="Acoes corretivas",
                                                text_font=("Roboto Medium", -16))
        app.ctkl_solution.grid(row=5, column=0,  sticky="w", pady=10, padx=20)

        app.ctke_solution = customtkinter.CTkTextbox(master=app.ctkf_form_content,
                                                    height=app.CONTEXT*5, fg_color="grey25")
        app.ctke_solution.insert(
            "0.0", "Escreva aqui as acoes tomadas para solucionar o problema")
        app.ctke_solution.grid(row=6, column=0,  sticky="we", pady=10, padx=20)

        app.ctkcheck_critical = customtkinter.CTkCheckBox(master=app.ctkf_form_content,
                                                        text="Critico")
        app.ctkcheck_critical.grid(row=6, column=1,  sticky="we", pady=10, padx=20)

        app.ctkb_create = customtkinter.CTkButton(master=app.ctkf_form_content,
                                                text="Criar", command=app.save_result)
        app.ctkb_create.grid(row=7, column=0, pady=10, padx=20, sticky="nsew")

        return ctk_frame

    
