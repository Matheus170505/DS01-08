# Quantidade de entrevistados (Considerando 10 para teste mas possivel alterar para 50)
quantidade = 10 

excelente = 0
ruim = 0

for i in range(quantidade):
    print(f"\nEntrevistado {i+1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite a opção: "))

    # Estrutura de decisão
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
    elif opiniao == 2:
        pass  
    else:
        print("Opção inválida!")

# Resultados finais
print("\nRESULTADO DA PESQUISA")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
