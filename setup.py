import os
import re
import subprocess
from setuptools import setup, find_packages, Command

from mike.app_version import version

root_dir = os.path.abspath(os.path.dirname(__file__))


class Coverage(Command):
    description = 'run tests with code coverage'
    user_options = [
        ('test-suite=', 's',
         "test suite to run (e.g. 'some_module.test_suite')"),
    ]

    def initialize_options(self):
        self.test_suite = None

    def finalize_options(self):
        self.test_suite = self.test_suite.split(',') if self.test_suite else []

    def run(self):
        env = dict(os.environ)
        pythonpath = os.path.join(root_dir, 'test', 'scripts')
        if env.get('PYTHONPATH'):
            pythonpath += os.pathsep + env['PYTHONPATH']
        env.update({
            'PYTHONPATH': pythonpath,
            'COVERAGE_FILE': os.path.join(root_dir, '.coverage'),
            'COVERAGE_PROCESS_START': os.path.join(root_dir, 'setup.cfg'),
        })

        subprocess.run(['coverage', 'erase'], check=True)
        subprocess.run(
            ['coverage', 'run', '-m', 'unittest', 'discover'] +
            (['-v'] if self.verbose != 0 else []) +
            ['-k' + i for i in self.test_suite],
            env=env, check=True
        )
        subprocess.run(['coverage', 'combine'], check=True,
                       stdout=subprocess.DEVNULL)


custom_cmds = {
    'coverage': Coverage,
}

with open(os.path.join(root_dir, 'README.md'), 'r') as f:
    # Read from the file and strip out the badges.
    long_desc = re.sub(r'(^# mike)\n\n(.+\n)*', r'\1', f.read())

setup(
    name='mike',
    version=version,

    description=('Manage multiple versions of your MkDocs-powered ' +
                 'documentation'),
    long_description=long_desc,
    long_description_content_type='text/markdown',
    keywords='mkdocs multiple versions',
    url='https://github.com/jimporter/mike',

    author='Jim Porter',
    author_email='itsjimporter@gmail.com',
    license='BSD-3-Clause',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Documentation',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],

    packages=find_packages(exclude=['test', 'test.*']),
    include_package_data=True,

    install_requires=([
        'jinja2 >= 2.7',
        'pyparsing >= 3.0',
        'verspec',
        'zensical >= 0.0.30',
    ]),
    extras_require={
        'dev': ['coverage', 'flake8 >= 3.0', 'flake8-quotes', 'shtab'],
        'test': ['coverage', 'flake8 >= 3.0', 'flake8-quotes', 'shtab'],
    },

    entry_points={
        'console_scripts': [
            'mike = mike.driver:main',
        ],
    },

    test_suite='test',
    cmdclass=custom_cmds,
    zip_safe=False,
)
