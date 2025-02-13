import pygame
import time
import pyautogui  # Import pyautogui for keyboard simulation

def print_controls_reference():
    """Display a reference guide for the controls"""
    print("\n=== Interactive Fiction Controller Reference ===")
    print("D-Pad:")
    print("  ↑ (Up)    -> north/n")
    print("  ↓ (Down)  -> south/s")
    print("  ← (Left)  -> west/w")
    print("  → (Right) -> east/e")
    print("\nButtons:")
    print("  X (×)     -> examine/x")
    print("  O (○)     -> inventory/i")
    print("  □ (Square)-> open")
    print("  △ (Triangle) -> close")
    print("\nTriggers & Bumpers:")
    print("  L1        -> help")
    print("  L2        -> look")
    print("  R1        -> wait")
    print("  R2        -> get all")
    print("\nOther:")
    print("  Touchpad  -> space")
    print("==========================================\n")

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

    print_controls_reference()

    try:
        while True:
            pygame.event.pump()  # Process events to get fresh values
            
            # Get D-pad values as buttons
            dpad_up = controller.get_button(11)
            dpad_down = controller.get_button(12)
            dpad_left = controller.get_button(13)
            dpad_right = controller.get_button(14)
            
            # Add triggers and bumpers
            left_trigger = controller.get_axis(4) > 0.5  # L2 trigger
            right_trigger = controller.get_axis(5) > 0.5  # R2 trigger
            left_bumper = controller.get_button(9)  # L1
            right_bumper = controller.get_button(10)  # R1
            touchpad = controller.get_button(15)  # Touchpad click - corrected button number
            
            # Common button mappings
            button_x = controller.get_button(0)  # × button - EXAMINE
            button_o = controller.get_button(1)  # ○ button - INVENTORY
            button_square = controller.get_button(2)  # □ button - OPEN
            button_triangle = controller.get_button(3)  # △ button - CLOSE
            
            # Check D-pad inputs and send corresponding key presses
            if dpad_up:
                pyautogui.typewrite('n\n')
                time.sleep(0.5)
            elif dpad_down:
                pyautogui.typewrite('s\n')
                time.sleep(0.5)
            elif dpad_left:
                pyautogui.typewrite('w\n')
                time.sleep(0.5)
            elif dpad_right:
                pyautogui.typewrite('e\n')
                time.sleep(0.5)

            # Check trigger, bumper and button inputs
            if left_trigger:
                pyautogui.typewrite('look\n')
                time.sleep(0.5)
            elif right_trigger:
                pyautogui.typewrite('get all\n')
                time.sleep(0.5)
            elif left_bumper:
                pyautogui.typewrite('help\n')
                time.sleep(0.5)
            elif right_bumper:
                pyautogui.typewrite('wait\n')
                time.sleep(0.5)
            elif touchpad:
                pyautogui.press('space')
                time.sleep(0.5)
            elif button_x:
                pyautogui.typewrite('x \n')  # × button - examine
                time.sleep(0.5)
            elif button_o:
                pyautogui.typewrite('i\n')  # ○ button - inventory
                time.sleep(0.5)
            elif button_square:
                pyautogui.typewrite('open \n')  # □ button - open
                time.sleep(0.5)
            elif button_triangle:
                pyautogui.typewrite('close \n')  # △ button - close
                time.sleep(0.5)

            time.sleep(0.1)  # Small delay to make output readable
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
