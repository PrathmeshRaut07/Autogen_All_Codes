import pyautogui
import cv2
import numpy as np
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load AutoGen configuration
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Function to capture the screen
def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

# Function to process the image and generate a response
def process_image_and_respond(image):
    # Example: Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Example: Detect edges in the image
    edges = cv2.Canny(gray_image, 100, 200)
    
    # Example: Save the processed image
    cv2.imwrite("processed_image.png", edges)
    
    # Example: Generate a response based on the processed image
    response = "I have processed the screen capture and detected edges. The processed image is saved as 'processed_image.png'."
    return response

# Create an AutoGen AssistantAgent
vision_agent = AssistantAgent(
    name="vision_agent",
    llm_config={"config_list": config_list},
)

# Create a UserProxyAgent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "."},
)

# Define a function to handle the conversation
def vision_agent_conversation():
    # Capture the screen
    screen_image = capture_screen()
    
    # Process the image and generate a response
    response = process_image_and_respond(screen_image)
    
    # Send the response to the user
    user_proxy.send_message(vision_agent, response)

# Start the conversation
vision_agent_conversation()