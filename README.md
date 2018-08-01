# Cookiecutter PyPackage (updated)

**Cookiecutter** template for a Python package.

Forked from [audreyr repo](https://github.com/audreyr/cookiecutter-pypackage/)

## Requirements

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher) :

```bash
pip install -U cookiecutter
```

## Steps

- Create a repo on [Github](https://github.com/new) with the name of the folder you just created > [REPOSITORY]
- *Copy the short description for the following steps*
- Execute in the terminal `git clone https://github.com/tducret/[REPOSITORY].git`
- Execute the cookiecutter with `cookiecutter https://github.com/tducret/cookiecutter-pypackage.git`
- Add keywords related to the project on Github (finding the project is easier)
- Add the same keywords in setup.py and check if everything is okay
- cd [REPOSITORY]
- Update requirements.txt (if needed)
- Update README.md
- Remove *_cli.py if the project doesn't need a CLI tool
- Add the repo to your [Travis-CI account](https://travis-ci.org/profile/tducret)
- Add the repo to your [Coveralls account](https://coveralls.io/repos/new)
- Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
- When everything is in place, add the files to git : ```git add .```
- commit it and push it
- Release your package by pushing a new tag to master