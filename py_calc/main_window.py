import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__ (self, parent: QWidget | None = None, *args, **Kwargs) -> None:
        super().__init__(parent, *args, **Kwargs)

        # Config da janela
        self.central_widget = QWidget() # type: ignore
        self.vertical_layout = QVBoxLayout() # type: ignore
        self.central_widget.setLayout (self.vertical_layout) # type: ignore
        self.setCentralWidget(self.central_widget) # type: ignore
        
        # Título da janela da aplicação
        self.setWindowTitle('Power Calc PY')
      

        # Última configuração a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
