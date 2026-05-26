from faker import Faker
import sys


def gerar_perfis(n=15, locale='pt_BR'):
    faker = Faker(locale)
    perfis = []
    for _ in range(n):
        nome = faker.name()
        endereco = faker.address().replace('\n', ', ')
        email = faker.email()
        perfis.append({'nome': nome, 'endereco': endereco, 'email': email})
    return perfis


def imprimir_perfis(perfis):
    print(f"Gerando {len(perfis)} perfis de usuários com dados falsos:\n")
    for idx, p in enumerate(perfis, 1):
        print(f"--- Perfil {idx} ---")
        print(f"Nome: {p['nome']}")
        print(f"Endereço: {p['endereco']}")
        print(f"Email: {p['email']}")
        print("-" * 20)


if __name__ == '__main__':
    try:
        perfis = gerar_perfis(15)
        imprimir_perfis(perfis)
    except ModuleNotFoundError:
        print("Biblioteca 'Faker' não encontrada. Instale com: pip install Faker")
        sys.exit(1)