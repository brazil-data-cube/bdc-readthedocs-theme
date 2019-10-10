"""Sphinx Brazil Data Cube theme."""

import os
import xml.etree.ElementTree as ET


def setup(app):
    """Configures BDC Templates"""
    app.connect('html-page-context', add_html_link)
    app.connect('build-finished', create_sitemap)
    app.sitemap_links = []


def add_html_link(app, pagename, templatename, context, doctree):
    """Collects page name and register into site map link"""
    base_url = app.config['html_theme_options'].get('base_url', '')
    if base_url:
        app.sitemap_links.append(base_url + pagename + ".html")


def create_sitemap(app, exception):
    """Generates the sitemap.xml from cached sitemap links"""
    if (
            not app.config['html_theme_options'].get('base_url', '') or
            exception is not None or
            not app.sitemap_links
        ):
        return

    filename = app.outdir + "/sitemap.xml"
    print("Generating sitemap.xml in %s" % filename)

    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for link in app.sitemap_links:
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "loc").text = link

    ET.ElementTree(root).write(filename)


def html_theme_path():
    return [os.path.dirname(os.path.abspath(__file__))]