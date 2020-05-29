import click
import six
from pyfiglet import figlet_format

from . import __version__, harden, prometheus

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


def log(string, color, font="block", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)

@click.command()
@click.version_option(version=__version__)
def main():
    """The Brick CLI Python project."""
    log("Brick CLI", color="red", figlet=True)
    log("Welcome to Brick CLI", "green")
    click.echo("Hello, world!")
    # harden.install_deps()
    prometheus.configure_node_exporter()