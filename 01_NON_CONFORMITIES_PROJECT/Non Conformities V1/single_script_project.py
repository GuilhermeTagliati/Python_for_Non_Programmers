import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, scrolledtext
import pandas
from PIL import Image, ImageTk
import os
import uuid

window = tk.Tk()
window.geometry('1080x720')
window.title("Sistema de abertura de Nao Conformidades")

savePath = os.path.join(os.path.dirname(__file__), '../data/data.csv')

def save_information():
    identification = ttkcombo_category.get()
    description = txt_description.get("0.0", "end")
    rootcause = txt_rootcause.get("0.0", "end")
    solution = txt_solution.get("0.0", "end")
    critical = check_state.get()
    result_dict = {
        'id': uuid.uuid4(),
        'type': str(identification).replace('\n', ''),
        'description': str(description).replace('\n', ''),
        'rootcause': str(rootcause).replace('\n', ''),
        'solution': str(solution).replace('\n', ''),
        'critical': str(critical).replace('\n', '')
    }
    df_result = pandas.DataFrame()
    if (os.stat(f'{savePath}').st_size == 0):
        df_result = pandas.DataFrame([result_dict])
    else:
        df_current = pandas.read_csv(f'{savePath}')
        df_result = pandas.concat(
            [df_current, pandas.DataFrame([result_dict])], axis=0)
    
    df_result.to_csv(f'{savePath}', index=False)
    messagebox.showinfo('Sucesso!!','Nao conformidade salva com sucesso')

tklabel_title = tk.Label(
    window, text="This is a Label", font=("Arial Bold", 16))
tklabel_title.grid(row=0, column=0, padx=0, pady=10)

tklabel_category = tk.Label(
    window, text="Categoria", font=("Arial Bold", 16))
tklabel_category.grid(row=1, column=0, padx=0, pady=10)
ttkcombo_category = ttk.Combobox(window, width=100)
ttkcombo_category['values'] = ("Category 01", "Category 02",
                               "Category 03", "Category 04", "Category 05", "Category 06")
ttkcombo_category.current(1)  # set the selected item
ttkcombo_category.grid(row=2, column=0, padx=0, pady=10)

tklabel_description = tk.Label(
    window, text="Descricao", font=("Arial Bold", 16))
tklabel_description.grid(row=3, column=0, padx=0, pady=10)

txt_description = scrolledtext.ScrolledText(window, width=100, height=5)
txt_description.grid(row=4, column=0)

tklabel_rootcause = tk.Label(
    window, text="Analise Causa Raiz", font=("Arial Bold", 16))
tklabel_rootcause.grid(row=5, column=0, padx=0, pady=10)
txt_rootcause = scrolledtext.ScrolledText(window, width=100, height=5)
txt_rootcause.grid(row=6, column=0)

tklabel_solution = tk.Label(
    window, text="Plano Corretivo", font=("Arial Bold", 16))
tklabel_solution.grid(row=7, column=0, padx=0, pady=10)
txt_solution = scrolledtext.ScrolledText(window, width=100, height=5)
txt_solution.grid(row=8, column=0)

check_state = tk.IntVar()

ttkchk = ttk.Checkbutton(window, text='Critico', var=check_state)
ttkchk.grid(row=9, column=0, padx=0, pady=10)

tkbtn_save = tk.Button(window,text='Salvar', command=save_information)
tkbtn_save.grid(row=10, column=0, padx=0, pady=10)



window.mainloop()
