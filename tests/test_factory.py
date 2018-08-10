from src import create_app


def test_config():
    """Test create_app with various configs/mappings/no configs."""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
    # is there a way to test if the instance config is loaded?


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'

