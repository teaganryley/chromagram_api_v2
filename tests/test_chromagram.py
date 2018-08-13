def test_request_methods_get(client):
    """Test server response to GET."""
    assert client.get('/chromagram').status_code == 405


def test_request_methods_post_valid(app):
    """Test server response to POST request with no attached file name."""
    path_to_file = app.config['TEST_WAV']
    client = app.test_client()
    data = {}

    with open(path_to_file, 'rb') as f:
        data['file'] = (f, f.name)
        assert client.post('/chromagram', content_type='multipart/form-data', data=data).status_code == 200


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