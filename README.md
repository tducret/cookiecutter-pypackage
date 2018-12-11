# Cookiecutter PyPackage (updated)

**Cookiecutter** template for a Python package.

Forked from [audreyr repo](https://github.com/audreyr/cookiecutter-pypackage/)

## Requirements

- Cookiecutter : `pip3 install -U cookiecutter`
- Travis CLI : [Installation](https://github.com/travis-ci/travis.rb#installation)
- Pytest : `pip3 install -U pytest`
- Pytest coverage : `pip3 install -U pytest-cov`

## Steps

- Create a repo on [Github](https://github.com/new) with a desired [REPOSITORY] name (ex : `myproject-python`)
- Fill the short description on Github and copy it for the following steps
- Execute in the terminal `git clone https://github.com/tducret/[REPOSITORY].git`
- Execute the cookiecutter with `cookiecutter -f https://github.com/tducret/cookiecutter-pypackage.git` (`-f` is to overwrite the contents of the output directory if it already exists)
- `cd [REPOSITORY]`
- Update requirements.txt (if needed)
- Update README.md
- Add keywords in `setup.py` and check if everything is okay
- Remove *_cli.py if the project doesn't need a CLI tool
- When everything is in place, add the files to git, commit it and push it : `git add .; git commit -am "First commit"; git push`
- Add topics (keywords) related to the project on Github (finding your project will be easier)
- Add the repo to your [Travis-CI account](https://travis-ci.org/profile/tducret) (Click on the `Sync` button if the repo doesn't appear)
- Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
- Add the repo to your [Coveralls account](https://coveralls.io/repos/new) (Click on the `Sync repos` button if the repo doesn't appear)
- Release your package by pushing a new tag to master
