import socket
import morpion

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 50000))	# Écoute sur le port 50000
serveur.listen(5)
print("Serveur lancé, en attente d'un adversaire ...")
print('\n')


while True:
    client, infosClient = serveur.accept()
    print("Client connecté. Adresse " + infosClient[0])
    morpion.lancerPartie(True, client)
    print("Connexion fermée")
    client.close()

serveur.close()
  

