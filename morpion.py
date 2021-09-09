def mat_ini():
    return [ [0 for i in range(3)] for j in range(3) ]

def symbole(x):
    l=["x",".","o"]
    return l[x+1]

def affichage(m):
    s=""
    for i in range(3):
        for j in range(3):
            s+=" "+symbole(m[i][j])+" "
        s+="\n"
    print(s)

def victoire(m,x):
    v=False
    for i in range(3):
        v = v or m[i][0]==m[i][1]==m[i][2]==x or m[0][i]==m[1][i]==m[2][i]==x  
    return v or m[0][0]==m[1][1]==m[2][2]==x or m[0][2]==m[1][1]==m[2][0]==x

def lancerPartie(estPremierJoueur, _client):
    m = mat_ini()
    x = 1
    nb_tour = 1
    client = _client
    while nb_tour <= 9:
        if estPremierJoueur: 
            monTour(m, x, client)
        else : 
            tourAdverse(m, x, client)
        affichage(m)

        nb_tour += 1
        if estPremierJoueur: 
            tourAdverse(m, x, client)
        else : 
            monTour(m, x, client)

        affichage(m)


def monTour(m, x, client):
    x = 1
    reponseValide = False
    i, j = 1, 1
    while not reponseValide:
        i=int( input("Ligne = ") )
        j=int( input("Colonne = ") )

        if m[i-1][j-1] != 0:
            print("\nCase déjà occupée\n")
        else:
            reponseValide = True

    client.send(f"{i};{j}".encode("utf-8"))
    m[i-1][j-1]= x
    if victoire(m,x):
        print("Le joueur "+str(x)+" a gagné !")   

def tourAdverse(m, x, client):
    x = -1
    reponse = client.recv(255)
    i, j = reponse.decode("utf-8").split(';')
    m[int(i)-1][int(j)-1]= x
    if victoire(m,x):
        print("Le joueur "+str(x)+" a gagné !")  