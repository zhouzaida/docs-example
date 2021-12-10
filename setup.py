from setuptools import find_packages, setup  # type: ignore

version_file = 'docs_example/version.py'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


setup(
    name='docs_example',
    version=get_version(),
    packages=find_packages(),
    python_requires='>=3.6',
)
