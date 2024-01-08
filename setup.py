from setuptools import setup, find_packages

setup(
    name='spotify_package',
    version='0.1',
    author='MILAN BHAKTA',
    author_email='MILZBHAKTA@GMAIL.COM',
    description='A package for fetching, processing, and visualizing data from the Spotify API',
    url='https://github.com/milanbhakta/spotify_package',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv'
    ],
)