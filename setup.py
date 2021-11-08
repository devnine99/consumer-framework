import os

from setuptools import setup

VERSION = os.getenv('VERSION')

setup(
    name='consumer-framework',
    version=VERSION,
    description='Consumer Framework',
    author='devnine99',
    author_email='devnine99@gmail.com',
    url='https://github.com/devnine99/consumer-framework',
    license='MIT',
    python_requires='>=3',
    install_requires=['kafka-python>=2', 'pydantic>=1.8'],
    packages=['consumer_framework'],
    entry_points={
        'console_scripts': [
            'consumer = consumer_framework.__main__:main',
        ],
    }
)
