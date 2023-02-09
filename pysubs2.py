import pysubs2

# Load the subtitle file
subs = pysubs2.load("subtitles.srt")

# Extract the subtitle text
for line in subs:
    print(line.text)
