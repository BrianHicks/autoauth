from setuptools import setup, find_packages

setup(
    name = 'Django Autoauth',
    version = '0.0.1',
    packages = find_packages(),

    install_requires = [
        'django',
    ],

    # testing
    #test_suite = 'nose.collector',
    #tests_require = [
        #'nose',
        #'mock',
    #],

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
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],

    long_description = open('README.md').read(),
)
