from setuptools import setup


setup(
    name='gsbib',
    version='1.0',
    license='MIT',
    description='Google Scholar Bibtex Entries',
    url='https://github.com/jiamings/scholar_bibtex_keys',
    author='Jiaming Song',
    author_email='jiaming.tsong@gmail.com',
    keywords='google scholar bibtex',
    packages=['gsbib'],
    entry_points={
        'console_scripts': ['gsbib=gsbib:main'],
    },
    include_package_data=True,
    zip_safe=False,
)
