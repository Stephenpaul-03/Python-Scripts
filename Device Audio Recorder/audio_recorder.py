import os
import sounddevice as sd
import numpy as np
import wave
import signal
import sys

SAMPLE_RATE = 16000  
CHANNELS = 1         
audio_data = []

def find_device(device_name):
    devices = sd.query_devices()
    for idx, device in enumerate(devices):
        if device_name in device['name'] and device['max_input_channels'] > 0:
            print(f"Using device: {device['name']} (Index: {idx})")
            return idx
    return None

def signal_handler(sig, frame):
    print("\nRecording stopped.")
    save_to_wav(audio_file_path, np.concatenate(audio_data), SAMPLE_RATE)
    sys.exit(0)

def record_audio(device=None):
    print("Recording... Press CTRL+C to stop.")
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16', device=device) as stream:
        while True:
            data = stream.read(SAMPLE_RATE)[0]  
            audio_data.append(data) 

def save_to_wav(filename, audio_data, sample_rate):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())
    print(f"Audio saved to {filename}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    filename = input("Enter the filename (without extension) to save the audio: ")
    music_folder = os.path.join(os.path.expanduser("~"), "Music")
    os.makedirs(music_folder, exist_ok=True)  
    audio_file_path = os.path.join(music_folder, f"{filename}.wav")
    device_index = find_device("Stereo Mix")
    if device_index is None:
        print("Stereo Mix not found, trying to find an available audio device.")
        device_index = find_device("Virtual Cable")  
    
    if device_index is None:
        print("No appropriate audio input device found. Exiting.")
        sys.exit(1)

    record_audio(device=device_index)
