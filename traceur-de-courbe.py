from sympy import diff, symbols, lambdify, sympify
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Interface graphique avec Tkinter by TOSCANI
def tracer_courbe():
    # Récupérer l'expression entrée par l'utilisateur
    expression_f = entry_function.get()
    
    # Variable symbolique
    x = symbols('x')
    
    # Calcul de la dérivée
    f_sympy = sympify(expression_f)
    f_prim = diff(f_sympy, x)
    
    # Conversion en fonction évaluable
    f_lambdified = lambdify(x, f_sympy, "numpy")
    f_prim_lambdified = lambdify(x, f_prim, "numpy")
    
    # Génération des valeurs pour x
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)
    y_prim_vals = f_prim_lambdified(x_vals)
    
    # Tracer les courbes
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="f(x)")
    ax.plot(x_vals, y_prim_vals, label="f'(x)", linestyle='--')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Courbes de la fonction et de sa dérivée")
    ax.legend()
    
    # Afficher le graphique dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    # Affichage de la dérivée dans l'interface
    label_derivative.config(text=f"La dérivée est: {f_prim}")

# Fenêtre Tkinter
window = tk.Tk()
window.title("Traceur de courbe et calcul de dérivée")

# Label et champ de saisie pour la fonction
label_function = tk.Label(window, text="Entrez l'expression de la fonction :")
label_function.pack()
entry_function = tk.Entry(window, width=50)
entry_function.pack()

# Bouton pour lancer le traçage
button_trace = tk.Button(window, text="Tracer la courbe et afficher la dérivée", command=tracer_courbe)
button_trace.pack()

# Label pour afficher la dérivée
label_derivative = tk.Label(window, text="")
label_derivative.pack()

# Boucle principale
window.mainloop()
