import wave

# Replace with your actual filename
with wave.open("sounds/shipcrash.wav", "rb") as num:
    print("--- AUDIO FILE DETAILS ---")
    print(f"Channels (1=Mono, 2=Stereo): {num.getnchannels()}")
    print(f"Sample Width (Bytes per sample): {num.getsampwidth()}")
    print(f"Frame Rate (FREQUENCY): {num.getframerate()} Hz")
