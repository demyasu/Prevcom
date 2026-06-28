import webbrowser
import threading
import time

def abrir_browser():
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=abrir_browser, daemon=True).start()
    from app import app
    app.run(host="127.0.0.1", port=5000, debug=False)
