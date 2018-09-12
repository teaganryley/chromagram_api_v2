import os
import sys

# ensures pytest will locate project without having to run setup.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src import create_app
from src.helpers import file_uploader, local_upload


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({
        'TESTING': True,
        'TEST_WAV': '/home/teagan/anaconda3/envs/simpletest/project/tests/resources/a2_5sec.wav'
    })

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def uploader():
    """An uploader used in file_uploader and local_upload tests."""
    return file_uploader