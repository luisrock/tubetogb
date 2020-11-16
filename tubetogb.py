import os
import sys

pathAudio = os.getcwd() + '/audio'
app = "/Applications/GarageBand.app"

#Receiving YouTube URL, file name and extension (optional, default = 'm4a') as args...
yt_url = sys.argv[1]
name = sys.argv[2]
extension = sys.argv[3] if 3 < len(sys.argv) else 'm4a'

pathMusic = f'{pathAudio}/{name}'

#Extracting audio from video
os.system(f'youtube-dl --extract-audio --audio-format {extension} --output "{pathMusic}.%(ext)s" {yt_url}')

#Open audio file with GarageBand
os.system(f"open -a {app} {pathMusic}.{extension}")

print(f'{pathMusic}.{extension} ... ready!')
quit()

