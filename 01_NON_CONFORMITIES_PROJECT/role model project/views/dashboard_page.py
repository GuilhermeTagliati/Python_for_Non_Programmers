import tkinter.messagebox
import customtkinter
import pandas as pd
import os


path =  os.path.join(os.path.dirname(__file__), '../../data/data.csv')

def load_dashboard_page(app, ctk_frame):
    ctk_frame.grid_rowconfigure(0, minsize=10)
    ctk_frame.grid_rowconfigure(1, weight=1)
    ctk_frame.grid_columnconfigure(0, weight=1)

    app.ctkl_page_title = customtkinter.CTkLabel(master=ctk_frame,
                                                 text="Dashboard",
                                                 text_font=("Bebas Neue", 2*app.CONTEXT))
    app.ctkl_page_title.grid(
        row=0, column=0, pady=app.CONTEXT, padx=app.CONTEXT)

    app.ctkf_form_content = customtkinter.CTkFrame(master=ctk_frame)
    app.ctkf_form_content.grid(row=1, column=0, sticky="nswe",
                               padx=app.CONTEXT, pady=app.CONTEXT)

    app.ctkl_id = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text="Id",
                                                text_font=("Roboto Medium", -12))
    app.ctkl_id.grid(row=1, column=0,  sticky="w", pady=10, padx=0)
    
    app.ctkl_identity = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text="Type",
                                                text_font=("Roboto Medium", -12))
    app.ctkl_identity.grid(row=1, column=1,  sticky="w", pady=10, padx=0)

    app.ctkl_description = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text="Descricao",
                                                text_font=("Roboto Medium", -12))
    app.ctkl_description.grid(row=1, column=2,  sticky="w", pady=10, padx=0)
    
    app.ctkl_rootcause = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text="Causa Raiz",
                                                text_font=("Roboto Medium", -12))
    app.ctkl_rootcause.grid(row=1, column=3,  sticky="w", pady=10, padx=0)
    
    app.ctkl_solution = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text="Solucao",
                                                text_font=("Roboto Medium", -12))
    app.ctkl_solution.grid(row=1, column=4,  sticky="w", pady=10, padx=0)
    app.ctkl_critical = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text="Critico ?",
                                                text_font=("Roboto Medium", -12))
    app.ctkl_critical.grid(row=1, column=5,  sticky="w", pady=10, padx=0)

    df = pd.read_csv(path)
    for i, row in df.iterrows():
        pos = 0;
        for j, value in row.items():
            app.e = customtkinter.CTkLabel(master=app.ctkf_form_content,
                                                text=value,
                                                text_font=("Roboto Medium", -11))
            app.e.grid(row=(i+2), column=pos,  sticky="nsew", pady=10, padx=0)
            pos += 1

    return ctk_frame

