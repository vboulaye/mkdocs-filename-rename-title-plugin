#!/usr/bin/env python
# coding: utf-8

import setuptools

setuptools.setup(
    name="mkdocs-filename-title-plugin",
    version='0.1',
    install_requires=['mkdocs>=1.0.4'],
    packages=["filename_title"],
    entry_points={
        'mkdocs.plugins': [
            'filename_title = filename_title.plugin:FilenameTitlePlugin',
        ]
    }
)
