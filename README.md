# Hotbar Randomizer

Hotbar Randomizer is a Python application built with PyQt6 that simplifies the process of placing random block patterns in Minecraft. By automating hotbar selection, this tool is perfect for users looking to create diverse designs without the hassle of manual selection.

## Features

- **Hotbar Checkbox Grid**: A 3x3 grid representing Minecraft hotbar slots, allowing users to toggle which slots are active.
- **Toggle All Button**: Quickly select or deselect all hotbar slots.
- **Random Slot Selection**: When enabled, the program randomly selects a checked slot and simulates typing the corresponding hotbar number.
- **Start/Stop Listening**: A toggle button to enable or disable the randomization process, ensuring full control over the automation.
- **Minecraft Integration**: Designed specifically for automating block pattern placement in Minecraft using the hotbar.
- **Background Operation**: Listens for `Shift + Right-Click` even when the program window is unfocused, enabling seamless interaction with Minecraft.

## How It Works

1. Launch the program to display the 3x3 grid of checkboxes.
2. Toggle the checkboxes to match the hotbar slots you want to include in the randomization.
3. Use the "Toggle All" button for quick selection or deselection.
4. Click "Start Listening" to enable the randomizer.
5. In Minecraft, hold `Shift` and right-click to randomly select one of the active hotbar slots. The program will simulate typing the corresponding number, allowing you to place blocks from the selected slot.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TromboneJake/HotbarRandomizer.git
   cd HotbarRandomizer
   ```
2. Install the required dependencies:
   ```bash
   pip install pyqt6 keyboard pynput
   ```
3. Run the program:
   ```bash
   python HotbarRandomizerQt.py
   ```

## Requirements

- Python 3.7+
- PyQt6 (`pip install pyqt6`)
- keyboard (`pip install keyboard`)
- pynput (`pip install pynput`)

## Usage Tips

- Ensure Minecraft is the active window when using the randomizer for seamless block placement.
- Adjust your Minecraft hotbar to match the slots you've toggled in the program for accurate randomization.
- Use the "Start Listening" button only when you're ready to automate.

## Troubleshooting

- **Keypress Issues**: If the program types shifted characters (e.g., `@` instead of `2`), ensure your keyboard language settings are correct.
- **Background Listening**: The program may not work as expected if it lacks permission to simulate keypresses in your operating system.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Inspired by the need for efficient random block placement in Minecraft.
- Built with PyQt6 for a clean and responsive user interface.

