from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Passo 2: Treinamento do Chatbot
chatbot = ChatBot('Assistente de Estudos')

# Treinamento do Chatbot com dados sobre Matemática
mat_training = [
    "Qual é a fórmula para calcular a área de um círculo?",
    "A fórmula para calcular a área de um círculo é π * raio².",
    "Qual é a fórmula para calcular o volume de uma esfera?",
    "A fórmula para calcular o volume de uma esfera é 4/3 * π * raio³.",
    "O que é um número primo?",
    "Um número primo é um número natural maior que 1 que possui apenas dois divisores: 1 e ele mesmo."
]

# Treinamento do Chatbot com dados sobre Ciências
cie_training = [
    "Qual é a lei da gravidade?",
    "A lei da gravidade foi formulada por Isaac Newton e descreve a atração entre corpos massivos.",
    "Qual é a teoria da evolução?",
    "A teoria da evolução é uma explicação científica para a origem das espécies, proposta por Charles Darwin.",
    "O que é um átomo?",
    "Um átomo é a menor unidade de um elemento químico que mantém as propriedades desse elemento."
]

# Treinamento do Chatbot com dados sobre História
his_training = [
    "Quem foi o primeiro presidente dos Estados Unidos?",
    "O primeiro presidente dos Estados Unidos foi George Washington.",
    "O que foi a Revolução Industrial?",
    "A Revolução Industrial foi um período de grande transformação econômica, social e tecnológica que começou na Inglaterra no século XVIII.",
    "Quem foi Cleópatra?",
    "Cleópatra foi a última rainha do Egito da dinastia Ptolemaica, conhecida por sua inteligência e beleza."
]

# Treinamento do Chatbot com os dados de todas as disciplinas
trainer = ListTrainer(chatbot)
trainer.train(mat_training)
trainer.train(cie_training)
trainer.train(his_training)

# Função para permitir que o usuário escolha a disciplina
def escolher_disciplina():
    print("Olá! Em qual disciplina você precisa de ajuda?")
    print("1 - Matemática")
    print("2 - Ciências")
    print("3 - História")
    opcao = input("Informe a disciplina com o respectivo número.")
    if opcao == '1':
        return 'Matemática'
    elif opcao == '2':
        return 'Ciências'
    elif opcao == '3':
        return 'História'
    else:
        print("Opção inválida. Por favor, escolha um número da disciplina informada acima.")
        return escolher_disciplina()

total_perguntas = 0
respostas_corretas = 0

while True:
    disciplina = escolher_disciplina()
    if disciplina.lower() == 'sair':
        print("Obrigado por usar o Assistente de Estudos.")
        if total_perguntas == 0:
            print("Nenhuma pergunta foi feita.")
        else:
            precisao = (respostas_corretas / total_perguntas) * 100
            print(f"A precisão de resposta do Assistente de Estudos foi de {precisao:.2f}%.")
        break
    elif disciplina.lower() in ['matemática', 'ciências', 'história']:
        pergunta = input(f"Qual é a sua pergunta sobre {disciplina.capitalize()}? (Digite 'sair' para encerrar): ")
        if pergunta.lower() == 'sair':
            print("Obrigado por usar o Assistente de Estudos.")
            if total_perguntas == 0:
                print("Nenhuma pergunta foi feita.")
            else:
                precisao = (respostas_corretas / total_perguntas) * 100
                print(f"A precisão de resposta do Assistente de Estudos foi de {precisao:.2f}%.")
            break
        else:
            total_perguntas += 1
            resposta = chatbot.get_response(pergunta)
            print("Assistente de Estudos:", resposta)
            resposta_correta = input("A resposta foi útil? (sim/não): ")
            if resposta_correta.lower() == 'sim':
                respostas_corretas += 1
    else:
        print("Por favor, escolha uma disciplina válida (Matemática, Ciências ou História).")
