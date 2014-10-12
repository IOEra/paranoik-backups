from setuptools import setup


setup(
    name="Paranoik",
    version="0.0.1",
    author="Jordan Jambazov",
    author_email="jordan.jambazov@gmail.com",
    license="BSD",
    keywords="backup",
    url="https://github.com/jordanjambazov/paranoik-backups",
    packages=['paranoik.backup', 'paranoik.compress', 'paranoik.syncers', 'paranoik.utils'],
)
