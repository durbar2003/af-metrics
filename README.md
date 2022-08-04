# af-metrics

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Gitter][gitter-badge]][gitter-link]


<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/durbar2003/af-metrics/workflows/CI/badge.svg
[actions-link]:             https://github.com/durbar2003/af-metrics/actions
[black-badge]:              https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]:               https://github.com/psf/black
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/af-metrics
[conda-link]:               https://github.com/conda-forge/af-metrics-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/durbar2003/af-metrics/discussions
[gitter-badge]:             https://badges.gitter.im/https://github.com/durbar2003/af-metrics/community.svg
[gitter-link]:              https://gitter.im/https://github.com/durbar2003/af-metrics/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[pypi-link]:                https://pypi.org/project/af-metrics/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/af-metrics
[pypi-version]:             https://badge.fury.io/py/af-metrics.svg
[rtd-badge]:                https://readthedocs.org/projects/af-metrics/badge/?version=latest
[rtd-link]:                 https://af-metrics.readthedocs.io/en/latest/?badge=latest
[sk-badge]:                 https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg
<!-- prettier-ignore-end -->

 Python package for monitoring the Coffea-Casa Analysis Facility using Prometheus Monitoring tool and generating dashboards from the collected metrics using Grafana. The package deploys Prometheus locally on localhost:8003 and establishes a connection between Prometheus and the JSON Data collected from the specific Jupyter Notebook to be monitored in the Coffea-Casa Analysis Facility using the Prometheus Client Package. This JSON data serves as the custom metrics for the Prometheus server. These Prometheus metrics serve as the data for generating convenient dashboards using the Grafana tool. 

 The current infrastructure can be represented as:

 ![Infrastructure Diagram](assets\infrastructure.png?raw=true "Title")