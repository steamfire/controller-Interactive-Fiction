# Interactive Fiction/Text Adventure Game Controller


This project simulates typing commands when pressing buttons on your game controller, for navigating Interactive Fiction games. It is configured to enter the most common Infocom game commands.  It uses Python 3, the `pygame` library to read controller input and the `pyautogui` library to simulate keyboard inputs.

## Features

- **Controller Support**: Only tested with SONY DUALSENSE controller on macOS 14. Should work with others, but will probably require remap in code.
- **Customizable Controls**: Supports D-Pad navigation, button mappings for actions like LOOK, WAIT, HELP, and more.  (customizable in code)

## Controls Mapping

- **D-Pad**:
  - ↑ (Up)    -> north/n
  - ↓ (Down)  -> south/s
  - ← (Left)  -> west/w
  - → (Right) -> east/e
- **Buttons**:
  - X (×)     -> examine/x
  - O (○)     -> inventory/i
  - □ (Square) -> open
  - △ (Triangle) -> close
- **Triggers & Bumpers**:
  - L1        -> help
  - L2        -> look
  - R1        -> wait
  - R2        -> get all
- **Other**:
  - Touchpad  -> space

## Requirements

- Python 3.x
- `pygame` library
- `pyautogui` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/interactive-fiction-controller.git
   cd interactive-fiction-controller
   ```

2. Install the required libraries:
   ```bash
   pip install pygame pyautogui
   ```

3. Connect your game controller to your computer and run the script:
   ```bash
   python controllerIF.py
   ```

## Usage
First run, on macOS - a dialog box will appear that asks for system permissions for Accessibility for Terminal.  This has to be granted to use the controller as text command input.  Not sure what happens for other OSes.

Once the script is running in terminal, the terminal window will display button mapping.  Change apps to your interactive fiction window.  Tapping controller buttons will type the IF commands + return IN ALL APPS as if it were a keyboard. 


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
