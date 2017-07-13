from distutils.core import setup

setup(
    name='steamformatter',
    version='0.1',
    packages=['steamformatter'],
    url='',
    license='GPLv3',
    author='granitosaurus',
    entry_points="""
        [console_scripts]
        steamf=steamformatter.cli:cli
    """,
    author_email='bernardas.alisauskas gmail.com',
    description='output steam game data to markdown'
)