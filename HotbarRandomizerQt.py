from PyQt6.QtCore import QSize, Qt, QEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QLabel, QWidget, QSpacerItem
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Controller, Key
import random
import keyboard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotbar Randomizer")
        self.setFixedSize(400, 500)

        # Initialize listener and controller
        self.mouse_listener = MouseListener(on_click=self.on_mouse_click)
        self.keyboard_controller = Controller()

        # List to store checkbox references
        self.checkboxes = []

        # Main Layout
        main_layout = QVBoxLayout()

        # Instruction label
        instructions_label = QLabel("HOW TO USE:\n"
            "Select numbers using the checkboxes below.\n"
            "Click 'Start Listening' to activate. Choose 'Stop Listening' to deactivate.\n"
            "Hold Shift and right-click to randomly select a number.\n"
            "The selected number will be typed as if pressed on the keyboard.")


        spacer = QSpacerItem(20, 40)

        # Toggle all button
        toggle_button_layout = QHBoxLayout()
        self.toggle_all_button = QPushButton("Select All")
        self.toggle_all_button.setFixedSize(100, 30)
        toggle_button_layout.addWidget(self.toggle_all_button)
        self.toggle_all_button.clicked.connect(self.toggle_button_clicked)


        # Checkbox Grid Layout
        checkbox_grid_layout = QGridLayout() # 3x3 Checkbox Grid
        self.checkbox_data =[]
        # Create 3x3 checkbox grid
        for row in range(3):
            for col in range(3):
                # Calc label num
                label_number = row * 3 + col + 1
                # Create vertical layout for each grid cell
                cell_layout = QVBoxLayout()
                # Create label and checkbox
                label = QLabel(str(label_number))
                checkbox = QCheckBox()
                # Center label and checkbox in cell
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
                cell_layout.addWidget(checkbox, alignment=Qt.AlignmentFlag.AlignCenter)
                # Store checkbox references
                self.checkboxes.append(checkbox)
                self.checkbox_data.append((label.text(), checkbox))
                # Add to grid
                checkbox_grid_layout.addLayout(cell_layout, row, col)
                checkbox_grid_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        

        # Current number label
        self.current_number_label = QLabel("Not Listening")
        self.current_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)
        
        # On Off button
        listening_button_layout = QHBoxLayout()
        self.listening_button = QPushButton("Start Listening")
        self.listening_button.setCheckable(True)
        self.listening_button.setFixedSize(150, 50)
        listening_button_layout.addWidget(self.listening_button)
        self.listening_button.toggled.connect(self.update_listening_text)
        
        
        # Footer label
        footer_label = QLabel("Hotbar Randomizer                Version: 2.0\n"
                              "Jacob Karpovich                     12/10/2024")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)


        # Assemble main layout
        main_layout.addWidget(instructions_label)
        main_layout.addItem(spacer)
        main_layout.addLayout(toggle_button_layout)
        main_layout.addLayout(checkbox_grid_layout)
        main_layout.addWidget(self.current_number_label)
        main_layout.addLayout(listening_button_layout)
        main_layout.addWidget(footer_label)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.installEventFilter(self)

    # Toggle all checkboxes
    def toggle_button_clicked(self):
        print("Toggled all!")

        # Check if all checkboxes are checked
        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes)

        # Toggle checkboxes: uncheck if all are checked, otherwise check all
        for checkbox in self.checkboxes:
            checkbox.setChecked(not all_checked)

        if all_checked:
            self.toggle_all_button.setText("Select All")
        else:
            self.toggle_all_button.setText("Deselect All")


    def update_listening_text(self, checked):
        if checked:
            self.listening_button.setText("Stop Listening")
            self.current_number_label.setText("Right-click while holding Shift")
        else:
            self.listening_button.setText("Start Listening")
            self.current_number_label.setText("Not Listening")

    def on_mouse_click(self, x, y, button, pressed):
        if not self.listening_button.isChecked():
            return
        if pressed and button.name == "right" and keyboard.is_pressed('shift'):
            self.type_random_checked_number()

    # Type random checked number
    def eventFilter(self, source, event):
        # Check if the start listening button is checked
        if self.listening_button.isChecked():
            # Detect mouse press events
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.RightButton:
                    modifiers = QApplication.keyboardModifiers()
                    if modifiers == Qt.KeyboardModifier.ShiftModifier:
                        self.type_random_checked_number()
                        return True # Event handled

        return super().eventFilter(source, event)


    def type_random_checked_number(self):
        checked_numbers = [
            label_text for label_text, checkbox in self.checkbox_data if checkbox.isChecked()
        ]
        if checked_numbers:
            selected_number = random.choice(checked_numbers)

            self.keyboard_controller.release(Key.shift)
            self.keyboard_controller.type(str(selected_number))
            self.keyboard_controller.press(Key.shift)

            print(selected_number)
            self.current_number_label.setText(selected_number)
        else:
            self.current_number_label.setText("No numbers selected")


    def start_listening(self):
        self.mouse_listener.start()

app = QApplication([])

window = MainWindow()
window.show()

window.start_listening()

app.exec()