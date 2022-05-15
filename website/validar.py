from .models import Automato

def validar_sequencia(sequencia, automato_id):
    V = Automato.objects.get(id=automato_id)
    estadoInicial = V.estadoinicial
    dic = {}
    estadosDeAceitacao = set(V.estadodeaceitacao)

    for i in V.transicoes.split():
        primeiro = i[0]
        simbolo = i[1]
        segundo = i[2]
        dic[(primeiro, simbolo)] = segundo

    estadoAtual = estadoInicial

    for i in sequencia:
        for j in dic.keys():
             if str(estadoAtual) == str(j[0]) and str(i) == str(j[1]):
                estadoAtual = dic.get(j)
                break

    for z in list(estadosDeAceitacao):
        if estadoAtual == str(z):
            return ("Sequência aceite")

    if estadoAtual != str(z):
        return ("Sequência não aceite")