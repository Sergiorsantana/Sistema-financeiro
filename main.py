import sqlite3
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Conectar ao banco de dados
conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

# Função para adicionar dados
def add_income():
    source = entry_source.get()
    amount = float(entry_amount.get())
    cursor.execute("INSERT INTO income (source, amount) VALUES (?, ?)", (source, amount))
    conn.commit()
    update_chart()

def delete_income():
    cursor.execute("DELETE FROM income WHERE id = (SELECT MAX(id) FROM income)")
    conn.commit()
    update_chart()

def update_chart():
    cursor.execute("SELECT source, amount FROM income")
    data = cursor.fetchall()
    
    sources = [row[0] for row in data]
    amounts = [row[1] for row in data]
    
    ax.clear()
    ax.bar(sources, amounts, color='blue')
    ax.set_title("Analisador Financeiro de Renda")
    canvas.draw()

# Configurar a interface
tk = ctk.CTk()
tk.title("Analisador Financeiro de Renda")
tk.geometry("600x500")

entry_source = ctk.CTkEntry(tk, placeholder_text="Fonte de Renda")
entry_source.pack(pady=5)

entry_amount = ctk.CTkEntry(tk, placeholder_text="Valor")
entry_amount.pack(pady=5)

btn_add = ctk.CTkButton(tk, text="Adicionar", command=add_income)
btn_add.pack(pady=5)

btn_delete = ctk.CTkButton(tk, text="Remover Último", command=delete_income)
btn_delete.pack(pady=5)

# Criar gráfico
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=tk)
canvas.get_tk_widget().pack()
update_chart()

tk.mainloop()
conn.close()
