from distutils.core import setup

setup(
    name='kala',
    version='0.3',
    url='https://github.com/bgroff/kala-app',
    author='Bryce Groff',
    author_email='bgroff@hawaii.edu',
    description='Project Management in Django.',
    license='BSD',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
    ],
    packages=['django_kala', 'api', 'auth', 'documents', 'projects', 'organizations']
)
