import pyautogui
import pyperclip
import time
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key= # ADD YOUR API KEY 
)

# Function to check if the last message is from Arya
def check_if_last_message_from_sender(chat_history):
    # Split the chat history by lines to separate messages
    lines = chat_history.strip().split('\n')
    
    # Get the last line (the last message)
    last_message = lines[-1]
    
    # Check if 'Arya:' is in the last message, indicating it's from Arya
    if "sender:" in last_message:
        return True
    else:
        return False

# Step 1: Click on the icon at (1410, 1061)
pyautogui.click(1410, 1061) # marks your secure point where you what place the message chat is present.

# Give some time for the click action
time.sleep(1)

# Step 2: Drag from (577, 527) to (868, 948) to select text
pyautogui.moveTo(536 ,314)  # Move the mouse to the start position it like yuor secure point.
time.sleep(0.5)  # Add a slight delay to ensure the move action
pyautogui.dragTo(646 ,956, duration=1.0, button='left')  # Drag to the end position

# Give some time for the selection to happen
time.sleep(1)

# Step 3: Copy the selected text to the clipboard using keyboard shortcut Ctrl+C
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# Step 4: Get the copied text from the clipboard and store it in a variable
chat_history = pyperclip.paste()

# Print the copied text
print("Copied text:", chat_history)

print(check_if_last_message_from_sender(chat_history))
# Check if the last message is from Arya
if check_if_last_message_from_sender(chat_history):

    # Step 5: Use OpenAI to generate a response based on the copied text
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Unais skilled in general tasks like Aleva and Google Cloud."},
            {"role": "user", "content": chat_history}
        ]
    )

    # Get the response from OpenAI
    response = completion.choices[0].message['content']

    # Print the OpenAI response
    print("Response from OpenAI:", response)

    # Step 6: Click on the chatbox at (717, 975) to focus
    pyautogui.click(717, 975)

    # Step 7: Wait for the field to be ready (optional, adjust delay if needed)
    time.sleep(1)

    # Step 8: Type the generated response in the chatbox
    pyautogui.write(response)

    # Step 9: Press Enter to send the message
    pyautogui.press('enter')
else:
    print("The last message is not from sender.")
