from setuptools import setup


setup(
    name="Paranoik",
    version="0.0.1",
    author="Jordan Jambazov",
    author_email="jordan.jambazov@gmail.com",
    keywords="backup",
    url="https://github.com/jordanjambazov/paranoik-backups",
    packages=['paranoik.backup', 'paranoik.backup.providers',
              'paranoik.compress', 'paranoik.syncers', 'paranoik.utils'],
)
