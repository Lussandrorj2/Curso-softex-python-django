# 📘 Programa de Notas Escolares com Loop While

Este programa em **Python** calcula a média de notas de um ou mais alunos, validando entradas e exibindo um boletim final. Ele utiliza um **loop `while`** para permitir a inserção de múltiplos alunos até que o usuário decida encerrar.

---

## 🚀 Funcionalidades

- Solicita o **nome** e a **matrícula** do aluno.  
- Permite inserir **várias notas** para cada aluno, terminando com `-1`.  
- **Validação de dados**:
  - Aceita apenas números entre **0 e 10**.  
  - Exibe mensagens de erro caso seja digitado um valor inválido.  
- Calcula a **média final do aluno**.  
- Exibe mensagens personalizadas de acordo com o desempenho:  
  - `>= 9.0` → Excelente! Aprovado com louvor.  
  - `7.0 - 8.9` → Parabéns! Aprovado.  
  - `5.0 - 6.9` → Em recuperação.  
  - `< 5.0` → Reprovado.  
- Pergunta se deseja cadastrar outro aluno:
  - Digitar `S` → cadastrar novo aluno  
  - Qualquer outra tecla → encerra o programa  
- Mantém a janela aberta até que o usuário pressione **ENTER** no final.

---

## 📌 Exemplo de Uso

```text
>>>> Programa de notas escolares com Loop While <<<<

Digite o nome do aluno: João
Digite a matrícula do aluno: 12345
Insira a nota (ou -1 para encerrar o cadastro deste aluno): 9
Insira a nota (ou -1 para encerrar o cadastro deste aluno): 7.5
Insira a nota (ou -1 para encerrar o cadastro deste aluno): -1

==== Boletim Escolar ====
Aluno: João
Matrícula: 12345
Notas: [9.0, 7.5]
Média: 8.25
Parabéns! Você está aprovado João!

Deseja cadastrar outro aluno? (S/N): n
Encerrando o programa...
Pressione ENTER para sair do programa...


## 📂 Estrutura do Código

Entrada de dados: nome, matrícula e notas.

Loop While: para inserir múltiplas notas.

Validações: garante que apenas valores corretos sejam aceitos.

Cálculo da média: soma das notas dividido pela quantidade.

Exibição dos resultados: notas inseridas, média e mensagem final.

## 🛠️ Tecnologias Utilizadas

Python 3

## 📅 Data de criação

21/08/2023 - Autor Lussandro A Farias.
