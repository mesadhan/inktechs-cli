# Inktechs-CLI


# Implementation Guide

1.Step: Create `inktechs` package

create '__init__.py' file. it should be empty,
Now, create `__main__.py` file

```python
def main():
    print('Hello! from inktechs cli')

if __name__ == '__main__':
    main()
```


2.Step: Then, create `setup.py` file and define meta for your CLI

```python
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
```

3. finally create `install.sh` file and addd
    
    pip install -e .

    
