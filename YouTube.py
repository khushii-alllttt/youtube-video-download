from pytube import YouTube

# Get video URL from user
video_url = input("Enter YouTube Video URL: ")

# Create YouTube object
yt = YouTube(video_url)

# Show basic video info
print("\nTitle:", yt.title)
print("Views:", yt.views)
print("Length:", yt.length, "seconds")

# Show available streams
print("\nAvailable Streams:")
for stream in yt.streams.filter(progressive=True, file_extension="mp4"):
    print(f"Resolution: {stream.resolution} | FPS: {stream.fps} | Type: {stream.mime_type}")

# Ask user for resolution
res = input("\nEnter desired resolution (e.g., 720p, 360p): ")

# Download video
stream = yt.streams.filter(progressive=True, file_extension="mp4", res=res).first()

if stream:
    print("\nDownloading...")
    stream.download()
    print("✅ Download Complete!")
else:
    print("❌ Resolution not available.")
