from setuptools import setup

setup(
    name='unbabel_cli',
    version='1.0.0',
    url='https://github.com/J88G/backend-engineering-challenge',
    project_urls={
        "Documentation": "https://github.com/J88G/backend-engineering-challenge/blob/master/README.md",
        "Code": "https://github.com/J88G/backend-engineering-challenge",
    },
    author='Joao Luz',
    maintainer="Joao Luz",
    description="Command line application that parses a stream of events and produces"
                " an aggregated output, calculating for every minute, a moving average"
                " of the translation delivery time for the last X minutes.",
    packages=['unbabel_cli'],
    include_package_data=True,
    install_requires=['click', ],
    entry_points='''
        [console_scripts]
        unbabel_cli=unbabel_cli.__main__:main
        '''
)