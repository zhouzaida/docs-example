# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import pytorch_sphinx_theme

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'docs-example'
copyright = '2021, docs-example contributors'
author = 'docs-example contributors'

version_file = '../docs_example/version.py'
with open(version_file, 'r') as f:
    exec(compile(f.read(), version_file, 'exec'))
__version__ = locals()['__version__']
# The short X.Y version
version = __version__
# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx_markdown_tables',
    'myst_parser',
    'sphinx_copybutton',
]  # yapf: disable


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pytorch_sphinx_theme'
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]

html_theme_options = {
    'menu': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/open-mmlab/mmcv'
        },
        {
            'name':
            '文档',
            'children': [
                {
                    'name': 'MMCV',
                    'url': 'https://mmcv.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MIM',
                    'url': 'https://openmim.readthedocs.io/en/latest/'
                },
                {
                    'name': 'MMAction2',
                    'url': 'https://mmaction2.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMClassification',
                    'url':
                    'https://mmclassification.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMDetection',
                    'url': 'https://mmdetection.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMDetection3D',
                    'url':
                    'https://mmdetection3d.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMEditing',
                    'url': 'https://mmediting.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMGeneration',
                    'url': 'https://mmgeneration.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMOCR',
                    'url': 'https://mmocr.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMPose',
                    'url': 'https://mmpose.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMSegmentation',
                    'url':
                    'https://mmsegmentation.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMTracking',
                    'url': 'https://mmtracking.readthedocs.io/zh_CN/latest/',
                },
                {
                    'name': 'MMFlow',
                    'url': 'https://mmflow.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMFewShot',
                    'url': 'https://mmfewshot.readthedocs.io/zh_CN/latest/',
                },
            ]
        },
        {
            'name':
            'OpenMMLab',
            'children': [
                {
                    'name': '主页',
                    'url': 'https://openmmlab.com/'
                },
                {
                    'name': 'GitHub',
                    'url': 'https://github.com/open-mmlab/'
                },
                {
                    'name': '推特',
                    'url': 'https://twitter.com/OpenMMLab'
                },
                {
                    'name': '知乎',
                    'url': 'https://zhihu.com/people/openmmlab'
                },
            ]
        },
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/readthedocs.css']

# -- Extension configuration -------------------------------------------------
# Ignore >>> when copying code
copybutton_prompt_text = r'>>> |\.\.\. '
copybutton_prompt_is_regexp = True