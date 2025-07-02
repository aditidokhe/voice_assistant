import pyttsx3
import pywhatkit
import datetime
import pyjokes

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello! I'm your typing-based assistant. Type a command below:")

    while True:
        command = input("You: ").lower()

        if 'play' in command:
            song = command.replace('play', '')
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand that. Try something else.")

if __name__ == "__main__":
    main()
    
