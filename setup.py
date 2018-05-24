from setuptools import setup

setup(
    name='hex2ascii',
    packages=[
        'hex2ascii'
    ],
    version="0.0.1",
    entry_points={
        'console_scripts' : [
            'hex2ascii = hex2ascii.hex2ascii:main'
        ],
    },
)