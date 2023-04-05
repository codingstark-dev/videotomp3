## Convert any video url to an MP3 file using Python and Flask


The endpoint uses the moviepy library to extract the audio from the video at the provided URL, saves it as an MP3 file, reads the file as bytes, removes the file, and returns the bytes as a response with the MIME type audio/mpeg.

<!-- create repo clone -->

```bash
git clone https://github.com/codingstark-dev/videotomp3.git
```

Here is a breakdown of the code:

```python
from flask import Flask, request, Response
import moviepy.editor as mp
import io
import os

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert():
    video_url = request.args.get('url')
    # video_url = request.query_string['video_url']
    video = mp.VideoFileClip(video_url)
    audio = video.audio
    audio_path = os.path.join(os.getcwd(), 'audio.mp3')
    audio.write_audiofile(audio_path)
    with open(audio_path, 'rb') as f:
        audio_bytes = f.read()
    os.remove(audio_path)
    return Response(audio_bytes, mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run()

```
