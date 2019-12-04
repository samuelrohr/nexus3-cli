# -*- coding: utf-8 -*-
import io
from setuptools import find_packages, setup

package_name = 'nexus3-cli'
package_version = '2.1.1'

requires = [
    'clint',
    'docopt',
    'future',
    'faker',
    'inflect',
    'py',
    'future',
    'requests[security]>=2.14.2',
    'six',
    'texttable'
]

test_requires = [
    'codecov',
    'flake8',
    'pytest',
    'pytest-cov',
    'pytest-helpers-namespace',
    'pytest-mock',
    'pytest-faker',
]

with io.open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    author='Thiago Figueiró',
    name=package_name,
    version=package_version,
    description='A python-based CLI for Sonatype Nexus OSS 3',
    url='https://github.com/thiagofigueiro/nexus3-cli',
    long_description=readme,
    long_description_content_type="text/markdown",
    setup_requires=["pytest-runner"],
    install_requires=requires,
    tests_require=test_requires,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6,<4',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'nexuscli': ['script/groovy/'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'nexus3=nexuscli.cli:main',
        ],
    },
    extras_require={'test': test_requires},
)
