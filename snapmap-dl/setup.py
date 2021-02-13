import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='snapmap-dl',
    version='1.0.0',
    author='Siddharth Dushantha',
    author_email='siddharth.dushantha@gmail.com',
    description='Download stories from SnapMap with and without filter/overlay',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sdushantha/snapmap-dl',
    py_modules=['snapmap-dl'],
    scripts=['snapmap-dl/snapmap-dl']
)

