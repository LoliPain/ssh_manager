from setuptools import setup

setup(
    name='ssh_manager',
    python_requires='>=3.10',
    version='0.1.1',
    packages=['ssh_manager', 'ssh_manager.stored'],
    install_requires=[
        'simple_term_menu',
    ],
    entry_points={
        'console_scripts':
            [
                'ssh_m = ssh_manager.main:main'
            ]
    },
)
