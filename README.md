# controller Interactive Fiction
 
# Interactive Fiction Controller Interface

## Description

This project provides a Python-based interface for controlling interactive fiction games using a game controller. It leverages the `pygame` library to handle joystick input and the `pyautogui` library to simulate keyboard inputs, allowing players to interact with text-based games seamlessly.

## Features

- **Controller Support**: Connects to various game controllers and maps buttons to common interactive fiction commands.
- **Customizable Controls**: Supports D-Pad navigation, button mappings for actions like LOOK, WAIT, HELP, and more.
- **Touchpad Integration**: Maps the touchpad click to the spacebar for quick interactions.
- **Real-time Input Handling**: Processes joystick inputs in real-time, allowing for smooth gameplay.

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

3. Connect your game controller and run the script:
   ```bash
   python controllerIF.py
   ```

## Usage

Once the script is running, you can use your game controller to navigate and interact with your interactive fiction game. The mappings are designed to provide a natural and intuitive experience for players.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.