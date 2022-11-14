import tkinter.messagebox
import customtkinter

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
    return ctk_frame
