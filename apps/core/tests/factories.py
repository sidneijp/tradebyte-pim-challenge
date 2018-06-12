import factory

from apps.core.models import Article, Category


class ArticleFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    sku = factory.Sequence(lambda n: 'TST-FAC-ART-%s' % n)
    ean = factory.Faker('ean13')
    stock = factory.Sequence(lambda n: n)
    price = factory.Sequence(lambda n: n + 0.111)

    class Meta:
        model = Article

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = Category