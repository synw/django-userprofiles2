from setuptools import setup, find_packages


version = __import__('userprofiles2').__version__

setup(
    name='django-userprofiles2',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='User profiles that work with Django Allauth',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-userprofiles2',
    download_url='https://github.com/synw/django-userprofiles2/releases/tag/' + version,
    keywords=['django', 'user-profiles'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        "django-allauth",
        "django-avatar",
    ],
    zip_safe=False
)
