# {{ cookiecutter.project_name }}

[![Actions Status][actions-badge]][actions-link]
{%- if cookiecutter.include_pypi | lower == "yes" %}
[![PyPI version][pypi-version]][pypi-link]
{%- endif %}
{%- if cookiecutter.include_rtd | lower == "yes" %}
[![Documentation Status][rtd-badge]][rtd-link]
{%- endif %}

[![Conda-Forge][conda-badge]][conda-link]
[![GitHub Discussion][github-discussions-badge]][github-discussions-link]


<!-- prettier-ignore-start -->
[actions-badge]:            {{cookiecutter.url}}/workflows/CI/badge.svg
[actions-link]:             {{cookiecutter.url}}/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/{{cookiecutter.project_name}}
[conda-link]:               https://github.com/conda-forge/{{cookiecutter.project_name}}-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  {{cookiecutter.url}}/discussions
{%- if cookiecutter.include_pypi | lower == "yes" %}
[pypi-link]:                https://pypi.org/project/{{cookiecutter.project_name}}/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}
[pypi-version]:             https://img.shields.io/pypi/v/{{cookiecutter.project_name}}
{%- endif %}
{%- if cookiecutter.include_rtd | lower == "yes" %}
[rtd-badge]:                https://readthedocs.org/projects/{{cookiecutter.project_name}}/badge/?version=latest
[rtd-link]:                 https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/?badge=latest
{%- endif %}

<!-- prettier-ignore-end -->