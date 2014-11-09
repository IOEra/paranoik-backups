from setuptools import setup, find_packages


EXCLUDE_FROM_PACKAGES = ['paranoik.tests']


setup(
    name="Paranoik",
    version="0.0.5",
    author="Jordan Jambazov",
    author_email="jordan.jambazov@gmail.com",
    keywords="backup",
    url="https://github.com/jordanjambazov/paranoik-backups",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES)
)
