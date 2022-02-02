import random
import tkinter
import time

def replay_pendu_no_gui(): #Fonction exécutée à la fin de la fonction du pendu exécuté dans le terminal afin de savoir si la personne souhaite rejouer
    a = str(input("Souhaitez vous rejouer au jeu du pendu dans votre terminal? (O/N): "))
    if a == "O": #Oui => Rejouer
        pendu_no_gui()
    if a == "N": #Non => Retour au menu principal
        main_rp() #Boucle principale

def pendu_no_gui(): #Le pendu 
    sttime = time.time()
    lines = open("dico.txt").readlines() # Lecture du fichier de mots
    positions = ["\n\n\n\n\n\n\n", "\n   |\n   |\n   |       \n   |     \n   |     \n   |\n___|________", "   _________\n   |/      \n   |       \n   |    \n   |      \n   |\n___|________", "   _________\n   |/      |\n   |       \n   |     \n   |      \n   |\n___|________", "   _________\n   |/      |\n   |       O\n   |     \n   |      \n   |\n___|________", "   _________\n   |/      |\n   |       O\n   |       +\n   |      \n   |\n___|________", "   _________\n   |/      |\n   |       O\n   |     --+--\n   |     \n   |\n___|________", "   _________\n   |/      |\n   |       O\n   |     --+--\n   |      / \n   |\n___|________", "   _________\n   |/      |\n   |       O\n   |     --+--\n   |      / \ \n   |\n___|________"]
    rand = random.randint(0, (len(lines)-1)) #Choix d'un nombre 
    line = lines[rand] #Choix d'une ligne au hasard

    words = line.split() #Permet de séparer les arguments avec les espaces. Etant donné que les listes se font par ligne, les arugments retournés ne sont que des mots entiers ou composés.
    mw = random.choice(words) #Choix du mot au hasard

    wlen = len(mw) #Longueur du mot
    tried = 8 #Nombre d'essais (max)
    out = "" #Output afichée en temps que mot dans le terminal
    fded = "" #Lettres trouvées
    letters_al_pst = [] #Lettres trouvées

    print("Le Jeu du pendu (officiel mais pas trop)")

    for i in mw: 
        out = out +"_ " #Affichage du nombre de lettres à trouver

    print(positions.reverse()) #Afin de revoyer les lettres dans le bon ordre, je devais faire un print de cette fonction, renvoyant une erreur si elle était seule.

    while tried > 0: # temps que le nombre d'erreurs est inférieur à 8

        print (f'Voici le mot à trouver: {out}\nVous avez déjà proposé les lettres suivantes : {letters_al_pst}')
        In = str(input("Proposez une lettre: "))[0:1].upper()


        if In in mw: # Si la lettre se trouve dans le mot
            if In not in letters_al_pst: #Si la lettre ne se trouve pas dans la liste de lettres déjà proposées
                fded = fded + In #On ajoute la lettre à celles trouvées
                letter_count = mw.count(In)
                print(f"La lettre {In} est présente {letter_count} fois dans ce mot! Bravo!")
                letters_al_pst.append(In) # On append à la liste la lettre non proposée
            else:
                print(f"La lettre {In} a déjà été proposée") 
        else:
            if In not in letters_al_pst:
                letters_al_pst.append(In)
                tried = tried-1 #On retire un au nombre d'erreurs allouées
                print("-> Nope\n")
                if tried==0:
                    print(positions[0])
                if tried==1:
                    print(positions[1])
                if tried==2:
                    print(positions[2])
                if tried==3:
                    print(positions[3])
                if tried==4:
                    print(positions[4])
                if tried==5:
                    print(positions[5])
                if tried==6:
                    print(positions[6])
                if tried==7:
                    print(positions[7])
                if tried==8:
                    print(positions[8])
            else:
                print(f"La lettre {In} a déjà été proposée")
        out = ""
        for x in mw: # permet de construire le mot selon les lettres trouvées
            if x in fded:
                out += x + " "
            else:
                out += "_ "
    
        if "_" not in out: #Si il n'y a plus de lettres manquantes dans le mot
            ftime = time.time() # Temps de fin d'éxec de la partie
            inttimes = ftime - sttime #Calcul du temps de la partie
            inttimes = str(inttimes)
            inttimes = inttimes[:-13]
            print(f"Et c'est gagné!\n\nVotre temps: {inttimes} secondes")
            replay_pendu_no_gui()#Demander au joueur si il souhaite rejouer dans laversion terminal du jeu
            break
        else: #Si le mot n'a pas été complètement trouvé
            ftime = time.time()
            inttimes = ftime - sttime
            inttimes = str(inttimes)
            inttimes = inttimes[:-13]
            if tried==0: # Si le nombre de tentatives restantes est 0
                print(f"Vous n'avez pas réussi à trouver le mot. La solution était {mw}. Votre partie a duré {inttimes} secondes") # Renvoi des informations nécessaires
                replay_pendu_no_gui() #Renvoie vers la fonction de replay.
            else:
                pass

