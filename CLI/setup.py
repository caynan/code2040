from setuptools import setup

setup(
    name='CODE2040',
    version='0.1',
    py_modules=[
        'cli',
        'code2040',
    ],
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        # Colorama is only required for Windows.
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        code2040=cli:cli
    ''',
)
