import webbrowser
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

# De HTML code die we eerder hebben gemaakt
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>App Portaal - Python Server</title>
    <style>
        body { margin: 0; background: #121212; color: white; font-family: sans-serif; 
               display: flex; justify-content: center; align-items: center; height: 100vh; }
        .box { text-align: center; border: 2px solid #007bff; padding: 40px; border-radius: 20px; }
        .btn { background: #007bff; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>App3882744 is nu actief</h2>
        <p>De Python server draait op de achtergrond.</p>
        <br><br>
        <a href="https://www.appcreator24.com/app3882744" class="btn">OPEN APP IN BROWSER</a>
    </div>
</body>
</html>
"""

# Maak een tijdelijk bestand aan
with open("temp_app.html", "w") as f:
    f.write(html_content)

def start_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server gestart op http://localhost:8000")
    print("Sluit dit venster niet zolang je de app gebruikt.")
    
    # Open automatisch je browser
    webbrowser.open("http://localhost:8000/temp_app.html")
    
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()



