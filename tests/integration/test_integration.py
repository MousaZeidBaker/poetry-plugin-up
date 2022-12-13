from unittest.mock import Mock

from poetry.core.packages.dependency import Dependency
from poetry.core.packages.package import Package
from pytest_mock import MockerFixture
from tomlkit import parse

from tests.helpers import TestUpCommand


def test_handle_dependency(
    up_cmd_tester: TestUpCommand,
    mocker: MockerFixture,
) -> None:
    dependency = Dependency(
        name="foo",
        constraint="^1.0",
        groups=["main"],
    )
    new_version = "2.0.0"
    package = Package(
        name=dependency.name,
        version=new_version,
    )

    content = parse("")

    selector = Mock()
    selector.find_best_candidate = Mock(return_value=package)
    bump_version_in_pyproject_content = mocker.patch(
        "poetry_plugin_up.command.UpCommand.bump_version_in_pyproject_content",
        return_value=None,
    )

    up_cmd_tester.handle_dependency(
        dependency=dependency,
        latest=False,
        only_packages=[],
        pyproject_content=content,
        selector=selector,
    )

    selector.find_best_candidate.assert_called_once_with(
        package_name=dependency.name,
        target_package_version=dependency.pretty_constraint,
        allow_prereleases=dependency.allows_prereleases(),
        source=dependency.source_name,
    )
    bump_version_in_pyproject_content.assert_called_once_with(
        dependency=dependency,
        new_version=f"^{new_version}",
        pyproject_content=content,
    )


def test_handle_dependency_with_latest(
    up_cmd_tester: TestUpCommand,
    mocker: MockerFixture,
) -> None:
    dependency = Dependency(
        name="foo",
        constraint="^1.0",
        groups=["main"],
    )
    new_version = "2.0.0"
    package = Package(
        name=dependency.name,
        version=new_version,
    )

    content = parse("")

    selector = Mock()
    selector.find_best_candidate = Mock(return_value=package)
    bump_version_in_pyproject_content = mocker.patch(
        "poetry_plugin_up.command.UpCommand.bump_version_in_pyproject_content",
        return_value=None,
    )

    up_cmd_tester.handle_dependency(
        dependency=dependency,
        latest=True,
        only_packages=[],
        pyproject_content=content,
        selector=selector,
    )

    selector.find_best_candidate.assert_called_once_with(
        package_name=dependency.name,
        target_package_version="*",
        allow_prereleases=dependency.allows_prereleases(),
        source=dependency.source_name,
    )
    bump_version_in_pyproject_content.assert_called_once_with(
        dependency=dependency,
        new_version=f"^{new_version}",
        pyproject_content=content,
    )
