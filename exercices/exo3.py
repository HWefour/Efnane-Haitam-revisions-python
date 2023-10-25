print("saisissez votre calcul")
calcul = input()
operation = calcul.split()
if len(operation) != 3:
    print("Entrée invalide. Format attendu : nombre1 opérateur nombre2")
else:
    nombre1 = int(operation[0])
    operateur = operation[1]
    nombre2 = int(operation[2])
if operateur == "+":
    resultat = nombre1 + nombre2
elif operateur == "-":
    resultat = nombre1 - nombre2
elif operateur == "*":
    resultat = nombre1 * nombre2
elif operateur == "/":
    resultat = nombre1 / nombre2

print(resultat)