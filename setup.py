from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='mlsage_pyclient',
    url='https://github.com/myurushkin/mlsage-pyclient',
    author='Mikhail Yurushkin',
    author_email='m.yurushkin@gmail.com',
    # Needed to actually package something
    packages=['mlsage_pyclient'],
    # Needed for dependencies
    install_requires=['requests'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Python API for MLSage',
)