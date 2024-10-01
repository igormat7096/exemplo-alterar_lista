#criar uma lista de nomes de carro 
carros = ["Fusca", "Civic", "Corolla", "Gol", "Onix", "Focus", "Celta", "Honda HR-V", "Toyota Hilux", "Chevrolet Tracker"]

#exebir a lista original para o usuário
for i in range(len(carros)):
    print(f"Indice {i}: {carros[i]}")

#informe o índice que deseja alterar 
try:
    indice = int(input("Informe o índice que deseja alterar: "))
    confirmacao = input(f"Deseja alterar o o carro {carros[indice]}? Digite 'SIM' para confirmar. ")
    
    if confirmacao == "sim":
        novo_carro = input("Informe o novo carro: ")
        carros[indice] = novo_carro
    else:
        ...

except Exception as e: 
    print(f"Não foi possível alterar o carro. {e}.")
finally:
    #nova lista 
    for i in range(len(carros)):
        print(f"índice {i}: {carros[i]}.")


