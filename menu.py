import string
import random
import time
import rsa
import message


def randomgenerator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def gerar_inspetor(public_key):
    inspetor = [public_key, randomgenerator()]
    return inspetor


def gerar_texto_inspetor(
    inspetor_A, inspetor_B, inspetor_C,
        inspetor_revogado_A, inspetor_revogado_B):

    print("Inspetores autorizados: ")
    print("1 -", inspetor_A[1])
    print("2 -", inspetor_B[1])
    print("3 -", inspetor_C[1])
    print()

    print("Inspetores com acesso revogado: ")
    print("4 -", inspetor_revogado_A[1])
    print("5 -", inspetor_revogado_B[1])
    print()

def menu(inspetores, inspetores_revogados, governo):
    print("""
Um navio foi apreendido pelo governo brasileiro
contendo lixo tóxico danoso ao meio ambiente.

Somente inspetores qualificados com autorização
podem adentrar o navio.

Cada inspetor autorizado possui a chave publica do
governo e os revogados qualquer outra chave.

As chaves de cada inspetor sao testadas com a chave
privada do governo, e, entram somente aqueles que
possuem a chave correspondente.

A chave é testada de forma automatica sem a intervenção
do usuario utilizando a tecnica de criptografia RSA.

    """)

    gerar_texto_inspetor(inspetores[0], inspetores[1],
                         inspetores[2], inspetores_revogados[0],
                         inspetores_revogados[1])

    print("Qual inspetor vai acessar o navio?")
    inspetor = input(">>> ")

    # Inspetores com acesso valido
    if inspetor == '1':
        print(f"\nInspetor {inspetores[0][1]} enviando mensagem a central...")
        m = validate_access(inspetores[0][1], inspetores[0][0], governo)
        print('Mensagem recebida!')

    elif inspetor == '2':
        print(f"\nInspetor {inspetores[1][1]} enviando mensagem a central...")
        time.sleep(1)
        m = validate_access(inspetores[1][1], inspetores[1][0], governo)
        time.sleep(2)
        print('Mensagem recebida!')

    elif inspetor == '3':
        print(f"\nInspetor {inspetores[2][1]} enviando mensagem a central...")
        time.sleep(1)
        m = validate_access(inspetores[2][1], inspetores[2][0], governo)
        time.sleep(2)
        print('Mensagem recebida!')

    # Inspetores com acesso revogado
    elif inspetor == '4':
        time.sleep(1)

    elif inspetor == '5':
        time.sleep(1)

    if rsa.is_keys_valid(inspetores_revogados[0][0], governo["private_key"], governo["totient"]):
        print("Acesso Concedido!")
    else:
        print("\nAcesso revogado!")
        print("Motivo: a chave de acesso foi renovada.\nPor favor, solicite outra.")

    if rsa.is_keys_valid(inspetores_revogados[1][0], governo["private_key"], governo["totient"]):
        print("Acesso Concedido!")
    else:
        print("Acesso revogado!")
        print("Motivo: a chave de acesso foi renovada.\nPor favor, solicite outra.")


def validate_access(id, public_key, governo):

    if rsa.is_keys_valid(public_key, governo["private_key"], governo["totient"]):
        m = message.blocks(f"Inspetor {id} requerendo acesso à área restrita.")

    c = rsa.encrypt(m, public_key)
    m = rsa.decrypt(c, governo["private_key"])
    m = message.revert_blocks(m)

    print(f'\nMensagem:\n{"".join(m)}\n')
    time.sleep(1)
    print('Acesso Concedido!\n')
    return m

