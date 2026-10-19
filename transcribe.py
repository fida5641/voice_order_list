from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="int8")
segments, info = model.transcribe("order.mp3")

text = " ".join(segment.text for segment in segments)
print(text)
