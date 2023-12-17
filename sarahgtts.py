from gtts import gTTS
import os
import speech_recognition as sr
import webbrowser as wb

# Initialize the speech recognizer
r = sr.Recognizer()
chrome_path = "content\\Google\\Chrome\\Application\\chrome.exe %s"
def opening(text):
    if "open" in text.lower():
        words_to_exclude = ["open"]
        cleaned_text = ' '.join(word for word in text.split() if word.lower() not in words_to_exclude)
        speak("As per your wish, opening " + cleaned_text)

        query = text.lower().replace("open", "").strip()
        opening_url = "https://www.google.com/search?q=" + query
        wb.open(opening_url, new=2)
    else:
        speak("I'm sorry, I didn't understand your request.")

def speak(text, lang='en', slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save("output.mp3")
    os.system("start output.mp3")

with sr.Microphone() as source:
    print("Hello, my name is Sarah, an Artificial Intelligence . How may I help you?")
    speak("Hello, my name is Sarah, an Artificial Intelligence . How may I help you?", lang='en', slow=True)

    try:
        audio = r.listen(source, timeout=5)
        print('Ok, I understand')
        speak("Ok, I understand")

        text = r.recognize_google(audio, show_all=False)
        print("Recognized Text:", text)  # Print the recognized text for debugging

        opening(text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio. Please try again.")
        speak("Sorry, I could not understand the audio. Please try again.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speak("Could not request results from Google Speech Recognition service. Please try again.")


