from rest_framework import serializers
from treebeard.mp_tree import MP_AddChildHandler, MP_AddRootHandler

from .models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.CharField(required=False)

    class Meta:
        model = Category
        exclude = ('path', 'depth', 'numchild',)

    def validate_parent(self, value):
        try:
            return Category.objects.get(pk=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError('Parent category does exist.')

    def save(self, **kwargs):
        if 'parent' in self._validated_data:
            parent = self._validated_data['parent']
            return MP_AddChildHandler(parent, **self._validated_data).process()
        return MP_AddRootHandler(Category, **self._validated_data).process()
