from setuptools import setup

setup(
    name='inktechs-cli',
    version='0.1.0',
    packages=['inktechs'],
    entry_points={
        'console_scripts': [
            'inktechs = inktechs.__main__:main'
        ]
    })
