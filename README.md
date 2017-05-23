# help.innobright.com Website

This Website is built with Sphinx.

## Dependencies

### Using Fabric deploy script (recommended)

Instructions below are for Ubuntu/Debian. This also works inside Windows Scripting Layer (WSL, i.e. Bash for Windows); it probably won't work inside any kind of normal Windows prompt.

The included [Fabric deploy script](http://www.fabfile.org/) will build and deploy the Website for you, provided you have permissions to the server/deploy location.

First, make sure you have fabric installed:

    sudo apt install fabric

Then, inside the directory with fabfile.py, run:

    fab venv

To create a Python virtualenv containing all dependencies. Run:

    fab build

To actually create the Website. You can browse it locally by opening build/index.html in your Web browser.

To deploy, use

    fab -u $USER deploy

Where `$USER` is your user on the remote server, e.g. "sjain". This assumes that you have an account on the remote server and SSH is properly setup on it.

### Without virtualenv

For Ubuntu/Debian, install:

    sudo apt install python3-sphinx python3-sphinx-rtd-theme python3-recommonmark

Inside the top-level folder, type `make` to build the site into the directory `build`.
Deploy `build` to the root of of the Website.
