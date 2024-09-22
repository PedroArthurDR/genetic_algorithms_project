from genetic_knapsack import algoritmo_genetico

pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
num_cromossomos = 150
geracoes = 50
taxa_mutacao = 0.01

melhor_individuo, melhor_valor = algoritmo_genetico(pesos_e_valores, peso_maximo, geracoes, num_cromossomos, taxa_mutacao)
print(f"Melhor solução: {melhor_individuo}, com valor total: {melhor_valor}")
