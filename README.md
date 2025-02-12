# Comparador de Saídas para o Verde - PUC Minas (Verde Diff)

Este é um script em Python que compara as saídas esperadas com as saídas do usuário no sistema de atividades Verde da PUC Minas. Ele facilita a identificação de inconsistências, auxiliando na depuração e correção dos códigos enviados.

## 🚀 Funcionalidades
- Compara a saída gerada pelo código do usuário com a saída esperada.
- Destaca diferenças entre as saídas para facilitar a análise.

## 🛠️ Como Usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/renancmd/verde-diff.git
   cd verde-diff
2. **Execute o script**:
    ```bash
    python3 main.py pub.out arquivo_usuario.txt
Onde:

- `pub.out` contém a saída esperada.

- `arquivo_usuario.txt` contém a saída gerada pelo código do usuário.

3. **Exemplos de saída do script**
    ```nginx
    Linha 3: Esperado: "Hello, world!" | Obtido: "hello, world!"
    Linha 5: Esperado: "42" | Obtido: " 42"

## 📋 Requisitos
    - Python 3.x instalado
    - Nenhuma dependência externa

## 📜 Licença
[MIT](https://choosealicense.com/licenses/mit/)
