from setuptools import setup

setup(
    name='inktechs-cli',
    version='0.1.0',
    packages=['inktechs'],
    author="Md. Sadhan Sarker",
    author_email="cse.sadhan@gmail.com",
    description="This is an Example Package",
    keywords="keyword1 keyword2",
    entry_points={
        'console_scripts': [
            'inktechs = inktechs.__main__:main'
        ]
    })
