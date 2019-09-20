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
    author="Md. Sadhan Sarker",
    author_email="cse.sadhan@gmail.com",
    description="This is an Example Package",
    keywords="keyword1 keyword2",
    entry_points={
        'console_scripts': [
            'inktechs = inktechs.__main__:main'
        ]
    })

```

3.finally create `install.sh` file
    
    pip install -e .

    
4.Now, Run CLI, hit your package name from terminal

    inktechs -c ./home/file.conf --o ./home/text.file
    
> Output: like below

    Hello! from inktechs cli
    
    Update configuration as following: ./home/file.conf

    Generate output as following ./home/text.file
    
    

5.If you want to uninstall package, base on your cli package name

    pip uninstall inktechs-cli
    
    
    
    
# References
- https://docs.python.org/3/library/getopt.html
- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
- https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode