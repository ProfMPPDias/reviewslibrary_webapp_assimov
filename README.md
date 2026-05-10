# Books Metrics & Reviews Dashboard 📚

Um painel interativo de dados desenvolvido com Python e Streamlit, projetado para visualizar e analisar os 100 livros mais populares e suas respectivas avaliações de clientes.

## 📸 Screenshots do Projeto

![Página Inicial](screenshots/Books_review_1.png)
![Página de Reviews](screenshots/Books_review_2.png)


## 👨‍💻 Desenvolvedor e Créditos
- **Desenvolvido por:** Marcos Dias
- **Projeto baseado no curso da:** ASIMOV Academy

## 🚀 Como Instalar e Rodar o Projeto

Este projeto acompanha um instalador automático para Windows. Para rodar a aplicação em seu computador, siga os passos abaixo:

1. **Faça o download ou clone o repositório** para uma pasta no seu computador.
2. Dê um clique duplo no arquivo **`install_and_run.bat`**.
3. O script irá automaticamente:
   - Criar um ambiente virtual isolado (`venv`).
   - Instalar todas as dependências necessárias listadas no `requirements.txt`.
   - Iniciar o aplicativo no seu navegador padrão.

*(Nota: Certifique-se de que o Python esteja instalado e adicionado ao PATH do Windows).*

### Instalação Manual (Mac/Linux/Windows)
Caso prefira configurar manualmente, abra o terminal na pasta do projeto e execute:
```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Mac/Linux:
# source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python runner.py
```

## 🛠️ Como Atualizar o Código no GitHub (Guia do Git)

Para manter o seu código salvo em um repositório remoto (como o GitHub), utilize a sequência de comandos abaixo no terminal da sua pasta:

```bash
# 1. Inicia o repositório (apenas na primeira vez)
git init

# 2. Adiciona todos os arquivos modificados para o "palco" (staging)
git add .

# 3. Cria um pacote (commit) com uma mensagem descritiva
git commit -m "Finalização do App de Avaliação de Livros"

# 4. Conecta com o seu GitHub (apenas na primeira vez - troque pela sua URL)
# git remote add origin https://github.com/SEU_USUARIO/NOME_DO_PROJETO.git

# 5. Envia as modificações para a nuvem
git branch -M main
git push -u origin main
```
