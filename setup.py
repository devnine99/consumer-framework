from setuptools import setup

setup(
    name='consumer-framework',
    version='0.0.2',
    description='Consumer Framework',
    author='devnine99',
    author_email='devnine99@gmail.com',
    url='https://github.com/devnine99/consumer-framework',
    license='MIT',
    python_requires='>=3',
    install_requires=['kafka-python>=2'],
    packages=['consumer_framework'],
)
