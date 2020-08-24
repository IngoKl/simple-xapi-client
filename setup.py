from setuptools import setup, find_packages

setup(
    name='simplexapiclient',
    version='0.0.1',
    url='https://github.com/IngoKl/simple-xapi-client.git',
    author='Ingo Kleiber',
    author_email='ikleiber@gmail.com',
    description='A minimalistic xAPI client written in Python',
    packages=find_packages(),    
    install_requires=['requests', 'pytest'],
)