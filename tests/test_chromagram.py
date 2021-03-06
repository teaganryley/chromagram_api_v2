
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

