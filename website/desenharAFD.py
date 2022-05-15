from graphviz import Digraph

def desenha_automato(descricao, estados, estadoinicial, estadodeaceitacao, transicoes):
    try:
        estadosdeaceitacao = set(estadodeaceitacao)
        dicionarioTransicao = {}
        for elemento in transicoes.split():
            estadoAtual = elemento[0]
            simbolo = elemento[1]
            estadoSeguinte = elemento[2]
            dicionarioTransicao[(estadoAtual, simbolo)] = estadoSeguinte

        d = Digraph(name=descricao)

        # configurações gerais
        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        d.edge_attr['color'] = 'deeppink'
        d.node_attr['shape'] = 'circle'
        d.node_attr['color'] = 'deeppink'

        # Estado inicial
        d.node('Start', label='', shape='none')

        # Estados de transição
        Transicao = set(estados) - set(estadosdeaceitacao)
        for estado in Transicao:
            d.node(estado)

        # Estado aceitação
        for estado in estadodeaceitacao:
            d.node(estado, shape='doublecircle')

        # Transicoes
        d.edge('Start', estadoinicial)

        for tuplo, estadoSeguinte in dicionarioTransicao.items():
            d.edge(tuplo[0], estadoSeguinte, label=tuplo[1])

        print(d.source)
        d.format = 'svg'
        d.render("website/static/website/images/"+ descricao)

    except IOError:
        print("O ficheiro não existe")
