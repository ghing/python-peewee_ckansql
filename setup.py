from distutils.core import setup

setup(
    name='peewee_ckansql',
    version='0.1.0dev',
    author='Geoffrey Hing',
    author_email='geoffhing@gmail.com',
    packages=['peewee_ckansql',],
    license='LICENSE.txt',
    description='Python Database API',
    long_description=open('README.rst').read(),
    install_requires=[
        'peewee',
        'ckansql',
    ],
    test_requires=[
        'nose',
    ],
    test_suite='nose.collector',
)
