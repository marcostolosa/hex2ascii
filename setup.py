from setuptools import setup

setup(
    name='hex2Ascii',
    packages=[
        'hex2Ascii'
    ],
    version="0.0.1",
    entry_points={
        'console_scripts' : [
            'hex2Ascii = hex2Ascii.hex2Ascii:main'
        ],
    },
)