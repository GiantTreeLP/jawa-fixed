
from setuptools import setup, find_packages

setup(
    name='jawa-fixed',
    packages=find_packages(),
    version='2.3.1-2',
    python_requires='>=3.8',
    description='Doing fun stuff with JVM ClassFiles.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    maintainer='GiantTree',
    maintainer_email='gianttree@groundmc.net',
    url='https://github.com/GiantTreeLP/jawa-fixed',
    keywords=[
        'java',
        'disassembly',
        'disassembler',
        'assembly'
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Disassemblers',
        'Topic :: Software Development :: Assemblers'
    ],
    install_requires=[
        'click>=5.0',
        'mutf8>=1.0.5'
    ],
    tests_require=[
        'pytest>=2.10',
    ],
    extras_require={
        'dev': [
            'pytest',
            'sphinx',
            'sphinxcontrib-googleanalytics',
            'sphinx_rtd_theme',
            'sphinx-click',
            'ghp-import',
            'pyyaml',
            'ipython',
            'twine',
            'wheel',
            'bump2version',
            'flake8'
        ]
    },
    entry_points='''
    [console_scripts]
    jawa=jawa.cli:cli
    '''
)
