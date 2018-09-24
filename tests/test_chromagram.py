from werkzeug.datastructures import FileStorage
from src.chromagram import is_allowed


def test_request_methods_get(client):
    """Test server response to GET."""
    assert client.get('/chromagram').status_code == 405


def test_request_methods_post_valid(app):
    """Test server response to POST request with valid file."""
    path_to_file = app.config['TEST_WAV']
    client = app.test_client()
    data = {}

    with open(path_to_file, 'rb') as f:
        data['file'] = (f, f.name)
        assert client.post('/chromagram', content_type='multipart/form-data', data=data).status_code == 200


def test_request_methods_post_valid_jsonify(app):
    """Test server's json response to POST request with valid name."""
    path_to_file = app.config['TEST_WAV']
    client = app.test_client()
    data = {}

    with open(path_to_file, 'rb') as f:
        data['file'] = (f, f.name)
        assert client.post('/chromagram', content_type='multipart/form-data', data=data).get_data()


def test_request_methods_post_no_file(client):
    """Test server response to POST request with no attached file."""
    assert client.post('/chromagram').status_code == 400


def test_request_methods_post_no_file_name(app):
    """Test server response to POST request with no attached file."""
    path_to_file = app.config['TEST_WAV']
    client = app.test_client()
    data = {}

    with open(path_to_file, 'rb') as f:
        data['file'] = (f, '')
        assert client.post('/chromagram', content_type='multipart/form-data', data=data).status_code == 400


def test_request_methods_post_file_too_large(app):
    """Tests that Flask rejects files over a certain limit."""
    path_to_file = app.config['TEST_WAV_LG']
    client = app.test_client()
    data = {}

    with open(path_to_file, 'rb') as f:
        data['file'] = (f, '')
        assert client.post('/chromagram', content_type='multipart/form-data', data=data).status_code == 413


def test_is_allowed_valid_extension(app):
    """Test is_allowed method properly accepts .wav files."""
    dummy_file = FileStorage(filename='a2_5sec.wav', content_type='audio/x-wav')
    with app.app_context():
        assert is_allowed(dummy_file)


def test_is_allowed_invalid_extension(app):
    """Test is_allowed properly rejects files not specified in ALLOWED_EXTENSIONS."""
    dummy_file = FileStorage(filename='a2_5sec.midi', content_type='audio/midi')
    with app.app_context():
        assert not is_allowed(dummy_file)


