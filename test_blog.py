import pytest
from unittest.mock import Mock, patch
from blog import Blog

api_response_2 = [
    {'userId': 3, 'id': 3, 'title': 'Outro Titulo 1', 'body': 'Outro Conteudo do blog 1'},
    {'userId': 4, 'id': 4, 'title': 'Outro Titulo 2', 'body': 'Outro Teste de conteudo do blog 2'}
]

@pytest.fixture
def mock_requests_get_2():
    with patch('blog.requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def blog_instance_2(mock_requests_get_2):
    mock_requests_get_2.return_value.json.return_value = api_response_2
    return Blog()

def test_posts_2(blog_instance_2):
    result = blog_instance_2.posts()
    assert result == api_response_2

def test_post_by_user_id_2(blog_instance_2, mock_requests_get_2):
    mock_requests_get_2.return_value.json.return_value = api_response_2[0]
    result = blog_instance_2.post_by_user_id(3)
    assert result == api_response_2[0]
