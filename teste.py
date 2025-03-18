import tkinter as tk

# Função para atualizar o visor
def on_click(button_text):
    current_text = entry_var.get()
    entry_var.set(current_text + button_text)

# Função para calcular o resultado
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except:
        entry_var.set("Erro")

# Função para limpar o visor
def clear():
    entry_var.set("")

# Função para capturar entrada do teclado
def on_key_press(event):
    key = event.char
    # Ignorar teclas especiais (como Shift, Ctrl, etc.)
    if key in "0123456789+-*/.":
        entry_var.set(entry_var.get() + key)
        return "break"  # Impede o comportamento padrão do widget Entry
    elif key == "\r":  # Tecla "Enter" para calcular
        calculate()
    elif key == "\x08":  # Tecla "Backspace" para apagar
        entry_var.set(entry_var.get()[:-1])

# Criar a janela
root = tk.Tk()
root.title("Calculadora")

# Criar uma variável para o visor
entry_var = tk.StringVar()

# Criar o visor
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)
entry.bind("<KeyPress>", on_key_press)  # Captura eventos do teclado

# Definir botões
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Criar botões na interface
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "=":
            btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=calculate)
        elif text == "C":
            btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=clear)
        else:
            btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: on_click(t))
        btn.grid(row=i + 1, column=j, padx=5, pady=5)

# Focar no campo de entrada para capturar teclado
entry.focus()

# Rodar a interface gráfica
root.mainloop()
