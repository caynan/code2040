from setuptools import setup

setup(
    name='CODE2040',
    version='0.1',
    py_modules=[
        'cli',
    ],
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        # Colorama is only required for Windows.
        'colorama',
        'six',
    ],
    entry_points='''
        [console_scripts]
        code2040=cli:cli
    ''',
)
