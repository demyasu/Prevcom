import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'copa2026'))

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prevcom_app.app import app as prevcom_app
from copa2026.app import app as copa_app

copa_app.config['APPLICATION_ROOT'] = '/'
prevcom_app.config['APPLICATION_ROOT'] = '/prevcom'

application = DispatcherMiddleware(copa_app, {
    '/prevcom': prevcom_app,
})

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 5001, application, use_debugger=True, use_reloader=True)
