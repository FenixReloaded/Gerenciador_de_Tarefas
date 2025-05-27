import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication
from interface.interface import GerenciadorTarefas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = GerenciadorTarefas()
    janela.show()
    sys.exit(app.exec())
