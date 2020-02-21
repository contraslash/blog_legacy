from core import models


def extract_and_transform():
    all_posts = models.BlogEnginePost.objects.all()
    all_post_serializerd = models.BlogSerializer(all_posts,  many=True).data

    for p in all_posts:
        f = open("posts_md/{}-{}.md".format(p.id, p.slug), "w+")
        f.write("Title: {}\n".format(p.title))
        f.write("Date: {}\n".format(p.created.isoformat()))
        f.write("Description: {}\n".format(p.short_description))
        tags = models.BlogEnginePostTags.objects.filter(post=p)
        f.write("Tags: {}\n".format(",".join((tag.tag.name for tag in tags))))
        f.write("---\n")
        f.write("# {}\n\n".format(p.title))
        f.write(p.body_markdown)
        f.close()

    f = open("README.md", "w+")
    for p in all_posts:
        f.write("- [{id}-{nombre}]('posts_md/{id}-{slug}.md)\n".format(id=p.id, nombre=p.title,slug=p.slug))

    f.close()


if __name__ == '__main__':
    extract_and_transform()
