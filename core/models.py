from django.db import models

# Create your models here.
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

from rest_framework import serializers

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
"""

from core import models

all_posts = models.BlogEnginePost.objects.all()
all_post_serializerd = models.BlogSerializer(all_posts,  many=True).data

for p in all_posts:
    f = open("post_md/{}-{}.md".format(p.id,p.slug), "w+")
    f.write("Title: {}\n".format(p.title))
    f.write("Date: {}\n".format(p.created.isoformat()))
    f.write("Description: {}\n".format(p.short_description))
    tags = models.BlogEnginePostTags.objects.filter(post=p)
    f.write("Tags: {}\n".format(",".join((tag.tag.name for tag in tags))))
    f.write("---\n")
    f.write("# {}".format(p.title))
    f.write(p.body_markdown)
    f.close()

f = open("README.md", "w+")
for p in all_posts:
    f.write("- [{id}-{nombre}]('posts_md/{id}-{slug}.md)\n".format(id=p.id, nombre=p.title,slug=p.slug))

f.close()

"""