class Pendu: #On défini une classe afin de nous aider lors de la création de l'interface visuelle
    def __init__(self):
        self.time = time
        self.start_time = time.time()
        file = open("dico.txt", "r", encoding="UTF-8")
        self.essais = 10 #Nombre d'essais
        self.mots = [] #Mots du fichier dico.txt

        for i in file:
            self.mots.append(i.rstrip()) #On place dans une liste tous les mots du fichier dico.txt
        file.close() #On ferme le fichier

        self.choix = self.mots[random.randint(0, len(self.mots)-1)] # Choix d'un mot au hasard
        self.trouvé = [] 
        self.said = []

        self.won = False #On déclare l'état de la partie comme non gagnée
        self.root = tkinter.Tk()
        self.root.title("Jeu du pendu") #Titre de la fenêtre
        self.root.geometry("800x800") #Taille du display de la fenêtre (hors plein écran)
        self.root.grid() #On active la grille afin de placer les éléments plus facilement
        self.root.bind("<Return>", self.penduTick)

        self.canvas = tkinter.Canvas(self.root, width=475, height=475, background="white")
        self.canvas.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        self.champentree = tkinter.Entry(self.root) #Entrée des cractères (input de l'interface)
        self.champentree.grid(column=0, row=2, columnspan=5, padx=10, pady=10)

        self.entrybutton = tkinter.Button(self.root, text="Soumettre", command=self.penduTick) #Bouton de soumission exécutant la fonction de soumettre les lettres (également assigné par la touche Entrée)
        self.entrybutton.grid(column=1, row=2, padx= 10, pady=5)

        self.restartButton = tkinter.Button(self.root, text = "Relancer une partie", command= self.restart) # Bouton pour relancer une nouvelle partie
        self.restartButton.grid(column = 1, row = 3, padx = 10, pady=5)

        self.outButton = tkinter.Button(self.root, text="Revenir au menu", command=self.get_out)
        self.outButton.grid(column= 1, row=4, padx=10, pady=7)

        self.wordLabel = tkinter.Label(self.root, text="", font= ("Arial", 15))
        self.wordLabel.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky="NS")

        self.essaisLabel = tkinter.Label(self.root, text="")
        self.essaisLabel.grid(column=0, row=3, padx=10, pady=10)

        self.congratsLabel = tkinter.Label(self.root, text = "")
        self.congratsLabel.grid(column=0, row=4, padx=10, pady=2)

        self.timeLabel = tkinter.Label(self.root, text="")
        self.timeLabel.grid(column=3, row=2)

        self.saidLabel = tkinter.Label(self.root, text="")
        self.saidLabel.grid(column=3, row=4, padx= -10, pady= 5)

    def restart(self):
        self.win = False

        i = random.randint(0, len(self.mots)-1)
        while self.choix == self.mots[i]:
            i = random.randint(0, len(self.mots)-1)
        self.choix = self.mots[i]

        self.lettresTrouvees = []
        self.essaies = 10
        self.canvas.delete('all')
        self.wordLabel.configure(text = "_ "*(len(self.choix))) #Nombre de tirets du bas en fonction du nombre de lettres dans le mot
        self.essaisLabel.configure(text = "Il vous reste 10 essais") # Affiche le nombre d'essais
        self.congratsLabel.configure(text="")
        self.saidLabel.configure(text=self.said)
        self.root.update_idletasks() #On update les taches de l'interface graphique

    def get_out(self):
        self.congratsLabel.configure(text="Merci d'avoir joué")
        self.root.destroy()
        main_rp()

    def penduTick(self, event = None) : 
        if self.essaies > 0 and not self.win:
            self.congratsLabel.configure(text="")
            self.saidLabel.configure(text=self.said)
            guess = self.champentree.get() # récupérer le texte de l'input
            self.champentree.delete(0, len(guess))
            if len(guess) != 1: #On vérifie si le joueur ne rentre q'un seul caractère
                guess = ""
                self.congratsLabel.configure(text="Merci de ne rentrer qu'un seul caractère")
            for c in guess.lower():
                self.said.append(c)
                if c in self.choix.lower() :
                    if c not in self.lettresTrouvees :
                        self.lettresTrouvees.append(c)
                else:
                    try:
                        int(c)
                    except:
                        self.essaies -= 1
                        self.drawNext()
                
                if self.essaies > 0 :
                    complete = True
                    for c in self.choix.lower() :
                        if c not in self.lettresTrouvees :
                            complete = False
                    
                    if complete : 
                        self.win = True
                        self.congratsLabel.configure(text= "Vous avez gagné!")
                        finish_time = self.time.time()
                        time = finish_time - self.start_time
                        time = str(time)
                        time = time[:-13]
                        self.timeLabel.configure(text="Votre temps : " + time + " secondes")
                        break

        newText = ""
        for i in self.choix :
            if i.lower() in self.lettresTrouvees : 
                newText += i
            else : 
                newText += "_ "
                
        self.wordLabel.configure(text=newText)

        if self.essaies <= 0 :
            self.wordLabel.configure(text = self.choix)
            self.congratsLabel.configure(text = "Vous avez perdu")
            finish_time = self.time.time()
            time = finish_time - self.start_time
            time = str(time)
            time = time[:-13] #Enlevre toutes les décimales sauf les deux dernières
            self.timeLabel.configure(text="Votre temps : " + time + ' secondes')
            self.root.update_idletasks()

        self.essaisLabel.configure(text= "Il vous reste " + str(self.essaies) + " essais")
        self.root.update_idletasks()

    def start(self) : 
        self.restart()
        self.root.mainloop()

    def drawNext(self): #Création du canvas modélisant le pendu
        self.canvas.delete(all)
        if self.essaies < 10 :
            self.canvas.create_line(10, 290, 280, 290, width=10) 
        if self.essaies < 9 :
            self.canvas.create_line(30, 290, 30, 40, width=10)
        if self.essaies < 8 :
            self.canvas.create_line(30, 45, 200, 45, width=8)
        if self.essaies < 7 :
            self.canvas.create_line(180, 45, 180, 120, width=8)
        if self.essaies < 6 :
            self.canvas.create_oval(170, 120, 190, 140, width=4)
        if self.essaies < 5 :
            self.canvas.create_line(180, 140, 180, 200, width=4)
        if self.essaies < 4 :
            self.canvas.create_line(180, 200, 160, 240, width=4)
        if self.essaies < 3 :
            self.canvas.create_line(180, 200, 200, 240, width=4)
        if self.essaies < 2 :
            self.canvas.create_line(180, 150, 160, 190, width=4)
        if self.essaies < 1 :
            self.canvas.create_line(180, 150, 200, 190, width=4)

print('>>>> Bienvenue dans le pendu <<<< \n\nDifférentes options s\'offrent à vous selon le type d\'interface que vous souhaitez:\n\n1 : Pendu dans le terminal (Une interface légère et peu énergivore)\n2 : Jeu du pendu avec une interface graphique (Un jeu avec des graphismes et une interface)\n3 : Sortir du jeu')#Démarrage
def main():
    i = int(input("Renseignez votre choix: "))
    if i == 1:
        pendu_no_gui()
    elif i == 2:
        pendu = Pendu()
        pendu.start()
    elif i == 3:
        print("Merci d'avoir joué!")
        exit()

def main_rp():
    print('>>>> Bienvenue dans le pendu <<<< \n\nDifférentes options s\'offrent à vous selon le type d\'interface que vous souhaitez:\n\n1 : Pendu dans le terminal (Une interface légère et peu énergivore)\n2 : Jeu du pendu avec une interface graphique (Un jeu avec des graphismes et une interface)\n3 : Sortir du jeu')#Redémarrage
    i = int(input("Renseignez votre choix: "))
    if i == 1:
        pendu_no_gui()
    elif i == 2:
        pendu = Pendu()
        pendu.start()
    elif i == 3:
        print("Merci d'avoir joué!")
        exit()
main()