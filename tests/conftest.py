import os
import sys

# ensures pytest will locate project without having to run setup.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from werkzeug.datastructures import FileStorage
from src import create_app
from src.helpers.audio_model import AudioModel
from src.helpers.local_upload import LocalUpload


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({
        'TESTING': True,
        'TEST_WAV': '/home/teagan/anaconda3/envs/simpletest/project/tests/resources/a2_5sec.wav',
        'TEST_WAV_LG': '/home/teagan/anaconda3/envs/simpletest/project/tests/resources/a2002011001-e02.wav',
        'MAX_CONTENT_LENGTH': 8 * 1024 * 1024,
        'ALLOWED_EXTENSIONS': {'txt', 'wav', 'mp3'},
        'UPLOAD_FOLDER': '/home/teagan/anaconda3/envs/simpletest/project/tests/uploads'
    })

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def test_model(app):
    with app.app_context():
        dummy_file = FileStorage(filename=app.config['TEST_WAV'], content_type='audio/x-wav')
        test_model = AudioModel(file=dummy_file,
                                module=LocalUpload)
        return test_model, app


@pytest.fixture
def test_uploader(app):
    with app.app_context():
        dummy_file = FileStorage(filename=app.config['TEST_WAV'], content_type='audio/x-wav')
        return LocalUpload(dummy_file), dummy_file, app
