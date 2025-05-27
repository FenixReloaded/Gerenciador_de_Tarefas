from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QInputDialog, QMessageBox
import os

from PyQt6.QtGui import QIcon
from tarefas.persistencia import carregar_tarefas
from tarefas.logica import adicionar_tarefa, atualizar_tarefa, completar_tarefa, deletar_completadas

class GerenciadorTarefas(QWidget):
    def __init__(self):
        super().__init__()

        caminho_icone = os.path.join(os.path.dirname(__file__), '..', 'Task.ico')
        self.setWindowIcon(QIcon(caminho_icone))

        self.setWindowTitle("Gerenciador de Tarefas")
        self.setMinimumSize(400, 400)

        self.tarefas = carregar_tarefas()

        self.layout = QVBoxLayout()
        self.lista = QListWidget()
        self.layout.addWidget(self.lista)

        botoes = [
            ("Adicionar Tarefa", self.on_adicionar),
            ("Atualizar Nome da Tarefa", self.on_atualizar),
            ("Completar Tarefa", self.on_completar),
            ("Deletar Tarefas Completadas", self.on_deletar),
        ]

        for texto, func in botoes:
            btn = QPushButton(texto)
            btn.clicked.connect(func)
            self.layout.addWidget(btn)

        btn_sair = QPushButton("Sair do Programa")
        btn_sair.clicked.connect(self.confirmar_saida)
        self.layout.addWidget(btn_sair)

        self.setLayout(self.layout)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.clear()
        for t in self.tarefas:
            status = "✓" if t["completada"] else " "
            self.lista.addItem(f"[{status}] {t['tarefa']}")

    def mostrar_mensagem(self, texto):
        QMessageBox.information(self, "Informação", texto)

    def on_adicionar(self):
        nome, ok = QInputDialog.getText(self, "Adicionar Tarefa", "Nome da Tarefa:")
        if ok and nome:
            adicionar_tarefa(self.tarefas, nome)
            self.atualizar_lista()
            self.mostrar_mensagem("Tarefa adicionada com sucesso!")

    def on_atualizar(self):
        idx = self.lista.currentRow()
        if idx >= 0:
            novo_nome, ok = QInputDialog.getText(self, "Atualizar Tarefa", "Novo nome:")
            if ok and novo_nome:
                atualizar_tarefa(self.tarefas, idx, novo_nome)
                self.atualizar_lista()
                self.mostrar_mensagem("Tarefa atualizada com sucesso!")
        else:
            self.mostrar_mensagem("Por favor, selecione uma tarefa para atualizar.")

    def on_completar(self):
        idx = self.lista.currentRow()
        if idx >= 0:
            completar_tarefa(self.tarefas, idx)
            self.atualizar_lista()
            self.mostrar_mensagem("Tarefa marcada como completada!")
        else:
            self.mostrar_mensagem("Por favor, selecione uma tarefa para completar.")

    def on_deletar(self):
        deletar_completadas(self.tarefas)
        self.atualizar_lista()
        self.mostrar_mensagem("Tarefas completadas foram deletadas.")

    def confirmar_saida(self):
        resposta = QMessageBox.question(
            self,
            "Confirmar saída",
            "Tem certeza que deseja sair?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if resposta == QMessageBox.StandardButton.Yes:
            self.close()
