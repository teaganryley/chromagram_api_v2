from flask import Blueprint, jsonify, request
from .helpers.local_upload import LocalUpload
from .helpers.audio_model import AudioModel
from .helpers import build_chroma

# create blueprint
bp = Blueprint('chromagram', __name__)


@bp.route('/chromagram', methods=('POST',))
def chromagram():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part.', 400

        file = request.files['file']

        if file.filename == '':
            return 'No selected file.', 400

        current_audio = AudioModel(file, LocalUpload)
        if current_audio.is_valid():
            return jsonify(chromagram=build_chroma.analyze(current_audio.save_file()))

    return 'This appears if the request method is not POST.'


#TODO: add garbage collection to server?