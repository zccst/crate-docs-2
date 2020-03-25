from okchain1.theme.rtd.conf.crate_reference import *

source_suffix = '.rst'
site_url = 'https://zc-crate-docs-04.readthedocs.io/en/stable/'

exclude_patterns = ['out/**', 'tmp/**', 'eggs/**', 'requirements.txt', 'README.rst']

extensions = ['crate.sphinx.csv', 'sphinx_sitemap']

# crate.theme sets html_favicon to favicon.png which causes a warning because
# it should be a .ico and in addition there is no favicon.png in this project
# so it can't find the file
html_favicon = None
