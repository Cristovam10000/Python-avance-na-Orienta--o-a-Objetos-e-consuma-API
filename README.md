# Python: Orientação a Objetos e Consumo de API

Projeto didático desenvolvido para praticar **POO (Programação Orientada a Objetos, paradigma que organiza o programa em objetos que combinam dados e comportamentos)** com Python.

Na etapa atual, o repositório modela restaurantes, avaliações e itens de cardápio, além de conter exercícios complementares sobre veículos e bancos. Apesar de “consumo de API” fazer parte do nome do repositório, ainda não há uma integração com **API (Application Programming Interface, interface que permite a comunicação estruturada entre sistemas)** implementada no código versionado.

## Objetivos de aprendizagem

- criar classes e objetos;
- aplicar herança entre classes;
- definir classes e métodos abstratos;
- utilizar polimorfismo em regras de desconto;
- organizar responsabilidades em módulos;
- trabalhar com listas de objetos e composição, relação em que um objeto contém outros objetos;
- praticar encapsulamento, organização do acesso ao estado interno, por convenção com atributos iniciados por `_`.

## Funcionalidades atuais

### Restaurante e avaliações

A classe `Restaurante` permite:

- cadastrar instâncias em uma lista compartilhada de restaurantes;
- alternar o estado entre ativo e inativo;
- receber avaliações com notas de 1 a 5;
- calcular a média das avaliações;
- adicionar itens válidos ao cardápio;
- exibir os itens cadastrados.

### Cardápio e descontos

`ItemCardapio` é uma **classe abstrata (classe que define uma base comum e um contrato para as subclasses)**. Toda classe concreta de item precisa implementar o método `aplicar_desconto()`.

| Tipo de item | Informação específica | Desconto atual | Exemplo usado em `app.py` |
| --- | --- | ---: | ---: |
| `bebida` | tamanho | 5% | R$ 5,00 → R$ 4,75 |
| `Prato` | descrição | 8% | R$ 25,00 → R$ 23,00 |
| `Sobremesa` | descrição, tipo e tamanho | 10% | R$ 10,00 → R$ 9,00 |

Cada objeto aplica sua própria regra por **polimorfismo (capacidade de objetos de tipos diferentes responderem à mesma operação com comportamentos específicos)**.

As responsabilidades estão separadas da seguinte forma:

1. o próprio item calcula e altera seu preço em `aplicar_desconto()`;
2. `Restaurante.adicionar_no_cardapio()` verifica se o objeto é um `ItemCardapio` e guarda a mesma referência na lista;
3. `Restaurante.exibir_cardapio` percorre a lista e apresenta os dados já armazenados.

### Exercícios complementares

O diretório `modelos/Pratica/` contém exemplos adicionais:

- `veiculo`, classe abstrata especializada por `carro` e `moto`;
- `Banco`, classe base especializada por `Agencia`.

O fluxo de veículos é demonstrado em `app.py`. As classes de banco existem como exercício independente e ainda não são chamadas pelo programa principal.

## Estrutura do projeto

```text
.
├── app.py
├── modelos/
│   ├── avaliacao.py
│   ├── restaurante.py
│   ├── cardapio/
│   │   ├── item_cardapio.py
│   │   ├── bebida.py
│   │   ├── prato.py
│   │   └── sobremesa.py
│   └── Pratica/
│       ├── Veiculo.py
│       └── banco.py
└── README.md
```

| Arquivo ou diretório | Responsabilidade |
| --- | --- |
| [`app.py`](app.py) | cria os objetos de exemplo e inicia a demonstração no terminal |
| [`modelos/restaurante.py`](modelos/restaurante.py) | gerencia estado, avaliações e cardápio do restaurante |
| [`modelos/avaliacao.py`](modelos/avaliacao.py) | representa o cliente e a nota de uma avaliação |
| [`modelos/cardapio/`](modelos/cardapio/) | concentra a abstração e os tipos concretos de item |
| [`modelos/Pratica/`](modelos/Pratica/) | reúne exercícios independentes de herança e abstração |

