#!/bin/bash
# Executar no Bash do PythonAnywhere

USERNAME="demyasu"
REPO_URL="https://github.com/demyasu/Prevcom.git"
PROJECT_DIR="/home/$USERNAME/Prevcom"

echo "=== 1. Clonando/atualizando o repositório ==="
cd /home/$USERNAME
rm -rf Prevcom.old 2>/dev/null
if [ -d "$PROJECT_DIR" ]; then
    mv Prevcom Prevcom.old
fi
git clone "$REPO_URL" Prevcom
cd Prevcom

echo ""
echo "=== 2. Criando virtualenv =="
rmvirtualenv combined 2>/dev/null
mkvirtualenv combined --python=python3.10
pip install -r requirements.txt

echo ""
echo "=== 3. Criando arquivo .env ==="
cat > prevcom_app/.env << 'ENVEOF'
SECRET_KEY=prevcom-app-secret-pythonanywhere-2026
FLASK_ENV=production
ENVEOF

echo ""
echo "=== 4. Configurando WSGI do PythonAnywhere ==="
WSGI_FILE="/var/www/${USERNAME}_pythonanywhere_com_wsgi.py"
cat > "$WSGI_FILE" << WSEOF
import sys
sys.path.insert(0, '$PROJECT_DIR')
sys.path.insert(0, '$PROJECT_DIR/copa2026')
from wsgi import application
WSEOF

echo ""
echo "=== 5. Forçando reload do web app ==="
touch /var/www/${USERNAME}_pythonanywhere_com_wsgi.py

echo ""
echo "=== Pronto! ==="
echo "Acesse: https://${USERNAME}.pythonanywhere.com/"
echo "Prevcom: https://${USERNAME}.pythonanywhere.com/prevcom/"
