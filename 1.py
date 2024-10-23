#grupo: Pamella, Neon e Matheus Felipe


class Animal:
    def __init__(self, nome, idade, especie):
        self._nome = nome
        self._idade = idade
        self._especie = especie
        self._daycare = False 

    def calcular_preco_servico(self):
        pass

class Cachorro(Animal):
    def calcular_preco_servico(self):
        return 50

class Gato(Animal):
    def calcular_preco_servico(self):
        return 40

class Passaro(Animal):
    def calcular_preco_servico(self):
        return 30

def menu():
    animais = []
    while True: 
        print("\nMenu:")
        print("1. Cadastrar animal")
        print("2. Consultar animal")
        print("3. Calcular preço de serviço")
        print("4. Serviço extra")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tipo_animal = input("Tipo de animal (cachorro/gato/passaro): ").strip().lower()
            nome = input("Nome do animal: ")
            idade = input("Idade do animal: ")

            if tipo_animal == 'cachorro':
                animal = Cachorro(nome, idade, tipo_animal)
            elif tipo_animal == 'gato':
                animal = Gato(nome, idade, tipo_animal)
            elif tipo_animal == 'passaro':
                animal = Passaro(nome, idade, tipo_animal)
            else:
                print("Animal inválido.")
                continue
            
            animais.append(animal)
            print("Animal cadastrado com sucesso!")

        elif opcao == '2':
            if not animais:
                print("Nenhum animal cadastrado.")
                continue
            else:
                for i in range(len(animais)):
                    animal = animais[i]
                    daycare_status = "ativado" if animal._daycare_ativado else "não ativado"
                    print(f"{i + 1}. {animal._nome}, Idade: {animal._idade}, Espécie: {animal._especie}, Daycare: {daycare_status}")
       
        elif opcao == '3':
            if not animais:
                print("Nenhum animal cadastrado.")
                continue
            nome_animal = input("Digite o nome do animal para calcular o preço do serviço: ").strip()
            animal_encontrado = next((animal for animal in animais if animal._nome.lower() == nome_animal.lower()), None)
            
            if animal_encontrado:
                preco = animal_encontrado.calcular_preco_servico()
                print(f"O preço do serviço para '{animal_encontrado._nome}' é R${preco:.2f}")
            else:
                print("Animal não encontrado.")

        elif opcao == '4':
            nome_animal = input("Digite o nome do animal para ativar o serviço de daycare: ").strip()
            animal_encontrado = next((animal for animal in animais if animal._nome.lower() == nome_animal.lower()), None)
            
            if animal_encontrado:
                extra = input("Deseja ativar o serviço de daycare? (sim/não): ").strip().lower()
                if extra == 'sim':
                    animal_encontrado._daycare_ativado = True
                    print("Serviço de daycare ativado para o seu pet!")
                elif extra == 'não':
                    print("Serviço de daycare não ativado.")
                else:
                    print("Opção inválida. Por favor, responda com 'sim' ou 'não'.")
            else:
                print("Animal não encontrado.")

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
