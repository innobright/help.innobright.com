# help.innobright.com Website

This Website is built with [Sphinx](http://sphinx-doc.org/).

When using Sphinx, see their [list of semantic markup](http://www.sphinx-doc.org/en/stable/markup/inline.html?highlight=role#other-semantic-markup) to mark up things like file names, GUI levels, command-line options, etc.

## Dependencies

### Using Fabric deploy script (recommended)

Instructions below are for Ubuntu/Debian. This also works inside Windows Subsystem for Linux (WSL, i.e. Bash for Windows); it probably won't work inside any kind of normal Windows prompt.

The included [Fabric deploy script](http://www.fabfile.org/) will build and deploy the Website for you, provided you have permissions to the server/deploy location.

First, make sure you have fabric installed:

    sudo apt install fabric

Then, inside the directory with fabfile.py, run:

    fab venv

To create a Python virtualenv containing all dependencies. Run:

    fab build

To actually create the Website. You can browse it locally by opening build/index.html in your Web browser, or by going into `build` and running `python3 -m http.server` to create a Web server that will properly serve files locally.

To deploy, use

    fab -u $USER deploy

Where `$USER` is your user on the remote server, e.g. "sjain". This assumes that you have an account on the remote server and SSH is properly setup on it.

If you add a new item to the table of contents hierarchy, you may need to run:

    fab clean

To force Sphinx to rebuild the entire site.

### Without virtualenv

For Ubuntu/Debian, install:

    sudo apt install python3-sphinx python3-sphinx-rtd-theme python3-recommonmark

Inside the top-level folder, type `make` to build the site into the directory `build`.
Deploy `build` to the root of of the Website.
