# Mkdocs plugin: `filename_title`

This plugin for [mkdocs](https://www.mkdocs.org/) changes the page title (e.g. the title in the nav bar) into the filename.


**By default, mkdocs [uses this order to determine the page title](https://github.com/mkdocs/mkdocs/blob/3bada392d2430e31edd55d67b59d60899c22ae11/mkdocs/structure/pages.py#L140):**

1. value passed in from config
2. value of metadata `title`
3. content of the first H1 in Markdown content
4. convert filename to title


**This plugin changes this into:**

1. value of metadata `title`
2. convert filename to title

So basically the filename is always used, except if a `title` metadata is specified in the file, e.g.

```
---
title: Some Title
---
```

The filename gets the following operations applied when converting it into a title:

* the characters `-` (dash) and `_` (underline) get replaced by a space
* if the whole filename is lowercase, it gets capitalized

## Installation

Just execute

```sh
sudo pip3 install .
```

inside the base directory of this repo (`setup.py` will be executed)

## Usage

Say in your `mkdocs.yml` configuration file:

```yaml
plugins:
  - filename_title
  - ...
```

