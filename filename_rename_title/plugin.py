from mkdocs.plugins import BasePlugin
import re


class FilenameRenameTitlePlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, site_navigation=None, **kwargs):
        """
        The page_markdown event is called after the page's markdown is loaded from
        file and can be used to alter the Markdown source text.
        The meta- data has been stripped off and is available as page.meta at this point.
        """
        if 'title' in page.meta:
            return markdown
        if page.is_homepage:
            return markdown
        page.title = re.sub('^[0-9]{1,2}_','',page.file.name).replace('-', ' ').replace('_', ' ')
        # Capitalize if the filename was all lowercase, otherwise leave it as-is.
        if page.title.lower() == page.title:
            page.title = page.title.capitalize()
        return markdown
