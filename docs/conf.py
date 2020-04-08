from okchain1.theme.rtd.conf.okchain_docs import *

source_suffix = '.rst'
site_url = 'https://zc-crate-docs-04.readthedocs.io/en/stable/'

exclude_patterns = ['out/**', 'tmp/**', 'eggs/**', 'requirements.txt', 'README.rst']

extensions = [
    'crate.sphinx.csv',
    'sphinx_sitemap',
]

# crate.theme sets html_favicon to favicon.png which causes a warning because
# it should be a .ico and in addition there is no favicon.png in this project
# so it can't find the file
html_favicon = None



# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# def setup(app):
#    app.add_stylesheet('css/sphinx_rtd_theme.css')
