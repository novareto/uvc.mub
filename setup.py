from setuptools import setup, find_packages
import os

version = '1.0'


crom_requires = [
    'cromlech.security',
    ]


zope_requires = [
    'zope.security',
    ]


setup(name='uvc.mub',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['uvc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.component',
          'zope.security',
      ],
      extras_require={
          'crom': crom_requires,
          'zope': zope_requires,
          },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
