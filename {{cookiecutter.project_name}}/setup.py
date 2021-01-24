from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

## blabla derived from: https://github.com/pypa/pip/issues/7645#issuecomment-578210649
parsed_reqs = parse_requirements('requirements.txt', session="blabla")
requirements = list(map(lambda ir: str(ir.req), parsed_reqs))

setup(
    name='{{cookiecutter.project_slug}}',
    use_scm_version=True,
    author='{{cookiecutter.author}}',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),  # exclude the tests
    install_requires=requirements,
    setup_requires=['setuptools_scm'],

    extras_require={
        # tests only requirements
        'tests': ['pytest'],
        'dev': ["mypy", "pytest", 'pylint', "twine", 'bumpversion']
    }
)
