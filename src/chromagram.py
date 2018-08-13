from flask import Blueprint, jsonify, request
#from .helpers.file_uploader import FileUploader
#from .helpers.local_upload import LocalUpload

# create blueprint
bp = Blueprint('chromagram', __name__)


@bp.route('/chromagram', methods=('POST',))
def chromagram():
    '''
    consume: wav file from body of request
    :return: json response containing matrix representing chromagram dzta
    '''
    #TODO: extension restriction
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return 'No file'
        if not file.filename or file.filename == '':
            return 'No file name'
        else:
            return
        #uploader = FileUploader(file, LocalUpload)
        #return uploader.save()

    return 'This appears if the request method is not POST.'
