from flask import Blueprint, jsonify, request
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
        file = request.files['file']
        print(file.filename)
        #TODO: add file validation as seen in file upload example
        #print(type(file))
        #print(file.mimetype)

        # validates extension and file size, saves to server temporarily
        #uploader = FileUploader(file, LocalUpload)
        #return uploader.save()

    return 'This appears if the request method is not POST.'

#TODO: instance/uploads needs to be generated with project
#TODO: create custom errors