# Poetry Plugin: up

![release](https://github.com/MousaZeidBaker/poetry-plugin-up/actions/workflows/release.yaml/badge.svg)
![test](https://github.com/MousaZeidBaker/poetry-plugin-up/actions/workflows/test.yaml/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
![python_version](https://img.shields.io/badge/Python-%3E=3.8-blue)
![poetry_version](https://img.shields.io/badge/Poetry-%3E=1.6-blue)
[![pypi_v](https://img.shields.io/pypi/v/poetry-plugin-up)](https://pypi.org/project/poetry-plugin-up)
[![pypi_dm](https://img.shields.io/pypi/dm/poetry-plugin-up)](https://pypi.org/project/poetry-plugin-up)

This package is a plugin that updates dependencies and bumps their versions in
`pyproject.toml` file. The version constraints are respected, unless the
`--latest` flag is passed, in which case dependencies are updated to latest
available compatible versions.

This plugin provides similar features as the existing `update` command with
additional features.


## Installation

The easiest way to install the `up` plugin is via the `self add` command of
Poetry.

```shell
poetry self add poetry-plugin-up
```

If you used `pipx` to install Poetry you can add the plugin via the `pipx
inject` command.

```shell
pipx inject poetry poetry-plugin-up
```

Otherwise, if you used `pip` to install Poetry you can add the plugin packages
via the `pip install` command.

```shell
pip install poetry-plugin-up
```


## Usage

The plugin provides an `up` command to update dependencies

```shell
poetry up --help
```

Update dependencies

```shell
poetry up
```

Update dependencies to latest available compatible versions

```shell
poetry up --latest
```

Update the `foo` and `bar` packages

```shell
poetry up foo bar
```

Update packages only in the `main` group

```shell
poetry up --only main
```

Update packages but ignore the `dev` group

```shell
poetry up --without dev
```


## Contributing

Contributions are welcome! See the [Contributing Guide](https://github.com/MousaZeidBaker/poetry-plugin-up/blob/master/CONTRIBUTING.md).


## Issues

If you encounter any problems, please file an
[issue](https://github.com/MousaZeidBaker/poetry-plugin-up/issues) along with a
detailed description.
