from setuptools import setup


setup(
    name='pyiceact',
    description='Package for IceAct data analysis',
    url='http://github.com/iceact/pyiceact',
    author='IceAct Collaboration',
    author_email='iceact@physik.rwth-aachen.de',
    license='MIT',
    packages=[
        'iceact',
        'iceact/resources',
    ],
    version='0.0.1',
    install_requires=[
        'matplotlib>=1.5',
        'eventio>=0.2.1',
    ],
    package_data={
        'resources': '*',
    },
    entry_points={
        'console_scripts': 'iceact-instrument-response=iceact.instrument_response:main',
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=3.0.0'],
    zip_safe=False,
)
