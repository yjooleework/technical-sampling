files = [
    "RS_20260922_01.mp3",
    "RS_20260922_02.mp3",
    "20260922_03.mp3",
    "RS_20260922_04.wav",
    "RS_20260922_05.mp3",
    "RS_20260922_06.flac"
]

for file in files:
    if not file.startswith("RS_"):
        print("PREFIX ERROR:", file)

    if not (
        file.endswith(".mp3")
        or file.endswith(".wav")
        or file.endswith(".flac")
    ):
        print("FORMAT ERROR:", file)
