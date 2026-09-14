import wave
import math
import struct

sample_rate = 44100
duration = 1.0
frequency = 1000

with wave.open("alarm.wav", "w") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for i in range(int(sample_rate * duration)):
        value = int(
            16000 * math.sin(
                2 * math.pi * frequency * i / sample_rate
            )
        )
        wav.writeframes(struct.pack("<h", value))

print("alarm.wav created successfully!")