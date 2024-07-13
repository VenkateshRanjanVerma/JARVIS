# JARVIS

## Key Features and Functions

### Speak Functionality:
- Implemented a `speak()` function to convert text to speech using the `pyttsx3` library.
- Utilizes Microsoft's SAPI5 for voice synthesis.
- Supports different voice options (male and female).

### Greeting User:
- Created a `wishMe()` function to greet the user based on the current system time using the `datetime` module.

### Voice Command Recognition:
- Developed a `takeCommand()` function to capture voice commands via the system microphone using the `speechRecognition` library.
- Handles errors and converts spoken input into text using Google's speech recognition API.

### Executing Commands:
- **Wikipedia Searches:** Fetches summaries from Wikipedia based on user queries using the `wikipedia` library.
- **Web Browsing:** Opens websites like YouTube and Google using the `webbrowser` module.
- **Music Playback:** Plays music from a specified directory using the `os` module.
- **Time Query:** Tells the current time using the `datetime` module.
- **Application Launch:** Opens applications like VS Code using the `os` module.
- **Email Sending:** Sends emails using the `smtplib` library.

### Error Handling:
- Incorporated try-except blocks to manage errors and ensure smooth execution of tasks.

### Modular Code:
- Organized code into functions for readability and maintainability.
- Used conditional statements to execute tasks based on specific voice commands.
