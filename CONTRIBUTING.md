# Contributing

Contributions are welcome via pull requests. Please make sure to install git
hooks which enforces certain rules and linting.


## Getting started

Install dependencies & activate virtual env

```shell
poetry install --sync && poetry shell
```

Install git hooks

```shell
pre-commit install --install-hooks --overwrite
```

Run pre-commit hooks against all files

```shell
pre-commit run --all-files
```

Run tests

```shell
pytest tests
```

Install current project from branch

```shell
poetry add git+https://github.com/MousaZeidBaker/poetry-plugin-up.git#branch-name
```


## Commit message

Commit messages **MUST** follow [Conventional
Commits](https://www.conventionalcommits.org/) specification.

```
<type>(<scope>): <description>
  │       │             │
  │       │             └─ Description: Short summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─ Scope: Optional contextual information
  │
  └─ Type: build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test

[optional body]

[optional footer(s)]
```
**Commit type** must be one of following:
- **build**: Changes that affect the build system or external dependencies
- **chore**: Other changes that don't modify src or test files
- **ci**: Changes to our CI configuration files and scripts
- **docs**: Documentation only changes
- **feat**: A new feature
- **fix**: A bug fix
- **perf**: A code change that improves performance
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **revert**: Reverts a previous commit
- **style**: Changes that do not affect the meaning of the code (white-space,
  formatting, missing semi-colons, etc)
- **test**: Adding missing tests or correcting existing tests


### Automated releases

A fully automated release process is implemented using [Release
Please](https://github.com/googleapis/release-please). The **commit type**
determines the next [semantic version](https://semver.org/), see following
examples:

- `fix:` represents a bug fix which correlates with a PATCH bump
- `feat:` represents a new feature which correlates with a MINOR bump
- `feat!:`,  or `fix!:`, `refactor!:`, etc., represents a breaking change
  (indicated by the `!`) which correlates with a MAJOR bump

One can manually set the version number by adding `Release-As: x.y.z` to the
**commit body**, but this should not be needed.


### How to change a commit message?

Amend the most recent commit

```shell
git commit --amend -m "fix: new message"
```

Force push the changes if already pushed to remote

```shell
git push --force-with-lease origin EXAMPLE-BRANCH
```

Amend older or multiple commits with interactive rebase
- use the `git rebase -i HEAD~N` command to display a list of the last `N`
  commits in your default text editor
- replace `pick` with `reword` for each commit message that needs to be changed
- save the changes and close the editor
- for each chosen commit, a new editor will open, change the commit message,
  save the file, and close the editor
- force push the changes, if already pushed to remote, with `git push
  --force-with-lease origin EXAMPLE-BRANCH`
