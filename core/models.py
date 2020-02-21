from django.db import models
from rest_framework import serializers


class BlogEnginePost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=50)
    body = models.TextField()
    body_markdown = models.TextField()
    visible = models.IntegerField()
    removed = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    short_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_engine_post'


class BlogEngineTag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=50)
    short_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_engine_tag'


class BlogEnginePostTags(models.Model):
    post = models.ForeignKey(BlogEnginePost, models.DO_NOTHING)
    tag = models.ForeignKey('BlogEngineTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_engine_post_tags'
        unique_together = (('post', 'tag'),)


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEnginePost
        fields = [
            'title',
            'slug',
            'short_description',
            'body_markdown',
            'visible',
            'created'

        ]
