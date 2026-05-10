@echo off
echo ==========================================
echo Instalador e Inicializador do Projeto
echo ==========================================

:: Verifica se a pasta venv existe
if not exist venv\Scripts\activate.bat (
    echo [INFO] Criando o ambiente virtual...
    python -m venv venv
)

:: Ativa o ambiente virtual
echo [INFO] Ativando o ambiente virtual...
call venv\Scripts\activate.bat

:: Instala as dependencias
echo [INFO] Instalando as dependencias...
pip install -r requirements.txt

:: Executa a aplicacao
echo [INFO] Iniciando a aplicacao Streamlit...
python runner.py

pause
