from rest_framework.serializers import ModelSerializer

from .models import Article, Category


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('path', 'depth', 'numchild',)
