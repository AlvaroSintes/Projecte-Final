import subprocess

def pex6():
    try:
        subprocess.run(["python3", "Servidor/Server Django/mysite/manage.py", "runserver", "8082"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al iniciar el servidor Django:", e)

