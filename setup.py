from setuptools import setup, find_packages


version = __import__('userprofiles').__version__

setup(
    name='django-userprofiles',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='User profiles that work with Django Allauth',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-userprofiles',
    download_url='https://github.com/synw/django-userprofiles/releases/tag/' + version,
    keywords=['django', 'user-profiles'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        "django-allauth",
        "django-avatar",
        "django-bootstrap3",
        "django-bootstrap-form",
        "django-braces",
    ],
    zip_safe=False
)
