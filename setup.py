import sys
from distutils.core import setup

CURRENT_PYTHON_VERSION = sys.version_info[:2]
REQUIRED_PYTHON_VERSION = (3, 7)

if CURRENT_PYTHON_VERSION < REQUIRED_PYTHON_VERSION:
    sys.stderr.write(
    """
    ============================
    Unsupported Python Version
    ============================
    The required Python version to install facebook_fetcher is {}.{}+
    But it seems you are trying to install facebook_fetcher using Python version {}.{}.

    To resolve this issue, you may try upgrading the Python version you are currently using :)

    """.format(*(REQUIRED_PYTHON_VERSION + CURRENT_PYTHON_VERSION))
    )
    sys.exit(1)

with open('README.md', 'r', encoding='utf-8') as doc:
    readme = doc.read()

setup(
    name='facebook_fetcher',
    packages=['facebook_fetcher'],
    version='1.0.2',
    license='MIT',
    description='Facebook scraper / Fetcher Unlimited by Andry RL',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Andry RL',
    author_email='andryerics@gmail.com',
    url='https://github.com/Andryerics/facebook_fetcher',
    keywords=['facebook-scraper', 'facebook-parser', 'facebook-scraper-without-apikey'],
    python_requires=">=3.7",
    install_requires=[
        'requests_toolbelt',
        'requests',
        'bs4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only'
    ],
)
