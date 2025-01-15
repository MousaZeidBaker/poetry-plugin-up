# Changelog

## [0.9.0](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/v0.8.0...v0.9.0) (2025-01-15)


### Features

* Add support for poetry 2 ([0e085e0](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/0e085e0d94c6251182056d8a42b958c05d9f2586))


### Bug Fixes

* Path.write_text does not have newline kwarg in 3.9 ([7b7955a](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/7b7955a9466df664a65b8829837c0abd1e2b69b5))

## [0.8.0](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/v0.7.3...v0.8.0) (2024-11-27)


### Features

* BREAKING: zero based caret dependencies will be updated by default, an option
  to opt-out can be used
  ([a1527e8](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/a1527e87a0daf121ca7d7fc7a5694504f17aabb8))


### Bug Fixes

* conflict ([bd56433](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/bd56433011d1b72d61afde1edce17b36208ca51f))
* linting errors ([65227c8](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/65227c838e2ba99a5da506bd637ada24bfb98218))


### Reverts

* add option to include zero based carets dependencies ([f171c51](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/f171c51baba1009964eaeb23fb0c26b414c8a8fa))

## [0.7.3](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/v0.7.2...v0.7.3) (2024-08-09)


### Bug Fixes

* fix no-install lock file updates ([40feadf](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/40feadf7fdae8400db7e41840a231f5bdb4def95))

## [0.7.2](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.7.1...v0.7.2) (2024-07-10)


### Documentation

* update README ([c2f3f1e](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/c2f3f1eb00b923b653827a18f0cc82d37308162e))

## [0.7.1](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.7.0...0.7.1) (2023-11-06)


### 🐛 Bug Fixes

* don't install LICENSE in the Python path ([63090ca](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/63090cad7c8eac39ea4df392843e9691d47f97a0))
* tests ([8caf803](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/8caf803570688ce71a70666512b802427d8b6072))

## [0.7.0](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.6.0...0.7.0) (2023-10-19)


### 🚀 Features

* add --preserve-wildcard ([ca9fcdf](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/ca9fcdf201e7c219e4cd872e004128dceaf0a71a))

## [0.6.0](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.5.0...0.6.0) (2023-10-09)


### 🚀 Features

* drop support for python 3.7 ([8e70a5d](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/8e70a5d9a2fa49309e863e1a18e0e4bd45c24a10))


### 🐛 Bug Fixes

* update README ([7e51a63](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/7e51a6335cb8038a4d148893ef0b1ebe63376e9c))

## [0.5.0](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.4.0...0.5.0) (2023-10-09)


### 🚀 Features

* Add new option --exclude ([c6bd601](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/c6bd601fc85410e06c12b98651d2037a97c15fae))


### 🐛 Bug Fixes

* rename method argument ([ff59b3d](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/ff59b3dcd2f7c53b093a2a5ce6d05b79f0ad006a))

## [0.4.0](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.3.0...0.4.0) (2023-08-30)


### 🚀 Features

* Preserve zero based caret ([8a5d3cb](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/8a5d3cb6a4f122537e7e66faf52c1672d8773abc))

## [0.3.0](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.2.2...0.3.0) (2023-02-13)


### 🚀 Features

* Preserve tilde when bumping ([b346042](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/b34604275a937faeb2a4b25b765429ecbaabef4d))

## [0.2.2](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.2.1...0.2.2) (2023-02-10)


### 🐛 Bug Fixes

* get rid of flake8 additional packages ([7ffdd5a](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/7ffdd5ab33b80248875c845ae5b41aa9addfef82))
* support `==` as pinned ([4f6d119](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/4f6d1191cef19d22e47ae2571c3e788b331c5901))
* throw error on pinned without latest ([95aaeac](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/95aaeaca0a7d3638916da8bb3048c1dd2a1cabd5))

## [0.2.1](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.2.0...0.2.1) (2022-12-19)


### 🐛 Bug Fixes

* revert pyproject.toml changes on error ([0e6c388](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/0e6c388b375b05f3121c4c1fa756aa10e4f9d5fe))

## [0.2.0](https://github.com/MousaZeidBaker/poetry-plugin-up/compare/0.1.0...0.2.0) (2022-12-13)


### 🚀 Features

* add pinned option to include pinned dependencies ([7ff01f9](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/7ff01f9eb7e48e27ed5d386e617d029b385b22e4))

## 0.1.0 (2022-12-13)


### 🚀 Features

* initial commit ([0a48f00](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/0a48f00b67d86e3772693825937ea2af76ede8fa))


### 📝 Documentation

* add test badge ([152015b](https://github.com/MousaZeidBaker/poetry-plugin-up/commit/152015bb7d0e4dc16fc147060bec4d40996e1ebf))
