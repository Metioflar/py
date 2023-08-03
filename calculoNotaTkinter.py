import tkinter as tk

from tkinter import messagebox


# Função para calcular a média aritmética das notas

def calcular_media(notas):
    total = sum(notas)

    media = total / len(notas)

    return media


# Função para adicionar a nota à lista

def adicionar_nota():
    nome_aluno = nome_entry.get()

    nota_str = nota_entry.get()

    if nota_str.replace('.', '', 1).isdigit():

        nota = float(nota_str)

        if nota >= 0:

            if nome_aluno not in alunos_notas:
                alunos_notas[nome_aluno] = []

            alunos_notas[nome_aluno].append(nota)

            nota_entry.delete(0, tk.END)

            nota_listbox.insert(tk.END, f"{nome_aluno}: {nota}")  # Adiciona o nome e a nota à Listbox

        else:

            calcular_medias()

    else:

        messagebox.showerror("Erro", "Insira um valor numérico válido.")


# Função para calcular e exibir as médias dos alunos

def calcular_medias():
    resultado_text.config(state=tk.NORMAL)

    resultado_text.delete('1.0', tk.END)

    for nome_aluno, notas in alunos_notas.items():
        media_aluno = calcular_media(notas)

        resultado_text.insert(tk.END, f"Média de {nome_aluno}: {media_aluno:.2f}\n")

    resultado_text.config(state=tk.DISABLED)


# Inicializar o dicionário de alunos e notas

alunos_notas = {}

app = tk.Tk()

app.title("Calculadora de Média de Alunos")

# Item B) Loop while para inserir as notas dos alunos

nome_label = tk.Label(app, text="Insira o nome do aluno:")

nome_label.pack()

nome_entry = tk.Entry(app)

nome_entry.pack()

nota_label = tk.Label(app, text="Insira a nota do aluno:")

nota_label.pack()

nota_entry = tk.Entry(app)

nota_entry.pack()

adicionar_button = tk.Button(app, text="Adicionar Nota", command=adicionar_nota)

adicionar_button.pack()

nota_listbox = tk.Listbox(app)

nota_listbox.pack()

# Item C) Loop for para imprimir a média de cada aluno

calcular_button = tk.Button(app, text="Calcular Médias", command=calcular_medias)

calcular_button.pack()

resultado_text = tk.Text(app, state=tk.DISABLED, height=10, width=30)

resultado_text.pack()

app.mainloop()
