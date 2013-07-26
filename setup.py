from setuptools import setup, find_packages

install_requires = []

setup(
    name='IL2ServerConnector',
    version='0.0.1',
    description='High-level access to IL-2 FB Dedicated Server.',
    long_description=open('README.md').read(),
    license='MIT',
    url='https://github.com/IL2HorusTeam/server-connector',
    bugtrack_url='https://github.com/IL2HorusTeam/server-connector/issues',
    author='Alexander Oblovatniy',
    author_email='oblovatniy@gmail.com',
    packages=find_packages(),
    test_suite='il2_server_connector.tests',
    scripts=[],
    install_requires=install_requires,
)
