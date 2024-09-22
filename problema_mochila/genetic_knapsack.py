import random


def initialize_population(tamanho_populacao, num_itens):
    return [[random.randint(0, 1) for _ in range(num_itens)] for _ in range(tamanho_populacao)]


def fitness(individuo, pesos_e_valores, peso_maximo):
    peso_total = 0
    valor_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            peso_total += pesos_e_valores[i][0]
            valor_total += pesos_e_valores[i][1]
        if peso_total > peso_maximo:
            return 0 
    return valor_total


def selecao_torneio(populacao, aptidoes, tamanho_torneio=3):
    melhores = random.sample(list(zip(populacao, aptidoes)), tamanho_torneio)
    return max(melhores, key=lambda x: x[1])[0]


def crossover(pai1, pai2):
    ponto_de_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:]
    filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:]
    return filho1, filho2


def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]
    return individuo


def algoritmo_genetico(pesos_e_valores, peso_maximo, num_geracoes, tamanho_populacao, taxa_mutacao):
    populacao = initialize_population(tamanho_populacao, len(pesos_e_valores))
    
    for geracao in range(num_geracoes):
        aptidoes = [fitness(individuo, pesos_e_valores, peso_maximo) for individuo in populacao]
        
        nova_populacao = []
        for _ in range(tamanho_populacao // 2):
            pai1 = selecao_torneio(populacao, aptidoes)
            pai2 = selecao_torneio(populacao, aptidoes)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutacao(filho1, taxa_mutacao))
            nova_populacao.append(mutacao(filho2, taxa_mutacao))
        
        populacao = nova_populacao
    

    aptidoes = [fitness(individuo, pesos_e_valores, peso_maximo) for individuo in populacao]
    melhor_individuo = populacao[aptidoes.index(max(aptidoes))]
    return melhor_individuo, max(aptidoes)
