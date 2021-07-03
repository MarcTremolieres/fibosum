import sys

def fibosum_calcule(N, M):
    a = 0
    b = 1
    modulo = 1000000007
    if N < 2:
        if M < 2:
            return M - N + 1
        somme = 1
        for _ in range(2, M + 1):
            a, b = b, a
            b += a
            if b >= modulo: b = b % modulo
            somme += b
            if somme >= modulo: somme = somme % modulo
        return somme
    somme = 0
    for _ in range(2, N):
        a, b = b, a
        b += a

        if b >= modulo: b = b % modulo
    for _ in range(N, M + 1):
        a, b = b, a
        b += a
        if b >= modulo: b = b % modulo
        somme += b
        if somme >= modulo: somme = somme % modulo
    return somme

lignes = sys.stdin.readlines()
nombre = int(lignes[0])
sortie = ""
for index in range(1,nombre + 1):
    ligne = lignes[index]
    valeurs = ligne.split(" ")
    N = int(valeurs[0])
    M = int(valeurs[1])
    sortie += str(fibosum_calcule(N, M))
    sortie += "\n"
print(sortie)




