# Import the necessary libraries
import pyttsx3
import speech_recognition as sr

# Create a speech recognition object
recognizer = sr.Recognizer()

# Create a text-to-speech engine
engine = pyttsx3.init()

# Function to listen to the user's voice
def listen_to_user():
    print("Listening...")
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=1)
        audio = recognizer.listen(mic)

    try:
        user_said = recognizer.recognize_google(audio, language='en')
        print(f"User said: {user_said}")
        return user_said.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results. Please check your internet connection.")
        return ""

# Function to speak to the user
def speak_to_user(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet_user():
    speak_to_user("Hello! How can I assist you today?")

# Function to handle user commands
def handle_command(user_said):
    if 'hello' in user_said:
        greet_user()
    elif 'time' in user_said:
        speak_to_user("Sorry, I can't tell the time right now. Implement this feature.")
    elif 'search' in user_said:
        speak_to_user("Sorry, I can't perform searches right now. Implement this feature.")
    else:
        speak_to_user("I'm sorry, I don't understand that command.")

# Main function to run the assistant
def run_assistant():
    greet_user()
    while True:
        user_said = listen_to_user()
        if user_said:
            handle_command(user_said)

if __name__ == "__main__":
    run_assistant()
