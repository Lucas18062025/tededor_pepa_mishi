import tkinter as tk
from tkinter import messagebox

# Variables del Juego.
player = "X"
game_over = False

# Funcion para verificar si hay un ganador.
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def botton_chick(row, col):
    global player, game_over
    if buttons[row][col]["text"] == "" and not game_over:
        buttons[row][col]["text"] = player
        buttons[row][col]["bg"] = "#37474F" if player == "X" else "#587380"
        if check_winner():
            game_over = True
            messagebox.showinfo(title = "TaTeTí", message = f"¡El jugador {player} ha ganado!")
            game_over = True
        else:
            player = "O" if player == "X" else "X"
            

#resetear el juego
def reset_game():
    global player, game_over
    player = "X"
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col]["bg"] = "#263238"

# Configuracion de la ventana principal.
root = tk.Tk()
root.title("TaTeTí")
root.geometry("400x450")
root.configure(bg="#263238")
frame = tk.Frame(root, bg="#263238")
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(frame, text="", font=("Arial", 40), width=5, height=2, bg="#263238", fg="white", command=lambda r=row, c=col: botton_chick(r, c))

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)
reset_button = tk.Button(root, text="Reiniciar", font=("Arial", 15), bg="#37474F", fg="white", command=reset_game)
frame.pack(pady=20)
reset_button.pack(pady=10)


root.mainloop()