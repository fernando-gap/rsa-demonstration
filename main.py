from rsa import rsa
from rsa import is_keys_valid
import menu

public_key, private_key, totient = rsa()
revoked_public_key = rsa(p=7, q=5)[0]

governo = {
    "private_key": private_key,
    "public_key": public_key,
    "totient": totient,
    "revoked_public_key": revoked_public_key,
}

governo["inspetores_autorizados"] = [
    menu.gerar_inspetor(governo["public_key"]),
    menu.gerar_inspetor(governo["public_key"]),
    menu.gerar_inspetor(governo["public_key"])
]

governo["inspetores_revogados"] = [
    menu.gerar_inspetor(governo["revoked_public_key"]),
    menu.gerar_inspetor(governo["revoked_public_key"]),
]

print(governo)
# # Terminal nao fechar
while True:
    menu.menu(governo["inspetores_autorizados"], governo["inspetores_revogados"], governo)

    print("\n\nContinuar? (sim/nao)")
    m = input(">>> ")
    if m.lower() == "sim":
        continue
    else:
        break
