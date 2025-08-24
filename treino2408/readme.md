# 📘 Programa de Notas Escolares com Loop While  

Este programa em **Python** foi desenvolvido para calcular a média de notas de um aluno, validando entradas, evitando erros e exibindo uma mensagem final de desempenho. Ele utiliza um **loop `while`** para permitir a inserção de várias notas até que o usuário decida encerrar.  

---

## 🚀 Funcionalidades  
- Solicita o **nome** e a **matrícula** do aluno.  
- Permite inserir **várias notas** até que o usuário digite `-1` para sair.  
- **Validação de dados**:
  - Aceita apenas números entre **0 e 10**.  
  - Exibe mensagens de erro caso seja digitado um valor inválido.  
- Calcula a **média final do aluno**.  
- Exibe mensagens personalizadas de acordo com o desempenho:  
  - `>= 9.0` → Excelente! Aprovado com louvor.  
  - `7.0 - 8.9` → Parabéns! Aprovado.  
  - `5.0 - 6.9` → Em recuperação.  
  - `< 5.0` → Reprovado.  

---

## 📌 Exemplo de Uso  

```bash
>>>> Programa de notas escolares com Loop While <<<<
Digite o nome do aluno: João
Digite a matrícula do aluno: 12345
Insira a nota (ou -1 para sair): 9
Insira a nota (ou -1 para sair): 7.5
Insira a nota (ou -1 para sair): -1

A média das notas é: 8.25
As notas inseridas foram: [9.0, 7.5]
Parabéns! Você está aprovado João!

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