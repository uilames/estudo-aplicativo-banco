import requests

# Dados dos usuário 
users = {
    'usuario1': {'senha': 'senha123', 'nome': 'João da Silva', 'saldo': 5000},
    'usuario2': {'senha': 'minhasenha', 'nome': 'Maria Souza', 'saldo': 8000}
}

# Chave da API do ChatGPT 
chatgpt_api_key = ''

def login():
    while True:
        username = input('Digite o nome de usuário: ')
        password = input('Digite a senha: ')

        if username in users and users[username]['senha'] == password:
            return users[username]
        else:
            print('Credenciais inválidas. Tente novamente.\n')

def consultar_saldo(user):
    print(f'Olá, {user["nome"]}!')
    print(f'Seu saldo atual é de R${user["saldo"]:.2f}\n')

def pedir_dica_financeira():
    user_input = input('Digite sua pergunta sobre finanças: ')

    headers = {
        'Authorization': f'Bearer {chatgpt_api_key}'
    }

    data = {
        'messages': [{'role': 'system', 'content': 'Você é um assistente financeiro.'},
                     {'role': 'user', 'content': user_input}]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        chatgpt_response = response_data['choices'][0]['message']['content']
        print(f'Resposta do ChatGPT: {chatgpt_response}\n')
    else:
        print('Desculpe, ocorreu um erro ao se comunicar com o ChatGPT.\n')

def main():
    print('Bem-vindo ao aplicativo de banco simulado!\n')

    user = login()
    consultar_saldo(user)

    while True:
        print('Opções:')
        print('1. Consultar saldo')
        print('2. Pedir dica financeira')
        print('3. Sair')

        escolha = input('Digite o número da opção desejada: ')

        if escolha == '1':
            consultar_saldo(user)
        elif escolha == '2':
            pedir_dica_financeira()
        elif escolha == '3':
            print('Obrigado por usar nosso aplicativo. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.\n')

if __name__ == '__main__':
    main()
