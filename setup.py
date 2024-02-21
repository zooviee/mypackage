from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Zooviee example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/zooviee/mypackage',
    author='Oluwaseyi Akinsanya',
    author_email='Seyiakinsanya3@gmail.com'
)