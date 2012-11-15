from setuptools import setup, find_packages

import cookie_message


setup(
    name='django-cookie-message',
    packages=find_packages(),
    include_package_data=True,
    version=cookie_message.__version__,
    description='',
    long_description=open('README.rst').read(),
    author=cookie_message.__author__,
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-cookie-message/',
    install_requires=[],
    zip_safe=False,
)
