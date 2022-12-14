import setuptools

setuptools.setup(
    name='spasscli',
    version='1.0.0',
    description='Random password generator.',
    url='https://github.com/sorzkode/',
    author='sorzkode',
    author_email='<sorzkode@proton.me>',
    packages=setuptools.find_packages(),
    install_requires=['click', 'pyfiglet'],
    long_description='A random password generator with a CLI.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT',
        'Operating System :: OS Independent',
        ],
)