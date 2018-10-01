import subprocess, os, pytest
from werkzeug.utils import secure_filename


def test_local_upload_init(test_uploader):
    """Verifies that LocalUpload instantiates with secure filename."""
    my_local_upload, dummy_file, app = test_uploader

    with app.app_context():
        assert my_local_upload.filename
        assert my_local_upload.filename == secure_filename(dummy_file.filename)


def test_local_upload_get_upload_path(test_uploader):
    """Tests LocalUpload upload path is not None."""
    my_local_upload, dummy_file, app = test_uploader

    with app.app_context():
        assert my_local_upload.get_upload_path()


def test_local_upload_save_none(test_uploader):
    """Verify exception is raise when saving None."""
    my_local_upload, dummy_file, app = test_uploader
    my_local_upload.filename = None

    with app.app_context():
        with pytest.raises(TypeError):
            my_local_upload.save()


def test_local_upload_save_valid(test_uploader):
    """Verify presence of saved file locally."""
    my_local_upload, dummy_file, app = test_uploader

    with app.app_context():
        # save file locally-- no return type, so nothing to check
        my_local_upload.save()

        # verify that file has been saved to upload directory
        dummy_name = secure_filename(dummy_file.filename)
        assert dummy_name in os.listdir(app.config['UPLOAD_FOLDER'])

        # invoke bash script to delete test upload
        subprocess.call(['./tests/teardown.sh'])
