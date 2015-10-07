from setuptools import find_packages, setup

setup(
    name='TelegramLogHandler',
    version='1.0.2',
    url='https://github.com/simonacca/TelegramLogHandler',
    author='Simone Accascina',
    author_email='simon@accascina.me',
    description='A log handler that sends log messages via a Telegram bot.',
    keywords='telegram log handler bot',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
