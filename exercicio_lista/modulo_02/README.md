📊 Análise de Dados de Acesso

Este projeto é um desafio de programação em Python que simula o registro e análise de acessos de usuários.
O programa solicita entradas pelo terminal e armazena os acessos para, ao final, gerar um resumo com estatísticas.

🚀 Funcionalidades

Cadastro de acessos informando:

Nome do usuário

Status do acesso (✅ Sucesso / ❌ Falha)

Duração da sessão (em minutos)

Armazenamento de cada acesso como uma tupla em uma lista.

Registro automático dos usuários que tiveram pelo menos um acesso bem-sucedido (usando set).

Cálculo do tempo total gasto em acessos bem-sucedidos.

Resumo final exibindo:

Todos os registros de acesso

Lista de usuários com sucesso

Tempo total de sessões bem-sucedidas

🖥️ Exemplo de uso
Digite seu nome ou 'parar' para sair: ANA
Selecione o status:
1) Sucesso
2) Falha
Escolha a opção: 1
Digite o tempo de duração (minutos): 15

Digite seu nome ou 'parar' para sair: BOB
Selecione o status:
1) Sucesso
2) Falha
Escolha a opção: 2
Digite o tempo de duração (minutos): 7

Digite seu nome ou 'parar' para sair: PARAR


Saída final:

Registros de acesso:
('ANA', 'Sucesso', 15)
('BOB', 'Falha', 7)

Usuários com pelo menos um sucesso:
{'ANA'}

Tempo total de duração com sucesso: 15 minutos

Programa encerrado...

🛠️ Tecnologias usadas

Python 3.x

Estruturas de dados básicas:

Listas

Tuplas

Conjuntos (set)

Controle de fluxo:

Laços while

Condições if/elif/else

Tratamento de erros com try/except

📚 Aprendizados

Diferença entre lista e conjunto em Python.

Uso de tuplas para armazenar dados relacionados.

Como validar entradas do usuário e evitar erros (ValueError).

Como calcular estatísticas com compreensão de listas e a função sum().