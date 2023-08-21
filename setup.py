from setuptools import setup

setup(
    name='arithmopkg1',
    version='0.1',
    packages=['arithmopkg1'],
    entry_points={
        'console_scripts': [
            'arithmopkg1 = arithmopkg1.__main__:main',
        ],
    },
)
