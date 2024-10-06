import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import os
from datetime import datetime
import time
import keyboard

if __name__ == "__main__":
    print("=========================")
    print("Author: [Nathaniel Tee]")
    print("License: MIT License")
    print("=========================")

# Function to normalize the audio data
def normalize_audio(audio_data):
    audio_data = audio_data / np.max(np.abs(audio_data))  # Normalize to max value 1.0
    audio_data = np.int16(audio_data * 32767)  # Convert to 16-bit PCM format (standard WAV)
    return audio_data

# Function to handle recording process
def record_audio(folder_path):  # Tambahkan folder_path sebagai parameter
    freq = 44100  # Sampling frequency
    print("Press 'S' to start recording...")
    
    # Wait until 'S' is pressed to start recording
    while True:
        if keyboard.is_pressed('s'):
            print("Recording started. Press 'Enter' to stop.")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            start_time = time.time()  # Get the start time
            recording_list = []  # To store chunks of recorded data
            
            # Start recording using callback to avoid missing data
            def callback(indata, frames, time, status):
                recording_list.append(indata.copy())  # Store the chunk of recorded audio
                
            with sd.InputStream(samplerate=freq, channels=1, callback=callback):
                while not keyboard.is_pressed('enter'):
                    elapsed_time = time.time() - start_time
                    print(f"Recording... {int(elapsed_time)} seconds", end='\r')
                    time.sleep(0.1)  # To reduce CPU usage
            
            # Stop recording and concatenate recorded chunks
            recording = np.concatenate(recording_list, axis=0)
            elapsed_time = time.time() - start_time
            print(f"\nRecording stopped at {int(elapsed_time)} seconds.")
            
            # Normalize the recorded audio
            recording_normalized = normalize_audio(recording)

            # Save file with timestamp
            filename = f"recording_{timestamp}.wav"
            file_path = os.path.join(folder_path, filename)  # Combine folder path and filename
            write(file_path, freq, recording_normalized)
            print(f"File saved as {file_path}")

            # Playback the recorded audio
            print("Playing back the recording...")
            sd.play(recording_normalized, freq)
            sd.wait()  # Wait until playback is finished
            print("Playback finished!")
            
            return  # Exit after recording is done

# Main logic to run recording
if __name__ == "__main__":
    # Set the folder path where you want to save recordings
    folder_path = "D:/Project Nathan/Recordings"  # Ganti dengan path folder yang diinginkan
    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
    record_audio(folder_path)  # Panggil fungsi dengan folder_path sebagai argumen
