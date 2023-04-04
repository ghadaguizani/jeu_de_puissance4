
# 1 couleur noir
# 2 couleur blanc
# 0 case vide
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
playerName1 = ""
playerName2 = ""
l = []
number = 1
player1_is_winner = False
player2_is_winner = False
tour = 0
msg_error = ""
grille = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],]

class Player():
    def __init__(self,name):
        self.name = name

  
class GameInterface():

    def __init__(self):
        self.labels = []

    # cette action sera déclanchée en cliquant sur le boutton valider , 
    # cette fonction va afficher des message d erreur lorsque l utilisaeur ne saist pas les noms des joueurs ,
    #  et elle permet de récupérer les noms des deux joueurs en utilisant la méthode get()
    def action1(self):
        global playerName1,playerName2
        if(playerName1.get()=="" and playerName2.get()!=""):
            messagebox.showinfo("erreur","Vous devez saisir le nom de joueur 1")
        elif(playerName2.get()=="" and playerName1.get()!=""):
            messagebox.showinfo("erreur","Vous devez saisir le nom de joueur 2")
        elif (playerName1.get()=="" and playerName2.get()==""):
            messagebox.showinfo("erreur","Vous devez saisir les nom des deux joueur ")
        else :
            playerName1 = playerName1.get()
            playerName2 = playerName2.get()
            print(playerName2,playerName1)
            self.create_window2()

    def showMsgError(self,msg_error):
        messagebox.showerror("error",msg_error)
    
    def showMsg(self,msg_error):
        messagebox.showinfo("message",msg_error)
    #cette fonction permet la création d un rectangle
    def creation_rectangle(self, x, y, r, canvasName,color):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_rectangle(x0, y0, x1, y1,outline="black", fill=color)

    #cette fonction permet la création d un pion
    def creation_cercle(self,x, y, r, canvasName,color):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, outline=color, fill=color)
  
    
    #cette fonction permet la création de fenetre 1 qui demande à l utilisateur de saisir les noms des joueurs
    def create_window1(self):
        global playerName1,playerName2,my_canvas
        G1 = Game(playerName1, playerName2)  # pour initialiser le jeu

        window1 = Tk()
        window1.title("Fenetre 1")

        my_canvas = Canvas(window1,width = 400,height = 200,background = "beige")
        # .place() is a geometry manager that organizes widgets by placing them in a specific position in the parent widget
        my_canvas.place(x = 0,y = 0)
        # pack organizes widgets in blocks before placing them in the parent widget 
        my_canvas.pack()

        label1 = Label(my_canvas,text="Bienvenue",background="beige",foreground='#4f94d4',font=('italic',20))
        #pour mettre le label dans le canvas

        my_canvas.create_window(200,50,window=label1)
        playerName1 = Entry()
        playerName2 = Entry()
        label2 = Label(my_canvas,text="Le nom du joueur 1",background="beige")
        my_canvas.create_window(100,100,window=label2)
        my_canvas.create_window(220,100,window=playerName1)
        label3 = Label(my_canvas,text="Le nom du joueur 2",background="beige")
        my_canvas.create_window(100,130,window=label3)
        my_canvas.create_window(220,130,window=playerName2)

        # this will create style object
        style = Style()
        style.configure('W.TButton', font =('italic', 10, 'bold', 'underline'),foreground = '#01263a')
        button1 = Button(text = "valider",style="W.TButton",command=self.action1)
        my_canvas.create_window(220,160,window = button1)
        #playerName.pack()
        window1.mainloop() 

    
    def create_window2(self):
        global window2,my_canvas2,playerName1,playerName2,my_canvas1
        G1 = Game(playerName1, playerName2)  # pour initialiser le jeu
        window2 = Tk()
        window2.title("Fenetre 2")
        my_canvas1 = Canvas(window2,width=700,height=700,background="grey")
        my_canvas1.pack()
        my_canvas2 = Canvas(my_canvas1,width = 520, height = 450,background="#002966")
        my_canvas1.create_window(350,250,window = my_canvas2)
        #my_canvas2.pack()
        for i in range(6):
            x = []
            for j in range(7):
                x.append(self.creation_cercle(50 + j * 70, 50 + 70 * i, 30, my_canvas2,"#24A0ED"))
            l.append(x)

        label1 = Label(my_canvas1,text="Saisir le numéro de colonne",background="grey",foreground='black',font=('italic',15))
        my_canvas1.create_window(350,500,window=label1)
        columnNumber = Entry(my_canvas1)
        my_canvas1.create_window(340,530,window = columnNumber)
        style = Style()
        style.configure('W.TButton', font =('italic', 10, 'bold', 'underline'),foreground = '#01263a')
        button1 = Button(my_canvas1,text = "valider",style="W.TButton",command=lambda:G1.play(columnNumber.get()))
        my_canvas1.create_window(340,570,window = button1)

        style.configure('W.TButton', font =('italic', 10, 'bold', 'underline'),foreground = '#01263a')
        button2 = Button(my_canvas1,text = "Réinitialiser",style="W.TButton",command=lambda:G1.reset())
        my_canvas1.create_window(340,620,window = button2)
        window2.mainloop()
        
    def add_pion(self,row,column):
        global my_canvas2,playerName1,playerName2,tour,number,player1_is_winner,player2_is_winner
        G2 = Grille(playerName1,playerName2)
        
        if number == 1:
            l[int(row)][int(column)] = self.creation_cercle(50 + int(column) * 70,50 + 70 * int(row),30 ,my_canvas2,"black")
            if(G2.is_winner(row,column)):
                player1_is_winner = True
                G2.displayGrille(grille)
            else :
                print("nooo")
                number = 2
                print(" c est le tour du joueur 2")

        else :
            l[int(row)][int(column)] = self.creation_cercle(50 + int(column) * 70,50 + 70 * int(row),30 ,my_canvas2,"white")
           
            if(G2.is_winner(row,column)):
                player2_is_winner = True
            else:
                number = 1
                print(" c est le tour du joueur 1")
                tour = tour + 1
                print(tour)
             

