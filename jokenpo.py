import tkinter as tk
import random

def jogar(escolha_jogador):
    escolha_computador = random.randint(1, 3)

    resultado = ''
    if escolha_jogador == escolha_computador:
        resultado = "Empate!"
    elif (escolha_jogador == 1 and escolha_computador == 3) or \
         (escolha_jogador == 2 and escolha_computador == 1) or \
         (escolha_jogador == 3 and escolha_computador == 2):
        resultado = "Você ganhou!"
    else:
        resultado = "Você perdeu!"

    lbl_resultado['text'] = f"Você escolheu: {escolhas[escolha_jogador]}\n" \
                            f"Computador escolheu: {escolhas[escolha_computador]}\n" \
                            f"Resultado: {resultado}"

def escolher_pedra():
    jogar(1)

def escolher_papel():
    jogar(2)

def escolher_tesoura():
    jogar(3)

# Criar a janela principal
janela = tk.Tk()
janela.title("JOKENPO")
janela.geometry("500x400")

escolhas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

# Criar o título
lbl_titulo = tk.Label(janela, text="JOKENPO", font=("Arial", 24, "bold"))
lbl_titulo.pack(pady=20)

# Criar a label de explicação
lbl_explicativo = tk.Label(janela, text="Você está jogando contra o robô!\nQuem será o vencedor?", font=("Arial", 14))
lbl_explicativo.pack()

# Criar os botões de escolha para o jogador
btn_pedra = tk.Button(janela, text="Pedra", width=20, command=escolher_pedra, bg="gray", fg="white")
btn_pedra.pack(pady=10)

btn_papel = tk.Button(janela, text="Papel", width=20, command=escolher_papel, bg="gray", fg="white")
btn_papel.pack(pady=10)

btn_tesoura = tk.Button(janela, text="Tesoura", width=20, command=escolher_tesoura, bg="gray", fg="white")
btn_tesoura.pack(pady=10)

# Criar a label para exibir o resultado
lbl_resultado = tk.Label(janela, text="")
lbl_resultado.pack(pady=10)

# Executar o loop principal da janela
janela.mainloop()
