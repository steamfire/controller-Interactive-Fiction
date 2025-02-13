import pygame
import time
import pyautogui  # Import pyautogui for keyboard simulation

def init_controller():
    pygame.init()
    pygame.joystick.init()
    
    # Check if any controller is connected
    if pygame.joystick.get_count() == 0:
        print("No controller found!")
        return None
    
    # Initialize the first controller
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print(f"Connected to: {controller.get_name()}")
    return controller

def main():
    controller = init_controller()
    if not controller:
        return

    try:
        while True:
            pygame.event.pump()  # Process events to get fresh values
            
            # Get D-pad values as buttons
            dpad_up = controller.get_button(11)
            dpad_down = controller.get_button(12)
            dpad_left = controller.get_button(13)
            dpad_right = controller.get_button(14)
            
            # Check D-pad inputs and send corresponding key presses
            if dpad_up:
                pyautogui.typewrite('n\n')  # Send 'n' followed by Enter
                time.sleep(0.5)  # Prevent multiple rapid inputs
            elif dpad_down:
                pyautogui.typewrite('s\n')  # Send 's' followed by Enter
                time.sleep(0.5)
            elif dpad_left:
                pyautogui.typewrite('w\n')  # Send 'w' followed by Enter
                time.sleep(0.5)
            elif dpad_right:
                pyautogui.typewrite('e\n')  # Send 'e' followed by Enter
                time.sleep(0.5)

            time.sleep(0.1)  # Small delay to make output readable
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
