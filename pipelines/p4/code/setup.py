from setuptools import setup, find_packages

setup(
    name='p4',
    version='1.0',
    packages=find_packages(include=('job*',)),
    description='p4',
    install_requires=[
        'prophecy-libs==1.1.11'
    ],
    entry_points={
        'console_scripts': [
            'main = job.pipeline:main',
        ],
    },
    extras_require={
        'test': ['pytest', 'pytest-html'],
    }
)
