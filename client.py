import socket
import morpion

def lancerPartie():
    while True:
        tourAdverse()
        monTour()



adresseIP = "127.0.0.1"	# Ici, le poste local
port = 50000	# Se connecter sur le port 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adresseIP, port))
print("Connecté au serveur")
morpion.lancerPartie(False, client)


"""
client.send("Bonjour, je suis le client".encode("utf-8"))
reponse = client.recv(255)
print(reponse.decode("utf-8"))"""


print("Connexion fermée")
client.close()




