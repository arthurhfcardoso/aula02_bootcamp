import sys


def ex01():
    # Soma dois numeros inteiros inseridos pelo usuario.
    tentativas = 0

    while tentativas < 3:
        try:
            Numero1 = int(input("Digite o primeiro numero inteiro: "))
            Numero2 = int(input("Digite o segundo numero inteiro: "))
            print("A soma dos numeros e", Numero1 + Numero2)
            break  # sai quando deu certo            
        except ValueError:
            print("Erro: Por favor, insira apenas numeros inteiros.")
            tentativas += 1
    else:
        print("Numero maximo de tentativas atingido.")

def ex02():
    # Recebe um numero e calcula o resto da divisao desse numero por 5.
    numero = int(input("Digite um numero inteiro: "))
    resto = numero % 5
    print("O resto da divisao de", numero, "por 5 e", resto)


def ex03():
    # Multiplica dois numeros fornecidos pelo usuario e mostra o resultado.
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = numero1 * numero2
    print("O resultado da multiplicacao e", f"{resultado:.2f}")


def ex04():
    # Pede dois numeros inteiros e imprime a divisao inteira do primeiro pelo segundo.
    pass


def ex05():
    # Calcula o quadrado de um numero fornecido pelo usuario.
    pass


def ex06():
    # Recebe dois numeros flutuantes e realiza a adicao.
    pass


def ex07():
    # Calcula a media de dois numeros flutuantes fornecidos pelo usuario.
    pass


def ex08():
    # Calcula a potencia de um numero (base e expoente fornecidos pelo usuario).
    pass


def ex09():
    # Converte a temperatura de Celsius para Fahrenheit.
    pass


def ex10():
    # Calcula a area de um circulo, recebendo o raio como entrada.
    pass


def ex11():
    # Recebe uma string e a converte para maiusculas.
    pass


def ex12():
    # Recebe o nome completo do usuario e imprime tudo em minusculas.
    pass


def ex13():
    # Recebe uma frase e imprime sem espacos no inicio e no fim.
    pass


def ex14():
    # Recebe uma data "dd/mm/aaaa" e imprime dia, mes e ano separadamente.
    pass


def ex15():
    # Concatena duas strings fornecidas pelo usuario.
    pass


def ex16():
    # Avalia duas expressoes booleanas e retorna o resultado do AND.
    pass


def ex17():
    # Recebe dois valores booleanos e retorna o resultado do OR.
    pass


def ex18():
    # Recebe um valor booleano e inverte esse valor.
    pass


def ex19():
    # Compara se dois numeros fornecidos pelo usuario sao iguais.
    pass


def ex20():
    # Verifica se dois numeros fornecidos pelo usuario sao diferentes.
    pass


def ex21():
    # Conversor de temperatura.
    pass


def ex22():
    # Verificador de palindromo.
    pass


def ex23():
    # Calculadora simples.
    pass


def ex24():
    # Classificador de numeros.
    pass


def ex25():
    # Conversao de tipo com validacao.
    pass


EXERCICIOS = {
    "ex01": ex01,
    "ex02": ex02,
    "ex03": ex03,
    "ex04": ex04,
    "ex05": ex05,
    "ex06": ex06,
    "ex07": ex07,
    "ex08": ex08,
    "ex09": ex09,
    "ex10": ex10,
    "ex11": ex11,
    "ex12": ex12,
    "ex13": ex13,
    "ex14": ex14,
    "ex15": ex15,
    "ex16": ex16,
    "ex17": ex17,
    "ex18": ex18,
    "ex19": ex19,
    "ex20": ex20,
    "ex21": ex21,
    "ex22": ex22,
    "ex23": ex23,
    "ex24": ex24,
    "ex25": ex25,
}


def main():
    if len(sys.argv) < 2:
        print("Uso: python exercicios.py ex01")
        print("Opcoes:", ", ".join(EXERCICIOS.keys()))
        return

    nome = sys.argv[1]
    func = EXERCICIOS.get(nome)
    if func is None:
        print(f"Exercicio invalido: {nome}")
        print("Opcoes:", ", ".join(EXERCICIOS.keys()))
        return

    func()


if __name__ == "__main__":
    main()
