# FPAA01 - Algoritmo de Karatsuba

## Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Fundamentos
de Projeto e Análise de Algoritmos**. O objetivo é implementar o algoritmo de Karatsuba em Python para a multiplicação eficiente de números inteiros grandes,
aplicando uma abordagem de "dividir para conquistar".

O repositório contém o código-fonte da implementação e um relatório
técnico detalhado sobre as complexidades do algoritmo.

## O Algoritmo de Karatsuba

O algoritmo de Karatsuba é um método de multiplicação rápida descoberto
por Anatolii Karatsuba em 1960. Ele reduz significativamente o número de
operações necessárias para multiplicar dois números grandes em
comparação com o método tradicional.

A ideia principal é transformar uma multiplicação de dois números de n
dígitos, que normalmente exigiria 4 multiplicações de números com n/2
dígitos, em um problema que necessita de apenas 3 multiplicações de n/2
dígitos, ao custo de algumas adições e subtrações adicionais.

Essa otimização altera a complexidade de tempo de O(n²) (método
clássico) para aproximadamente O(n\^1.585), tornando-o muito mais rápido
para números com muitos dígitos.

## Ambiente virtual

### Passo 1: Criar e ativar o ambiente virtual

É recomendável usar um ambiente virtual para gerenciar suas dependências. Siga os passos abaixo para configurar um ambiente virtual:

1. Crie um ambiente virtual usando o seguinte comando:
    ```bash
    python3 -m venv .venv
    ```

2. Ative o ambiente virtual:
    - No macOS e Linux:
        ```bash
        source .venv/bin/activate
        ```
    - No Windows:
        ```bash
        .venv\Scripts\activate
        ```

### Passo 2: Executar o script

Após ativar o ambiente virtual, execute o script principal:
```bash
python main.py
```

## Versão do Python

Este projeto foi desenvolvido na versão **3.13.0** do Python e **não exige a instalação de nenhuma dependência adicional**.

## Explicação do Código (main.py)

O arquivo `main.py` contém a implementação da função principal do
algoritmo.

### Função `karatsuba(x, y)`

Esta função implementa a lógica recursiva do algoritmo. A seguir, uma
explicação detalhada da sua estrutura:

-   **Caso Base:** A recursão para quando os números de entrada (x e y)
    são pequenos (ex: menos de 10 dígitos). Nesse ponto, a multiplicação
    padrão do Python (`*`) é mais eficiente que a sobrecarga da
    recursão.
-   **Preparação:** O tamanho `n` é definido como o máximo de dígitos
    entre x e y. O ponto de divisão, `n2`, é calculado como `n/2`.
-   **Divisão dos Números:** Os números x e y são divididos em duas
    metades (a, b, c, d) com base no ponto de divisão `n2`.

( x = a `\cdot 10`{=tex}\^{n2} + b \\ y = c `\cdot 10`{=tex}\^{n2} + d )

-   **Chamadas Recursivas:** Três produtos são calculados
    recursivamente:

( z2 = karatsuba(a, c) \\ z0 = karatsuba(b, d) \\ z1 = karatsuba(a + b,
c + d) )

-   **Combinação dos Resultados:**

( resultado = (z2 `\cdot 10`{=tex}\^{2n2}) + ((z1 - z2 - z0)
`\cdot 10`{=tex}\^{n2}) + z0 )

## Relatório Técnico

### Análise da Complexidade Assintótica

-   **Complexidade de Tempo:**\
    A relação de recorrência para o algoritmo é:\
    ( T(n) = 3T(n/2) + O(n) )\
    Pelo Teorema Mestre, essa recorrência resolve para O(n\^log₂3) ≈
    O(n\^1.585).

-   **Melhor, Pior e Médio Caso:**\
    Os três casos são idênticos, dependendo apenas do número de dígitos.

-   **Complexidade de Espaço:**\
    A profundidade da recursão é O(log n).

### Análise da Complexidade Ciclomática

A análise ciclomática foi focada na função `karatsuba(x, y)`, que contém
a lógica central do algoritmo.

#### Grafo de Fluxo de Controle (Nós e Arestas)

O fluxo de controle da função pode ser representado pelo seguinte grafo:

**Nós (N):** - Nó 1 (Início): Ponto de entrada da função.\
- Nó 2 (Decisão): Condição `if len(str(x)) < 10 or len(str(y)) < 10:`.\
- Nó 3 (Caso Base): Bloco `return x * y`.\
- Nó 4 (Caso Recursivo): Bloco de cálculos, chamadas recursivas e
combinação dos resultados.\
- Nó 5 (Fim): Ponto de saída da função.

**Arestas (E):** - E1: Nó 1 → Nó 2\
- E2: Nó 2 → Nó 3 (se verdadeiro)\
- E3: Nó 2 → Nó 4 (se falso)\
- E4: Nó 3 → Nó 5\
- E5: Nó 4 → Nó 5

#### Cálculo da Complexidade Ciclomática

Utilizando a fórmula:\
( M = E - N + 2P )

-   E (Arestas) = 5\
-   N (Nós) = 5\
-   P (Componentes) = 1

( M = 5 - 5 + 2 `\cdot 1`{=tex} = 2 )

A complexidade ciclomática da função `karatsuba` é **2**. Isso indica
que existem dois caminhos independentes no código: um para o caso base e
outro para o passo recursivo.

## Exemplo de Saída da Execução

Ao executar `python main.py`, a saída demonstrará:

    Multiplicando 12345678901234567890 por 98765432109876543210...
    Resultado Karatsuba: 1219326311370217952237463801111263526900
    Resultado Python:    1219326311370217952237463801111263526900

Os resultados são idênticos!
