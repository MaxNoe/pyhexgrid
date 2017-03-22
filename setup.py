from setuptools import setup


setup(
    name='pyhexgrid',
    description='A numpy aware package for hexagonale grids',
    url='http://github.com/maxnoe/pyhexgrid',
    author='Maximilian Nöthe',
    author_email='maximilian.noethe@tu-dortmund.de',
    license='MIT',
    packages=['hexgrid'],
    version='0.1.0',
    install_requires=[
        'numpy',
        'pandas',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=3.0.0'],
    zip_safe=False,
)
