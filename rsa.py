import math
import secrets

# gerar "e" de tal forma que o mdc de "e" e "t" seja igual a 1
def get_e(t, p, q):
    n = max(p, q)
    while True:
        e = secrets.randbelow(t)
        # gcd é o mdc
        if e > n and math.gcd(e, t) == 1:
            return e


# gerar "d" aplicando o módulo inverso em "e" e "t".
def get_d(e, t):
    return pow(e, -1, t)

def rsa(p=3313, q=6121):
    n = p * q

    # Euler Totient
    t = (p - 1) * (q - 1)

    e = get_e(t, p, q)
    d = get_d(e, t)

    return (n,e,),(n,d,),(t,)

# Encriptar mensagem M^e % n
def E(M, e, n):
    return pow(M, e, n)


def encrypt(message: list, public_key):
    for i in range(len(message)):
        message[i] = int(message[i], base=16)
        message[i] = E(message[i], public_key[1], public_key[0])

    return message

def decrypt(cipher: list, private_key):
    for i in range(len(cipher)):
        cipher[i] = D(cipher[i], private_key[1], private_key[0])
        cipher[i] = hex(cipher[i])[2:]

    return cipher


# Decriptar mensagem C^d % n
def D(C, d, n):
    return pow(C, d, n)

# Checar se as chaves públicas e chaves privadas são válidas
# e*d % t = 1, isso significa que "e" e "d" são inversamente multiplicativos
def is_keys_valid(public_key, private_key, totient):
    result = public_key[1]*private_key[1] % totient[0]

    if result == 1:
        return True
    else:
        return False

