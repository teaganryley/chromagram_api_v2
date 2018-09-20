from flask import Blueprint, jsonify, request, current_app
from .helpers.file_uploader import FileUploader
from .helpers.local_upload import LocalUpload

# create blueprint
bp = Blueprint('chromagram', __name__)


@bp.route('/chromagram', methods=('POST',))
def chromagram():
    '''
    consume: wav file from body of request
    :return: json response containing matrix representing chromagram dzta
    '''
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part', 400

        file = request.files['file']

        if file.filename == '':
            return 'No selected file', 400

        if file and is_allowed(file):
            uploader = FileUploader(file, LocalUpload)
            #TODO: install librosa, write chromagram testing module
            #TODO: save file, then send to chromagram
            return 'Happiness'

    return 'This appears if the request method is not POST.'


#TODO: instance/uploads needs to be generated with project
def is_allowed(file):
    return '.' in file.filename and \
        file.filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']
