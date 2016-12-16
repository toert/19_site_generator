import jinja2
import json
import argparse
from os.path import join, split, exists
from os import makedirs
from re import sub
from markdown import markdown


DIR_TO_SAVE = 'pages'


def parse_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('config',
                        help='enter the filepath to your config')
    return parser.parse_args()


def load_json(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as data:
        return json.load(data)


def convert_md_to_html(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as data:
        return markdown(data.read(), extensions=['codehilite', 'fenced_code'])


def get_article_url(source):
    source_with_dir = join(DIR_TO_SAVE, source)
    source = sub(r'.md\b', '.html', source_with_dir)
    return source


def create_dir_for_file(path):
    if not exists(split(path)[0]):
        makedirs(split(path)[0])


def compile_index_html(config, path_to_tempate='templates/index.html'):
    html_page = open(path_to_tempate, encoding = 'utf-8').read()
    template = jinja2.Template(html_page)
    for article in config['articles']:
        article['source'] = get_article_url(article['source'])
    filepath_to_save = join(DIR_TO_SAVE, 'index.html')
    render_page(config, filepath_to_save, template)


def compile_articles_html(config, path_to_template='templates/article.html'):
    html_page = open(path_to_template, encoding = 'utf-8').read()
    template = jinja2.Template(html_page)
    for article in config['articles']:
        info_about_article = {
            'title': article['title'],
            'topic': article['topic'],
            'text' : convert_md_to_html(join('articles', article['source']))
            }
        final_path = get_article_url(article['source'])
        create_dir_for_file(final_path)
        render_page(info_about_article, final_path, template)


def render_page(data, filepath, template):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template.render(info=data))


if __name__ == '__main__':
    parser = parse_path()
    path_to_config = parser.config
    compile_index_html(load_json(path_to_config))
    compile_articles_html(load_json(path_to_config))
