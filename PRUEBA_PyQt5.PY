from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

def on_button_click():
    label.setText("¡Hola, " + line_edit.text() + "!")

# Crear una aplicación y una ventana principal
app = QApplication([])
window = QWidget()

# Crear y configurar widgets
label = QLabel("Ingresa tu nombre:")
line_edit = QLineEdit()
button = QPushButton("Saludar")
button.clicked.connect(on_button_click)

# Configurar el diseño
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(button)

# Aplicar el diseño a la ventana
window.setLayout(layout)

# Mostrar la ventana
window.show()

# Iniciar la aplicación
app.exec_()
