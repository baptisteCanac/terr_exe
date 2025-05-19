import subprocess
import sys
import os

def run():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # dossier racine du projet
    app_dir = os.path.join(base_dir, "app")
    venv_dir = os.path.join(app_dir, "env")
    requirements_path = os.path.join(base_dir, "requirements.txt")

    # Créer l'environnement virtuel et installer les dépendances en une seule étape
    if not os.path.exists(venv_dir):
        print("Création de l'environnement virtuel...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

    # Installer les dépendances si nécessaire
    pip_path = os.path.join(venv_dir, "Scripts", "pip.exe")
    if not is_requirements_installed(pip_path, requirements_path):
        print("Installation des dépendances...")
        subprocess.check_call([pip_path, "install", "-r", requirements_path])
    else:
        print("Les dépendances sont déjà installées.")

    # Lancer main.py dans l'environnement virtuel
    python_path = os.path.join(venv_dir, "Scripts", "python.exe")
    main_py = os.path.join(app_dir, "main.py")
    print("Lancement de main.py...")
    subprocess.check_call([python_path, main_py])

def is_requirements_installed(pip_path, requirements_path):
    """Vérifie si les dépendances de requirements.txt sont installées."""
    installed_packages = subprocess.check_output([pip_path, "freeze"]).decode().splitlines()
    
    # Lire requirements.txt et comparer avec les packages installés
    with open(requirements_path) as f:
        required_packages = f.read().splitlines()

    # Si tous les packages requis sont installés, retourner True
    return all(pkg in installed_packages for pkg in required_packages)

if __name__ == "__main__":
    run()
