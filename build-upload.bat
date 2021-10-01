@echo off
redir dist /S /Q
py -m build
py -m twine upload --repository pypi dist/*