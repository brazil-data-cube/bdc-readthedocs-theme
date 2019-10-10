from setuptools import setup


setup(
    name='bdc-readthedocs-theme',
    version='0.1',
    description='Brazil Data Cube Theme for Sphinx readthedocs.',
    long_description=open('README.md').read(),
    author='Admin',
    author_email='admin@admin.com',
    url='https://github.com/brazil-data-cube/bdc-readthedocs-theme',
    packages=['bdc_theme'],
    include_package_data=True,
    install_requires=['Sphinx>2'],
    license="MIT"
)
