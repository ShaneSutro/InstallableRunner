# InstallableRunner
A plug-and-play Vestaboard library handling scheduling and formatting

## Requirements
In order to run, your repository must contain the following:

- [ ] Your repository must be public
- [ ] Your main script entrypoint must be named `__init__.py`
    - [ ] Your script should accept two dictionary objects - one contains all user fields and one contains your dev options in that order. You may use the `(*args, **kwargs)` convention if you'd like.
- [ ] Your workspace must contain a `vbconfig.json` file with your configuration. See options below
- [ ] If your project requires dependencies to run, create and include a virtual environment with the name `venv`. _NOTE: You MUST use `virtualenv` for your virtual environment, as the `venv` module does not create an `activate_this.py` file, which is required to run on a sub process._