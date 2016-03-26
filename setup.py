from distutils.core import setup


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setup(
  name='julian',
  packages=['julian'],
  version='0.13',
  description='Simple library for converting between Julian calendar dates and datetime objects',
  long_description=long_description,
  author='Daniel Zawada',
  author_email='zawadadaniel@gmail.com',
  url='https://github.com/dannyzed/julian',
  download_url='https://github.com/dannyzed/julian/tarball/0.13',
  keywords=['julian', 'calendar', 'datetime'],
  classifiers=[],
)