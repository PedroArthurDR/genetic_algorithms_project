from genetic_minimization import algoritmo_genetico

geracoes = 100
tamanho_populacao = 10
taxa_mutacao = 0.01

melhor_x, melhor_valor = algoritmo_genetico(geracoes, tamanho_populacao, taxa_mutacao)
print(f"Melhor x: {melhor_x}, valor mínimo de f(x): {melhor_valor}")
