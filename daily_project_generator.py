import os
import random
import requests
import subprocess
from datetime import datetime

TEMPLATES = {
    'html-css-js': {
        'files': {
            'index.html': '<!DOCTYPE html>\n<html>\n<head>\n  <title>Hello</title>\n</head>\n<body>\n  <h1>Hello World</h1>\n</body>\n</html>',
            'style.css': 'body { font-family: Arial, sans-serif; }',
            'app.js': 'console.log("Hello World");'
        }
    },
    'cpp': {
        'files': {
            'main.cpp': '#include <iostream>\nint main() { std::cout << "Hello World" << std::endl; return 0; }'
        }
    },
    'react': {
        'files': {
            'package.json': '{"name": "hello-react", "version": "1.0.0", "private": true}',
            'App.jsx': 'export default function App() { return <h1>Hello React</h1>; }',
            'index.jsx': 'import React from "react"; import ReactDOM from "react-dom/client"; import App from "./App"; const root = ReactDOM.createRoot(document.getElementById("root")); root.render(<App />);',
            'index.html': '<div id="root"></div>'
        }
    },
    'basic-ml': {
        'files': {
            'train.py': 'from sklearn.datasets import load_iris\nfrom sklearn.tree import DecisionTreeClassifier\nX, y = load_iris(return_X_y=True)\nclf = DecisionTreeClassifier().fit(X, y)\nprint("Model trained")'
        }
    }
}

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME')

if not GITHUB_TOKEN or not GITHUB_USERNAME:
    raise SystemExit('Set GITHUB_TOKEN and GITHUB_USERNAME environment variables.')

selected = random.choice(list(TEMPLATES.keys()))
project_name = f"daily-{selected}-{datetime.now().strftime('%Y%m%d')}"
os.makedirs(project_name, exist_ok=True)

for filename, content in TEMPLATES[selected]['files'].items():
    file_path = os.path.join(project_name, filename)
    with open(file_path, 'w') as f:
        f.write(content)

subprocess.run(['git', 'init'], cwd=project_name, check=True)
subprocess.run(['git', 'add', '.'], cwd=project_name, check=True)
subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=project_name, check=True)

# create repo via GitHub API
repo_data = {'name': project_name, 'auto_init': False, 'private': False}
headers = {'Authorization': f'token {GITHUB_TOKEN}'}
response = requests.post('https://api.github.com/user/repos', json=repo_data, headers=headers)
response.raise_for_status()

repo_url = response.json()['html_url']
origin = response.json()['clone_url']

subprocess.run(['git', 'remote', 'add', 'origin', origin], cwd=project_name, check=True)
subprocess.run(['git', 'branch', '-M', 'main'], cwd=project_name, check=True)
subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=project_name, check=True)

print(f"Created new repo {repo_url}")
