from setuptools import setup, find_packages

setup(
    name = 'Django Autoauth',
    version = '0.0.0',
    packages = find_packages(),

    install_requires = [
        'django >= 1.3.1',
    ],

    # testing
    test_suite = 'runtests.runtests',
    tests_require = [
        'nose',
        'django-nose',
        'mock',
    ],

    # metadata for PyPi and others
    author = 'Brian Hicks',
    author_email = 'brian@brianthicks.com',
    description = 'Automatic Authentication for Django',
    license = 'TODO',
    url = 'https://github.com/BrianHicks/autoauth',
    download_url = 'https://github.com/BrianHicks/autoauth',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],

    long_description = open('README.md').read(),
)