## Pré-requisitos

- Python 3.12 ou superior;
- Git, somente para clonar o repositório;
- nenhuma biblioteca externa.

O código atual usa uma forma de `f-string` — texto formatado que incorpora valores de expressões Python — aceita a partir do Python 3.12. A execução desta revisão foi verificada com Python 3.14.3.

## Como executar

Clone o projeto e entre no diretório:

```bash
git clone https://github.com/Cristovam10000/Python-avance-na-Orienta--o-a-Objetos-e-consuma-API.git
cd Python-avance-na-Orienta--o-a-Objetos-e-consuma-API
```

A criação de um **ambiente virtual (diretório isolado que mantém o interpretador e as dependências do projeto separados do restante do sistema)** é opcional, pois ainda não existem dependências externas.

No Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python app.py
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python app.py
```

Se não quiser criar um ambiente virtual, execute diretamente `python app.py` no Windows ou `python3 app.py` no Linux e macOS.

## Fluxo demonstrado por `app.py`

1. cria uma sobremesa, uma bebida e um prato;
2. aplica a regra de desconto de cada tipo;
3. cria o restaurante `Praça`;
4. adiciona os três objetos ao cardápio;
5. cria um carro e uma moto;
6. liga os dois veículos;
7. exibe o cardápio e o estado dos veículos no terminal.

Saída esperada, de forma resumida:

```text
Cardapio do restaurante Praça:

1. Nome:Coca-Cola | Preço: R$4.75 | Tamanho: grande
2. Nome:Lasanha | Preço: R$23.00 | Descrição: Lasanha de carne com molho branco e queijo gratinado
3. Nome:Pudim | Preço: R$9.00 | Descrição: Pudim de leite condensado | Tipo: Doce | Tamanho: Médio
Marca: Honda, Modelo: Civic, Ligado: True, Portas: 4
Marca: Yamaha, Modelo: MT-07, Ligado: True, Tipo: Esportiva
```

## Validação

Nesta revisão, o fluxo correspondente ao seguinte **smoke test (execução curta que verifica se o fluxo principal inicia e termina sem erro)** foi executado diretamente com o interpretador Python 3.14.3 disponível no ambiente:

```powershell
python app.py
```

O programa terminou com código de saída `0` e exibiu os três itens com os descontos esperados, além dos dois veículos ligados. Também foram aprovadas oito verificações pontuais sobre descontos, média de avaliações, filtro do cardápio e estado dos veículos.

Ainda não existe uma suíte de testes automatizados versionada no repositório; portanto, essa validação oferece evidência sobre o fluxo demonstrativo e as regras verificadas, mas não cobre todos os métodos e casos de erro.

## Limitações conhecidas

- o consumo de API ainda não foi implementado;
- os dados de demonstração estão definidos diretamente em `app.py`;
- chamadas repetidas de `aplicar_desconto()` acumulam novos descontos sobre o preço já alterado;
- entradas inválidas em alguns métodos são ignoradas sem mensagem de erro;
- não há testes automatizados, **type hints (anotações que documentam os tipos esperados por parâmetros, variáveis e retornos)** ou gerenciamento de dependências;
- alguns nomes de classes ainda não seguem a convenção PascalCase, em que cada palavra começa com letra maiúscula, recomendada pela **PEP 8 (Python Enhancement Proposal 8, guia de estilo do código Python)**;
- o repositório ainda não possui um arquivo de licença.

## Próximos passos sugeridos

- adicionar testes unitários com `pytest`, framework que organiza e executa testes em Python;
- incluir type hints e validação explícita das entradas;
- padronizar os nomes das classes segundo a PEP 8;
- separar os exemplos de cardápio e veículos em pontos de entrada próprios;
- evoluir a exibição dos itens para um comportamento polimórfico;
- implementar e documentar a etapa de consumo de API.