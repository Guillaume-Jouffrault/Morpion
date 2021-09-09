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

m = mat_ini()

cp = 0

while cp <= 7 :
    affichage(m)
    if cp%2 :
        x=1
    else :
        x=-1
    i=int( input("Ligne = ") )
    j=int( input("colonne = ") )

    if m[i-1][j-1] != 0:
        print("\nCase déjà occupée\n")
    else:
        m[i-1][j-1]= x
        cp+=1
    if victoire(m,x):
        print("Le joueur "+str(x)+" a gagné !")    
affichage(m)