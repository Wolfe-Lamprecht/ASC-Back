from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True
    )

    user_url = serializers.ModelSerializer.serializer_url_field(view_name='user_detail')

    class Meta:
        model = User
        fields = ('username', 'user_url', 'first_name', 'last_name', 'email', 'password', 'status', 'picture', 'posts')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='author'
    )

    class Meta:
        model = Post
        fields = ('title', 'author', 'author_id', 'body')