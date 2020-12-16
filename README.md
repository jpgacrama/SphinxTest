# Sphinx

Installation Instructions:

1. Install latest version of Python and Sphinx.

    - For windows, see: https://www.sphinx-doc.org/en/1.6/install.html#windows-install-python-and-sphinx

2. Install the latest GNU Make for your Operating System
3. Install the latest JDK

4. Make sure that the path of Python is available in your system's PATH variable
5. Open command line as ADMINISTRATOR
6. Type the following commands to install additional extensions:

    - pip install sphinxcontrib-plantuml
    - pip install sphinx_rtd_theme

To Generate Documentation:

1. Open windows command prompt and run it as administrator.
2. Go to the Documentation folder by typing cd "Path to Documentation folder"
3. Type make clean

    - This removes the previously-generated documentation

4. Type make html

    - This generates your documentation from *.rst files inside the src folder

5. View your results in "_build\html\index.html"
