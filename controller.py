import pygame
import time

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
            
            # Get left stick X and Y values
            left_x = round(controller.get_axis(0), 3)  # Round to 3 decimal places
            left_y = round(controller.get_axis(1), 3)
            
            # Get D-pad values as buttons
            # DualSense D-pad buttons are typically 11-14
            dpad_up = controller.get_button(11)
            dpad_down = controller.get_button(12)
            dpad_left = controller.get_button(13)
            dpad_right = controller.get_button(14)
            
            dpad_x = dpad_right - dpad_left  # Will be 1 (right), -1 (left), or 0
            dpad_y = dpad_up - dpad_down     # Will be 1 (up), -1 (down), or 0
            
            print(f"Left Stick - X: {left_x:>6}, Y: {left_y:>6} | D-pad - X: {dpad_x:>2}, Y: {dpad_y:>2}", end='\r')
            time.sleep(0.1)  # Small delay to make output readable
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
