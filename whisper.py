import whisper

model = whisper.load_model("large")
result = model.transcribe("sample.m4a",
                          language="ja", task="translate")
print(result["text"])
