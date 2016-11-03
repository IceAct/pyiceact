from setuptools import setup


setup(
    name='pyiceact',
    description='Package for IceAct data analysis',
    url='http://github.com/iceact/pyiceact',
    author='IceAct Collaboration',
    author_email='iceact@physik.rwth-aachen.de',
    license='MIT',
    packages=['iceact'],
    version='0.0.1',
    install_requires=[
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=3.0.0'],
    zip_safe=False,
)
