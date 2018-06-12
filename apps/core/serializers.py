from rest_framework import serializers
from treebeard.mp_tree import MP_AddChildHandler, MP_AddRootHandler

from .models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(label='Parent ID', required=False, source='get_parent.id')
    parent_name = serializers.CharField(read_only=True, required=False, source='get_parent.name')
    children = SubCategorySerializer(source='get_children', many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'parent_name', 'children',)

    def validate_parent(self, value):
        try:
            return Category.objects.get(pk=value).pk
        except Category.DoesNotExist:
            raise serializers.ValidationError('Parent category does exist.')

    def save(self, **kwargs):
        if 'parent' in self._validated_data:
            parent = self._validated_data['parent']
            return MP_AddChildHandler(parent, **self._validated_data).process()
        return MP_AddRootHandler(Category, **self._validated_data).process()
