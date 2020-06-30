import setuptools

setuptools.setup(
    name='django-postgres-createdb',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
