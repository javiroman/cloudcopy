from setuptools import setup, find_packages

setup(
    name='cloudcopy',
    version='0.0.1',
    author="Javi Roman",
    author_email="jroman.espinar@gmail.com",
    description="Agnostic Data Ingest Tool for Public Cloud (AWS, Azure)",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click==8.1.3',
        'JayDeBeApi',
        'openpyxl',
        'prettytable==3.7.0',
        'boto3==1.26.137'
    ],
    entry_points='''
        [console_scripts]
        cloudcopy=cloudcopy.main:main
    ''',
)
