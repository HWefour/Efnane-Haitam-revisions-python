def compterMots(fichier_texte):
    with open(fichier_texte, 'r') as fichier:
        contenu = fichier.read()
        mots = contenu.split()
        nombreMots = len(mots)
    return nombreMots

fichierEntree = 'fichier_texte.txt'

fichierSortie = 'resultat.txt'

nombreMots = compterMots(fichierEntree)

with open(fichierSortie, 'w') as fichier:
    fichier.write(f'Le nombre de mots dans le fichier est : {nombreMots}')

print(f'Le résultat a été écrit dans {fichierSortie}')
