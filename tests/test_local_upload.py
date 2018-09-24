import subprocess, os
from src.helpers.local_upload import LocalUpload
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


def test_local_upload_return_value(app):
    """Checks save() method returns True."""
    with app.app_context():
        dummy_file = FileStorage(filename=app.config['TEST_WAV'], content_type='audio/x-wav')
        my_local_upload = LocalUpload(dummy_file)
        assert my_local_upload.save()

    # invoke bash script to delete test upload
    subprocess.call(['./tests/teardown.sh'])


def test_local_upload_file_saving(app):
    """Checks save() method actually saves file to upload folder."""
    with app.app_context():
        dummy_file = FileStorage(filename=app.config['TEST_WAV'], content_type='audio/x-wav')
        my_local_upload = LocalUpload(dummy_file)
        my_local_upload.save()

        # verify that file has been saved to upload directory
        dummy_name = secure_filename(dummy_file.filename)
        assert dummy_name in os.listdir(app.config['UPLOAD_FOLDER'])

    # invoke bash script to delete test upload
    subprocess.call(['./tests/teardown.sh'])
