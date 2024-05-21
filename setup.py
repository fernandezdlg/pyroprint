from setuptools import setup

setup(
    name='pyroprint',
    version='0.1',  # specify your version here
    description='A CLI tool for printing Fire arguments',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # this line is necessary for markdown to render correctly
    url='https://github.com/fernandezdlg/print-fire-cli-arguments', # replace with your repository URL
    author='Juan Fernandez',  # replace with your name
    author_email='juanfernandezdlg@gmail.com',  # replace with your email
    license='GPLv3',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    packages=['pyroprint'],
    python_requires='>=3.9',
    install_requires=[
        'fire',
    ],
    entry_points={
        'console_scripts': [
            'pyroprint=pyroprint.print_arguments:main',
        ],
    },
)