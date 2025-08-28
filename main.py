def karatsuba(x, y):

    # Se os números forem pequenos (ex: menos de 10 dígitos), 
    # use a multiplicação normal do Python. É mais rápido para números pequenos.
    if len(str(x)) < 10 or len(str(y)) < 10:
        return x * y

    # 2. Calcular o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    # 3. Dividir os números em duas metades (a, b, c, d)
    a = x // (10**n2)
    b = x % (10**n2)
    c = y // (10**n2)
    d = y % (10**n2)

    # 4. Fazer as três chamadas recursivas 
    z2 = karatsuba(a, c)  # ac
    z0 = karatsuba(b, d)  # bd
    z1 = karatsuba(a + b, c + d) # (a+b)(c+d)

    # 5. Calcular o termo do meio: (ad + bc) = z1 - z2 - z0
    meio = z1 - z2 - z0

    # 6. Combinar os resultados para obter o produto final
    resultado = (z2 * (10**(2 * n2))) + (meio * (10**n2)) + z0
    
    return resultado

def main():
    while True:
        try:
            s1 = input("Digite o primeiro inteiro (ou 'sair' para encerrar): ").strip()
            if s1.lower() in ("sair", "exit", "q"):
                print("Encerrando.")
                return
            s2 = input("Digite o segundo inteiro (ou 'sair' para encerrar): ").strip()
            if s2.lower() in ("sair", "exit", "q"):
                print("Encerrando.")
                return
            x = int(s1)
            y = int(s2)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros válidos.")

    print(f"Produto Karatsuba: {karatsuba(x, y)}")
    print(f"Produto Python:    {x * y}")


if __name__ == "__main__":
    main()