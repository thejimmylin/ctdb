from invoke import task
from pathlib import Path
import os
import platform
import json


REPO_ROOT = Path(__file__).parent
OS = platform.system().lower()
VENV_DIRNAME = Path('.venv')
PATHONPATHS = {
    'windows': VENV_DIRNAME / 'Scripts' / 'python.exe',
    'linux': VENV_DIRNAME / 'bin' / 'python',
    'darwin': VENV_DIRNAME / 'bin' / 'python',
}
VSCODE_SETTINGS = {
    "python.pythonPath": str(PATHONPATHS[OS]),
    "python.linting.enabled": True,
    "python.linting.pylintEnabled": False,
    "python.linting.flake8Enabled": True,
    "python.linting.flake8Args": ["--max-line-length=160"],
    "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Args": ["--max-line-length=160"]
}
PATHONPATHS_ABS = {
    'windows': REPO_ROOT / VENV_DIRNAME / 'Scripts' / 'python.exe',
    'linux': REPO_ROOT.resolve() / VENV_DIRNAME / 'bin' / 'python',
    'darwin': REPO_ROOT.resolve() / VENV_DIRNAME / 'bin' / 'python',
}
SETCRETS = {
    'DATABASES_MSSQL_PASSWORD': '',
}


# VSCode

@task
def vscode(c):
    s = json.dumps(VSCODE_SETTINGS, indent=4)
    try:
        os.mkdir(REPO_ROOT / '.vscode')
    except FileExistsError:
        pass
    with open(REPO_ROOT / '.vscode' / 'settings.json', 'w', encoding='utf-8') as f:
        f.write(s)
    print('Done!')


@task
def secrets(c):
    s = json.dumps(SETCRETS, indent=4)
    with open(REPO_ROOT / 'secrets.json', 'w', encoding='utf-8') as f:
        f.write(s)
    print('Done!')
