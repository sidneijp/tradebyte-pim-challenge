import pytest

from apps.core.models import Article
from . import factories


@pytest.mark.django_db
def test_create_article(authenticated_client, root_categories):
    article = factories.ArticleFactory.build(categories=root_categories)
    data = {
        'sku': article.sku,
        'ean': article.ean,
        'name': article.name,
        'stock': article.stock,
        'price': article.price,
    }
    response = authenticated_client.post('/api/articles/', data)
    assert response.status_code == 201
    last_inserted_article = Article.objects.last()
    assert last_inserted_article.sku == article.sku


@pytest.mark.django_db
def test_list_articles(authenticated_client, articles):
    expected_amount = len(articles)
    response = authenticated_client.get('/api/articles/')
    assert response.status_code == 200
    amount = len(response.json())
    assert expected_amount == amount


@pytest.mark.django_db
def test_get_article(authenticated_client, article):
    response = authenticated_client.get('/api/articles/%s/' % article.id)
    assert response.status_code == 200
    json_response = response.json()
    assert article.id == json_response.get('id')
    expected_fields = ('id', 'sku', 'ean', 'name', 'stock', 'price', 'categories')
    fields = json_response.keys()
    for expected_field in expected_fields:
        assert expected_field in fields
    assert len(expected_fields) == len(fields)


@pytest.mark.django_db
def test_delete_article(authenticated_client, article):
    response = authenticated_client.delete('/api/articles/%s/' % article.id)
    assert response.status_code == 204
    invalid_id = 'invalid'
    response = authenticated_client.delete('/api/articles/%s/' % invalid_id)
    assert response.status_code == 404


@pytest.mark.django_db
def test_unauthorized_api_call(client, articles):
    response = client.get('/api/articles/')
    assert response.status_code == 401
