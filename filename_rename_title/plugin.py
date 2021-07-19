from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Navigation as MkDocsNavigation, Section
import re
from mkdocs.structure.files import Files, File
from mkdocs.config import config_options, Config
from mkdocs.structure.pages import Page


class FilenameRenameTitlePlugin(BasePlugin):
    def on_nav(self, nav: MkDocsNavigation, config: Config, files: Files):
        print(str(nav))
        #if isinstance(nav, Section):
        for item in nav.items:
            self.process_item_title(item)
        return nav

    def process_item_title(self, nav: MkDocsNavigation):
        if isinstance(nav, Page):
            if nav.title is None and 'title' not in nav.meta:
                nav.title = self.format_title(nav.file.name)
        if isinstance(nav, Section):
            print(nav.title)
            nav.title = self.format_title(nav.title)
            print(nav.title)
        if isinstance(nav, Section):
            for item in nav.children:
                self.process_item_title(item)
        return nav

    # def on_page_markdown(self, markdown, page, config, site_navigation=None, **kwargs):
    #     """
    #     The page_markdown event is called after the page's markdown is loaded from
    #     file and can be used to alter the Markdown source text.
    #     The meta- data has been stripped off and is available as page.meta at this point.
    #     """
    #     if 'title' in page.meta:
    #         return markdown
    #     if page.is_homepage:
    #         return markdown
    #     page.title = re.sub('^[0-9]{1,2}_','',page.file.name).replace('-', ' ').replace('_', ' ')
    #     # Capitalize if the filename was all lowercase, otherwise leave it as-is.
    #     if page.title.lower() == page.title:
    #         page.title = page.title.capitalize()
    #     return markdown

    def format_title(self, title):
        title = re.sub('^[0-9]{1,2}[ _]', '', title).replace('-', ' ').replace('_', ' ')
        # Capitalize if the filename was all lowercase, otherwise leave it as-is.
        if title.lower() == title:
            title = title.capitalize()
        return title
