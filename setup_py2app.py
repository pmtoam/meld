# -*- coding: utf-8 -*-

#!/usr/bin/env python

import glob
import os
import site
from setuptools import setup
import meld.meldapp
import meld.conf

APP_NAME = 'MeldMerge'
VERSION_STRING = meld.conf.__version__
FORCE_32_BIT = False

PLIST = {
    'CFBundleDocumentTypes': [
        {
            'CFBundleTypeExtensions': ['scmdifftool'],
            'CFBundleTypeIconFile': 'DiffToolDocument',
            'CFBundleTypeName': 'Diff Tool',
            'CFBundleTypeRole': 'Editor',
            'LSTypeIsPackage': True,
        },
    ],
    'LSEnvironment':
    {
        'DYLD_LIBRARY_PATH': 'Contents/Resources/lib:Contents/Frameworks/',
        'LIBRARY_PATH': 'Contents/Resources:/lib:Contents/Frameworks/'
    },
    'CFBundleIdentifier': 'org.gnome.meld',
    'CFBundleShortVersionString': VERSION_STRING,
    'CFBundleSignature': '???',
    'CFBundleVersion': VERSION_STRING,
    'LSPrefersPPC': FORCE_32_BIT,
    'NSHumanReadableCopyright': u'Copyright © 2016',
    'CFBundleDisplayName': 'Meld',
    'CFBundleName': 'Meld',
    'NSHighResolutionCapable': True,
    'LSApplicationCategoryType': 'public.app-category.productivity',
    'LSRequiresNativeExecution': True,
}

#find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

from modulegraph.find_modules import PY_SUFFIXES
PY_SUFFIXES.append('')

setup(
    name='Meld',
    version=meld.conf.__version__,
    description='Visual diff and merge tool',
    author='Kai Willadsen',
    author_email='kai.willadsen@gmail.com',
    url='http://meldmerge.org',
    license='GPLv2+',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Desktop Environment :: Gnome',
        'Topic :: Software Development',
        'Topic :: Software Development :: Version Control',
    ],
    packages=[
        'meld',
        'meld.ui',
        'meld.util',
        'meld.vc',
    ],
    package_data={
        'meld': ['README', 'COPYING', 'NEWS'],
        'meld.vc': ['README', 'COPYING'],
    },
    app=['bin/meld'],
    setup_requires=["py2app"],
    options={'py2app': {
                'includes': '',
                'frameworks':
                'libatk-1.0.0.dylib,'
                'libcairo-gobject.2.dylib,'
                'libcairo-script-interpreter.2.dylib,'
                'libcairo.2.dylib,'
                'libgio-2.0.0.dylib,'
                'libgirepository-1.0.1.dylib,'
                'libglib-2.0.0.dylib,'
                'libgmodule-2.0.0.dylib,'
                'libgobject-2.0.0.dylib,'
                'libgtk-3.0.dylib,'
                'libgtkmacintegration-gtk3.2.dylib,'
                'libgtksourceview-3.0.1.dylib,'
                'libharfbuzz.0.dylib,'
                'libpango-1.0.0.dylib,'
                'libpangocairo-1.0.0.dylib,'
                'libpangoft2-1.0.0.dylib,'
                'librsvg-2.2.dylib,'
                ,
                'argv_emulation': True,
                'iconfile': 'osx/meld.icns',
                'plist': PLIST,
                'prefer_ppc': False,
    }},
    data_files=[
        ('share/man/man1',
         ['meld.1']
         ),
        ('share/doc/meld',
         ['COPYING', 'NEWS']
         ),
        ('share/meld',
         ['data/gschemas.compiled']
         ),
         ('share/meld',
          ['data/org.gnome.meld.gschema.xml']
          ),
        ('share/meld',
         ['data/meld.css']
         ),
        ('share/meld/icons',
         glob.glob("data/icons/*.png") +
         glob.glob("data/icons/COPYING*")
         ),
        ('share/meld/ui',
         glob.glob("data/ui/*.ui") + glob.glob("data/ui/*.xml")
         ),
    ],
)
