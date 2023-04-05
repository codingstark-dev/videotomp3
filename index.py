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
    return Response(audio_bytes, mimetype="audio/mp3")


if __name__ == '__main__':
    app.run(
        debug=True
    )
