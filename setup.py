from setuptools import setup
from eclingo.main import __version__


with open('README.md', mode='r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='eclingo',
    version=__version__,
    description='A solver for epistemic logic programs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Javier Garea',
    author_email='javier.garea@udc.es',
    url='https://github.com/potassco/eclingo',
    license='MIT',
    keywords=[
        'artificial intelligence',
        'logic programming',
        'answer set programming',
        'epistemic specifications'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    python_requires='>=3.6',
    packages=[
        'eclingo',
        'eclingo.preprocessor',
        'eclingo.parser',
        'eclingo.solver',
        'eclingo.postprocessor',
        'eclingo.utils'
    ],
    entry_points={
        'console_scripts': ['eclingo=eclingo.__main__:main']
    },
    include_package_data=True
)
