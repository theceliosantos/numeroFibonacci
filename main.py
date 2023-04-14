num = int(input("Digite um número inteiro: "))
fibonacci = [0, 1]

while fibonacci[-1] <= num:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)


if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci!")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")