# Onboarding

## Conventions

### Docstring

Use [Google's format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)

### Bits and pieces

Working in Windows, I find Notepad ++ very good to read JSON files. See: <https://stackoverflow.com/questions/1560464/how-to-reformat-json-in-notepad>

### Inline comments

Try not to. See PEP8, <https://www.python.org/dev/peps/pep-0008/#inline-comments>

## Settings and secrets

Uses the package `python-dotenv`. Sequence:

* you put secrets and/or settings in `.env` file
* you put settings in `settings.py`
* in each file
  * load secrets into the environment with `dotenv`
  * `settings.py` takes variables from the environment
  * import `settings.py` into each file and extract the variables as `settings.<variable>`
