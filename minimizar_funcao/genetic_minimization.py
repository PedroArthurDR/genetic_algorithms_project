import random
import math

def initialize_population(tamanho_populacao):
    return [random.uniform(-10, 10) for _ in range(tamanho_populacao)]

def fitness(x):
    return x**3 - 6*x + 14

def selecao(populacao, fitnesses):
    return random.choices(populacao, weights=[1/f for f in fitnesses], k=2)

def crossover(pai1, pai2):
    ponto_de_corte = random.uniform(0, 1)
    filho1 = ponto_de_corte * pai1 + (1 - ponto_de_corte) * pai2
    filho2 = ponto_de_corte * pai2 + (1 - ponto_de_corte) * pai1
    return filho1, filho2

def mutacao(individuo, taxa_mutacao):
    if random.random() < taxa_mutacao:
        return individuo + random.uniform(-0.1, 0.1)
    return individuo

def algoritmo_genetico(geracoes, tamanho_populacao, taxa_mutacao):
    populacao = initialize_population(tamanho_populacao)
    
    for geracao in range(geracoes):
        fitnesses = [fitness(x) for x in populacao]
        
        nova_populacao = []
        while len(nova_populacao) < tamanho_populacao:
            pai1, pai2 = selecao(populacao, fitnesses)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutacao(filho1, taxa_mutacao))
            nova_populacao.append(mutacao(filho2, taxa_mutacao))
        
        populacao = nova_populacao[:tamanho_populacao]
    
    melhor_x = min(populacao, key=fitness)
    return melhor_x, fitness(melhor_x)
