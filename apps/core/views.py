from rest_framework.viewsets import ModelViewSet

from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
