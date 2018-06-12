import pytest

from apps.core.models import Category
from .factories import CategoryFactory, ArticleFactory


@pytest.fixture
def root_category():
    category_name = CategoryFactory.build().name
    data = {'name': category_name}
    return Category.add_root(**data)


@pytest.fixture
def root_categories():
    category_names = [_.name for _ in CategoryFactory.build_batch(2)]
    categories = []
    for name in  category_names:
        categories.append(Category.add_root(**{'name': name}))
    return categories


@pytest.fixture
def article(root_categories):
    return ArticleFactory.create(categories=root_categories)


@pytest.fixture
def articles(root_categories):
    return ArticleFactory.create_batch(2, categories=root_categories)
