import pytest 
from bookmarks.models import Bookmark 


@pytest.mark.django_db
def test_create_new_bookmark(client):
    numrows = Bookmark.objects.count() 

    response = client.post('/bookmarks', {
        'title': 'YouTube',
        'url': 'https://www.youtube.com'
    })

    assert response.status_code == 201
    assert Bookmark.objects.count() == numrows+1

    o = Bookmark.objects.last()
    assert o.title == 'YouTube'
    assert o.url == 'https://www.youtube.com'


@pytest.mark.django_db
def test_delete_bookmark(client):
    bookmark = Bookmark.objects.create(
        title='YouTube',
        url='https://www.youtube.com'
    )

    response = client.delete(f'/bookmarks/{bookmark.id}')

    assert response.status_code == 204
    assert Bookmark.objects.count() == 0
