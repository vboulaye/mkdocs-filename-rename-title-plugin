#!/usr/bin/env python
# coding: utf-8

import setuptools

setuptools.setup(
    name="mkdocs-filename-rename-title-plugin",
    version='0.1',
    install_requires=['mkdocs>=1.0.4'],
    packages=["filename_rename_title"],
    entry_points={
        'mkdocs.plugins': [
            'filename_rename_title = filename_rename_title.plugin:FilenameRenameTitlePlugin',
        ]
    }
)
