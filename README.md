# Uber

# Para iniciar máquina virtual
python -m venv .env
cd .\.env\Scripts\
.\activate

cd ../..
pip install -r requirements.txt

# Para atualizar os requerimentos de bibliotecas
pip freeze > requirements.txt