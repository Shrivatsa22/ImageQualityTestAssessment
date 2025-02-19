from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Cropping Parameters")
        self.setGeometry(200, 200, 400, 300)

        self.layout = QVBoxLayout()

        # Input fields for cropping parameters
        self.x_label = QLabel("X Coordinate:", self)
        self.x_input = QLineEdit(self)

        self.y_label = QLabel("Y Coordinate:", self)
        self.y_input = QLineEdit(self)

        self.width_label = QLabel("Width:", self)
        self.width_input = QLineEdit(self)

        self.height_label = QLabel("Height:", self)
        self.height_input = QLineEdit(self)

        # OK and Cancel buttons
        self.button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.reject)

        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel_button)

        # Adding widgets to the layout
        self.layout.addWidget(self.x_label)
        self.layout.addWidget(self.x_input)
        self.layout.addWidget(self.y_label)
        self.layout.addWidget(self.y_input)
        self.layout.addWidget(self.width_label)
        self.layout.addWidget(self.width_input)
        self.layout.addWidget(self.height_label)
        self.layout.addWidget(self.height_input)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

    def get_parameters(self):
        try:
            x = int(self.x_input.text())
            y = int(self.y_input.text())
            width = int(self.width_input.text())
            height = int(self.height_input.text())
            return x, y, width, height
        except ValueError:
            return None

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    form = MyForm()
    if form.exec_() == QDialog.Accepted:
        params = form.get_parameters()
        if params:
            print(f"Parameters: {params}")
        else:
            print("Invalid input!")
    sys.exit(app.exec_())
