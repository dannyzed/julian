from distutils.core import setup


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = ''


setup(
  name='julian',
  packages=['julian'],
  version='0.14',
  description='Simple library for converting between Julian calendar dates and datetime objects',
  long_description=long_description,
  author='Daniel Zawada',
  author_email='zawadadaniel@gmail.com',
  url='https://github.com/dannyzed/julian',
  download_url='https://github.com/dannyzed/julian/tarball/0.14',
  keywords=['julian', 'calendar', 'datetime'],
  classifiers=[],
)
