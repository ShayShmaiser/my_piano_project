import pytest
from unittest.mock import patch, MagicMock
import pygame
import pygame_gui
from pygame.locals import QUIT

# Mocking necessary Pygame and MongoDB components
pygame.font.init()

# Mock Button class
class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.pos = pos
        self.text_input = text_input
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color

    def changeColor(self, position):
        pass

    def update(self, screen):
        pass

    def checkForInput(self, position):
        return False

def get_font(size):
    return pygame.font.Font(None, size)

# Mock the MongoDB collection
mock_collection = MagicMock()

@patch('main.collection', mock_collection)  # Replace 'my_app' with your actual module name
@patch('main.main_menu')
@patch('main.login')
@patch('pygame.display.set_mode')
@patch('pygame.display.update')
@patch('pygame.event.get')
def test_register(mock_pygame_event_get, mock_display_update, mock_set_mode, mock_login, mock_main_menu):
    print("Starting test_register")
    
    # Create fake events
    events = [
        pygame.event.Event(pygame_gui.UI_TEXT_ENTRY_FINISHED, {'ui_object_id': '#username_entry', 'text': 'testuser'}),
        pygame.event.Event(pygame_gui.UI_TEXT_ENTRY_FINISHED, {'ui_object_id': '#password_entry', 'text': 'testpass'}),
        pygame.event.Event(QUIT)
    ]
    
    # Set side effect to return events sequentially and then empty list
    mock_pygame_event_get.side_effect = [events, []]
    mock_set_mode.return_value = MagicMock()

    # Import the register function and run it
    from main import register  # Replace 'my_app' with your actual module name
    try:
        print("Calling register function")
        register(max_iterations=2)  # Ensure this parameter is supported in your function
    except SystemExit:
        pass

    print("Checking assertions")
    mock_collection.insert_one.assert_called_once_with({"username": "testuser", "password": "testpass"})
    print("Test completed")

if __name__ == "__main__":
    pytest.main()