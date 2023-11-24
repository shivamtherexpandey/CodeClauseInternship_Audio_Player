# CodeClause_Internship_Audio_Player

This Python code creates a simple audio player application using the Tkinter and Pygame libraries. Here's a breakdown of its functionality:

1. **Imports:**
   - It imports necessary modules such as `pygame`, `tkinter`, `PIL` (Python Imaging Library), and their respective components for GUI, file dialog, message box, image handling, etc.

2. **Class `AudioPlayer`:**
   - It defines the main functionalities and interface for the audio player.
   - The constructor (`__init__`) initializes the GUI window using Tkinter.
   - Loads images for buttons (play, pause, browse) using the `PIL` library and displays them using Tkinter buttons.
   - It sets up the GUI elements, such as buttons for playing, pausing, and browsing audio files.
   - Initializes variables like `self.audio_file` to hold the selected audio file path and `self.playing` to track whether the audio is currently playing or paused.

3. **Methods:**
   - `browse_audio`: Opens a file dialog to select an audio file with specified extensions (`*.mp3 *.wav *.ogg *.flac`) and stores the chosen file path in `self.audio_file`.
   - `toggle_play_pause`: Toggles between playing and pausing the selected audio file. It utilizes `pygame.mixer` to handle audio playback. If an audio file is selected, it loads the file and plays or pauses it accordingly. It also updates the button image to display 'Play' or 'Pause' as appropriate.

4. **Main Section (`__name__ == "__main__"`):**
   - Creates the Tkinter window (`root`) and sets a background image using `PIL` and `ImageTk`.
   - Instantiates the `AudioPlayer` class within the Tkinter window.
   - Starts the main event loop (`root.mainloop()`) to run the application, enabling user interaction with the GUI elements.

Overall, this code creates a basic GUI audio player interface where users can select an audio file, play/pause the audio, and interact with buttons that display different images for play, pause, and file browsing operations.
