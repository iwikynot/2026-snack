"""
Programme Snake version 1

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 

# On crée un environnement Tkinter
tk = Tk()

def compiteNextFrame(numFrame):
    print(numFrame)
    numFrame = numFrame + 1
    
    can delete('all')
   
# On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
# Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
# intégré (ici l'environnement Tkinter)
# Les trois autres paramètres permettent de spécifier la taille et la couleur
# de fond du canevas
can = Canvas(tk, width=500, height=500, bg='black')

# On affiche le canevas
can.pack()

can.create_rectangle(500, 100, 400, 20, outline='yellow', fill='green')
can.create_oval(100, 200, 120, 120, outline='red', fill='blue')

# lancement de la boucle principale qui écoute les évènements (claviers...)
tk.mainloop() # Cet appel doit être la derniere instruction du programme




