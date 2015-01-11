from setuptools import setup, find_packages


EXCLUDE_FROM_PACKAGES = ['paranoik.tests']


setup(
    name="Paranoik",
    version="0.0.7",
    author="Jordan Jambazov",
    author_email="jordan.jambazov@codeideo.com",
    keywords="backup",
    url="https://github.com/codeideo/paranoik-backups",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=[
        "six"
    ]
)
