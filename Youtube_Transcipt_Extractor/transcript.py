from youtube_transcript_api import YouTubeTranscriptApi

video_id = "CRtF9TdR2p8"

api = YouTubeTranscriptApi()

transcript = api.fetch(video_id)

with open("transcript.txt", "w", encoding="utf-8") as file:
    for item in transcript:
        file.write(item.text + "\n")

print("Transcript saved to transcript.txt")
