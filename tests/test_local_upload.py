import subprocess
from src.helpers.local_upload import LocalUpload
from werkzeug.datastructures import FileStorage


def test_is_allowed_valid_extension(app):
    dummy_file = FileStorage(filename='a2_5sec.wav',
                             content_type='audio/x-wav')
    with app.app_context():
        my_local_upload = LocalUpload(dummy_file)
        assert my_local_upload.is_allowed()


def test_is_allowed_invalid_extension(app):
    dummy_file = FileStorage(filename='a2_5sec.midi',
                             content_type='audio/midi')
    with app.app_context():
        my_local_upload = LocalUpload(dummy_file)
        assert not my_local_upload.is_allowed()


def test_upload_size_limit(app):
    dummy_file = FileStorage(filename='/home/teagan/anaconda3/envs/simpletest/project/tests/resources/a2002011001-e02.wav',
                             content_type='audio/x-wav')

    with app.app_context():
        my_local_upload = LocalUpload(dummy_file)
        assert my_local_upload.save()

    # invoke bash script to delete test upload
    subprocess.call(['./tests/teardown.sh'])

