import logging
import os

import markdown

LOGGER = logging.getLogger(__name__)

LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel("DEBUG")

SOURCE_FOLDER = "posts_md"
DEST_FOLDER = "content/blog"


def md_to_gatsby(source_folder=SOURCE_FOLDER, dest_folder=DEST_FOLDER):
    all_posts = os.listdir(source_folder)
    for post in all_posts:
        LOGGER.info(f"Generating file {post}")
        md = markdown.Markdown(extensions=["meta"])
        with open(os.path.join(SOURCE_FOLDER, post)) as post_file:
            md.convert(post_file.read())
        folder_name = os.path.join(DEST_FOLDER, post.split(".")[0])
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        with open(os.path.join(folder_name, "index.md"), "w+") as new_post:
            new_post.write("---\n")
            for meta, value in md.Meta.items():
                new_post.write(f"{meta}: \"{','.join(value)}\"\n")
            new_post.write("---\n")
            new_post.write('\n'.join(md.lines))


if __name__ == '__main__':
    md_to_gatsby()
