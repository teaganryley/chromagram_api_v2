from flask import Blueprint, jsonify, request, current_app
from .helpers.file_uploader import FileUploader
from .helpers.local_upload import LocalUpload
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

        print(type(file))
        #if file and is_allowed(file):
            #uploader = FileUploader(file, LocalUpload)
            #return jsonify(chromagram=build_chroma.analyze(uploader.save()))

    return 'This appears if the request method is not POST.'


def is_allowed(file):
    return '.' in file.filename and \
        file.filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


# current_audio = new AudioModel(req.files['file'])
# # if current_audio.is_valid()
# #      return generate_chromagram(current_audio.get_path())
# # endif