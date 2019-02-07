from distutils.core import setup

setup(
    name='pylicense',
    license='MIT',
    version='0.1',
    py_modules=['pylicense'],
    install_requires=[
        'bs4',
        'lxml'
    ],
)
