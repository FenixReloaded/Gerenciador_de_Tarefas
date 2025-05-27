# Gerenciador de Tarefas

Este é um aplicativo de Gerenciador de Tarefas desenvolvido com **Python** e **PyQt6**, que permite adicionar, atualizar, completar e excluir tarefas com persistência de dados em um arquivo JSON.

---

## Funcionalidades

- Adicionar nova tarefa
- Atualizar o nome de uma tarefa existente
- Marcar uma tarefa como completada
- Deletar todas as tarefas completadas
- Interface gráfica simples e funcional com PyQt6

---

## Estrutura do Projeto

###### Resumido:

projeto/

├── interface/

│   └── interface.py

├── tarefas/

│   ├──  **init** .py

│   ├── logica.py

│   └── persistencia.py

├── Task.ico

├── main.py

├── requirements.txt

└── readme.md

###### Completo:

├── main.py

├── main.spec

├── readme.md

├── requeriments.txt

├── Task.ico

├── __init__.py
│
├── build

│   └── main

│       ├── Analysis-00.toc

│       ├── base_library.zip

│       ├── EXE-00.toc

│       ├── main.pkg

│       ├── PKG-00.toc

│       ├── PYZ-00.pyz

│       ├── PYZ-00.toc

│       ├── warn-main.txt

│       ├── xref-main.html

│       │
│       └── localpycs

│           ├── pyimod01_archive.pyc

│           ├── pyimod02_importers.pyc

│           ├── pyimod03_ctypes.pyc

│           ├── pyimod04_pywin32.pyc

│           └── struct.pyc
│
├── dist

│   └── main.exe
│
├── interface

│   ├── interface.py

│   ├── __init__.py
│   │
│   └── __pycache__

│       ├── interface.cpython-311.pyc

│       └── __init__.cpython-311.pyc
│
├── persistencia_de_dados

│   └── tarefas.json
│
├── tarefas

│   ├── logica.py

│   ├── persistencia.py

│   ├── __init__.py
│   │
│   └── __pycache__

│       ├── logica.cpython-311.pyc

│       ├── persistencia.cpython-311.pyc

│       └── __init__.cpython-311.pyc
│
└── tarefas_persistencia
    └── tarefas.json

---

## Como Executar

1. Clone o reposítorio ou baixe o código.
2. Instale as dependências:

   pip install -r requirements.txt
   
4. Execute o programa:
   Através do botão de rodar em uma IDE ou através de um comando no terminal, para isso vá até a pasta raiz onde está localizado o programa e rode o seguinte código:

   python main.py

## Detalhes Técnicos

* **Persistência:**

  Os dados das tarefas são armazenados em um arquivo `tarefas.json` dentro da pasta `tarefas_persistencia`.
* **Interface:**

  Desenvolvida com  **PyQt6** , possui botões para todas as operações e confirmações com  **QMessageBox** .
* **Ícone:**

  O ícone da aplicação está localizado na raiz do projeto com o nome `Task.ico`.

  Caso queira trocar, basta substituir o arquivo.

## Como Gerar Executável (.exe)

* Se quiser transformar este programa em um executável para Windows, utilize o  **PyInstaller** :

  pip install pyinstaller
* E depois dentro da pasta raiz do projeto use esse comando:

  python -m PyInstaller --noconfirm --onefile --windowed main.py
* Assim o executável estará dentro da pasta "dist" que estará na raiz do diretório.

## Requisitos

* Python 3.11.5+
* PyQt6

---

## Autor

* Desenvolvido por: Caio Pereira Guimarães
* Email para contato: cpg.contato.networking@gmail.com

---

## Licença

Este projeto é livre para uso e modificação.