class Grille(GameInterface):
    def __init__(self,playerName1,playerName2):

        player1 = Player(playerName1)
        player2 = Player(playerName2)
        self.players = (player1,player2) 
        #self.grille = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,2,1,1],]

    def displayGrille(self,grille):
        gr = ''
        for i in range(6):
            for j in range(7):
                gr = gr + " " + str(grille[i][j]) + " "
            gr = gr + "\n"
        print(gr)
       

    #fonction qui retourne le numéro de la ligne disponible pour la colonne donnée 
    def rowNumber(self,col):
        global grille
        row = 5
        while grille[row][int(col)]!=0 and row >= 0 :
            row = row - 1
        return row

    #fonction qui vérifie est ce qu il y a une case vide ou non dans la colonne donnée , si oui elle retourne le numéro de la ligne 
    def verif(self,col):
        if self.rowNumber(int(col)) == -1:
            return False
        else :
            return True
    
    #fonction qui ajoute le numéro 1 ou 2 à la case
    def add(self,col,number):
        global grille
        nb_h = 0
        row = self.rowNumber(int(col))
        grille[int(row)][int(col)] = number
        self.displayGrille(grille)

    #fonction qui permet de compter le nombre de pions alignés verticalement , horizontalement et en diagonal en regardant les deux sens de la direction 
    def nb_pions(self,row,column,dir_x,dir_y):
        global grille
        color = grille[int(row)][int(column)]
        result = 1
        #compter le nombre des pions dans la direction (dir_x,dir_y)
        r = row + dir_y
        c = int(column) + dir_x
        if r in range(6) and c in range(7):
            while grille[r][c] == color :
                result = result + 1
                r = r + dir_y
                c = c + dir_x
                if(r not in range(6) or c not in range(7)):
                    break
            
        
        #compter le nombre de pions dans la direction (-dir_x,-dir_y)
        r = row - dir_y
        c = int(column) - dir_x
        if r in range(6) and c in range(7):
            while grille[r][c] == color :
                result = result + 1
                r = r - dir_y
                c = c - dir_x
                if(r not in range(6) or c not in range(7)):
                    break
        
        return result 

    #cette fonction retourne true si le joueur a gagné(c est à dire le nombre de pions >=4 ) si non elle retourne False
    def is_winner(self,row,column):
        if(self.nb_pions(row,column,1,1) >= 4 or self.nb_pions(row,column,1,-1) >= 4 or self.nb_pions(row,column,1,0) >= 4 or self.nb_pions(row,column,0,1) >= 4 ):
            return True
        else:
            return False


class Game(Grille):
    
    def __init__(self,namePlayer1,namePlayer2):
        super().__init__(namePlayer1,namePlayer2)

    def play(self,column):
        G = GameInterface()
        global number,player1_is_winner,player2_is_winner,msg_error
        if tour < 21 and player1_is_winner == False and player2_is_winner == False :
            if len(str(column)) == 0 :
                msg_error = "Vous devez saisir le numéro de colonne"
                G.showMsgError(msg_error)
                print("Vous devez saisir le numéro de colonne")
            elif not str(column).isdigit():
                msg_error = "L'indice doit-être un entier "
                G.showMsgError(msg_error)
            elif(int(column) > 6 or int(column) < 0 ) :
                msg_error = "le numéro de colonne doit etre un entier entre 0 et 6"
                G.showMsgError(msg_error)
            else :
                r = self.rowNumber(int(column))
                print(r)
                if(self.verif(column)):
                    self.add(column,number)
                    self.add_pion(r,column)
                    
                else :
                    msg_error = "vous devez choisir une autre colonne"
                    G.showMsgError(msg_error)
                    print("vous devez choisir une autre colonne")

        elif(player1_is_winner == True):
            msg = "Bravoooooo le joueur  1 ayant le pion noir a gagné et le jeu est terminé Vous pouvez redémarrer le jeu en cliquant sur le boutton réinitialiser"
            G.showMsg(msg)
            print("Bravoooooo le joueur  1 a gagné")
        elif(player2_is_winner == True):
            msg = "Bravoooooo le joueur  2 ayant le piant blanc a gagné et le jeu est terminé Vous pouvez redémarrer le jeu en cliquant sur le boutton réinitialiser"
            G.showMsg(msg)
            print("Bravo le joueur 2 a gagné")
        else :
            msg = "Le jeu est terminé  et il n'y a pas de gagnant malheureusement Vous pouvez redémarrer le jeu en cliquant sur le boutton réinitialiser"
            G.showMsg(msg)
        
        

    def reset(self):
        global grille,playerName1,playerName2,player1_is_winner,player2_is_winner
        player1_is_winner = False
        player2_is_winner = False
        G1 = GameInterface()
        G2 = Grille(playerName1,playerName2)
        print("ok g")
        for i in range (6):
            for j in range(7):
                l[i][j] = G1.creation_cercle(50 + j * 70,50 + 70 * i,30 ,my_canvas2,"#24A0ED")
                grille[i][j] = 0
        G2.displayGrille(grille)



    