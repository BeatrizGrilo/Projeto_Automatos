from .models import MaquinaTuring

def validar_TM(sequencia, turing_id):

    V = MaquinaTuring.objects.get(id=turing_id)
    estadoInicial = V.estadoinicial
    dic = {}
    estadosDeAceitacao = V.estadodeaceitacao

    for i in V.transicoes.split():
        primeiro = i[0]
        simbolo = i[1]
        segundo = i[2]
        simbolo2 = i[3]
        move = i[4]
        dic[(primeiro, simbolo)] = segundo, simbolo2, move

    lista = ["Δ"] * 21
    lista[10:0] = sequencia
    indice = 0

    for elemento in lista:
        if elemento == 'Δ':
            indice = indice + 1
        else:
            break

    EstadoAtual = estadoInicial
    try:
        while EstadoAtual != estadosDeAceitacao:
            numero = lista[indice]
            GuardaValor = EstadoAtual
            EstadoAtual = dic[EstadoAtual, lista[indice]][0]
            lista[indice] = dic[GuardaValor, lista[indice]][1]
            if dic[GuardaValor, numero][2] == "R":
                indice = indice + 1
            if dic[GuardaValor, numero][2] == "L":
                indice = indice - 1

        if EstadoAtual == estadosDeAceitacao:
            return ("Sequência aceite")
    except:
        return ("Sequencia não aceite")
