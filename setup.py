from setuptools import find_packages, setup


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('bdc_readthedocs_theme', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='bdc-readthedocs-theme',
    version=version,
    description='Brazil Data Cube Theme for Sphinx readthedocs.',
    long_description=open('README.md').read(),
    author='Admin',
    author_email='admin@admin.com',
    url='https://github.com/brazil-data-cube/bdc-readthedocs-theme',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Sphinx>2'],
    license="MIT"
)
