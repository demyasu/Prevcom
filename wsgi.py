import sys
import os
import importlib.util

# ============================================================
# 1. ATIVAR O VIRTUALENV (MODO COMPATÍVEL COM PYTHONANYWHERE)
# ============================================================

# Caminho para o site-packages do seu venv
venv_site_packages = '/home/pcyasuic/Prevcom/venv/lib/python3.11/site-packages'

# Adiciona o site-packages do venv ao sys.path
if venv_site_packages not in sys.path:
    sys.path.insert(0, venv_site_packages)

# ============================================================
# 2. FUNÇÃO PARA CARREGAR APLICATIVOS FLASK
# ============================================================

def load_app(app_path, project_dir, name):
    if project_dir not in sys.path:
        sys.path.insert(0, project_dir)

    old_cwd = os.getcwd()
    os.chdir(project_dir)

    spec = importlib.util.spec_from_file_location(name, app_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    os.chdir(old_cwd)

    return module.app

# ============================================================
# 3. CAMINHOS DAS SUAS APLICAÇÕES
# ============================================================

copa_dir = '/home/pcyasuic/Copa2026'
prevcom_dir = '/home/pcyasuic/Prevcom/prevcom_app'

# ============================================================
# 4. CARREGAR AS APLICAÇÕES
# ============================================================

copa_app = load_app(copa_dir + '/app.py', copa_dir, 'copa')
prevcom_app = load_app(prevcom_dir + '/app.py', prevcom_dir, 'prevcom')

# ============================================================
# 5. DISPATCHER
# ============================================================

def application(environ, start_response):
    path = environ.get('PATH_INFO', '')

    if path.startswith('/prevcom'):
        environ['SCRIPT_NAME'] = '/prevcom'
        environ['PATH_INFO'] = path[len('/prevcom'):]
        return prevcom_app(environ, start_response)
    else:
        return copa_app(environ, start_response)
