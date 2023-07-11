from pathlib import Path

from cleo.testers.application_tester import ApplicationTester
from poetry.core.packages.package import Package
from pytest_mock import MockerFixture
from tomlkit import parse


def test_command(
    app_tester: ApplicationTester,
    packages: list[Package],
    mocker: MockerFixture,
    project_path: Path,
    tmp_pyproject_path: Path,
):
    command_call = mocker.patch(
        "poetry.console.commands.command.Command.call",
        return_value=0,
    )
    mocker.patch(
        "poetry.version.version_selector.VersionSelector.find_best_candidate",
        side_effect=packages,
    )
    mocker.patch(
        "poetry.console.commands.installer_command.InstallerCommand.reset_poetry",  # noqa: E501
        return_value=None,
    )

    path = project_path / "expected_pyproject.toml"
    expected = parse(path.read_text())

    assert app_tester.execute("up") == 0
    assert parse(tmp_pyproject_path.read_text()) == expected
    command_call.assert_called_once_with(name="update")


def test_command_with_latest(
    app_tester: ApplicationTester,
    packages: list[Package],
    mocker: MockerFixture,
    project_path: Path,
    tmp_pyproject_path: Path,
):
    command_call = mocker.patch(
        "poetry.console.commands.command.Command.call",
        return_value=0,
    )
    mocker.patch(
        "poetry.version.version_selector.VersionSelector.find_best_candidate",
        side_effect=packages,
    )
    mocker.patch(
        "poetry.console.commands.installer_command.InstallerCommand.reset_poetry",  # noqa: E501
        return_value=None,
    )

    path = project_path / "expected_pyproject_with_latest.toml"
    expected = parse(path.read_text())

    assert app_tester.execute("up --latest") == 0
    assert parse(tmp_pyproject_path.read_text()) == expected
    command_call.assert_called_once_with(name="update")


def test_command_with_dry_run(
    app_tester: ApplicationTester,
    packages: list[Package],
    mocker: MockerFixture,
    tmp_pyproject_path: Path,
):
    command_call = mocker.patch(
        "poetry.console.commands.command.Command.call",
        return_value=0,
    )
    mocker.patch(
        "poetry.version.version_selector.VersionSelector.find_best_candidate",
        side_effect=packages,
    )
    mocker.patch(
        "poetry.console.commands.installer_command.InstallerCommand.reset_poetry",  # noqa: E501
        return_value=None,
    )

    expected = parse(tmp_pyproject_path.read_text())

    assert app_tester.execute("up --dry-run") == 0
    # assert pyproject.toml file not modified
    assert parse(tmp_pyproject_path.read_text()) == expected
    command_call.assert_not_called()


def test_command_with_no_install(
    app_tester: ApplicationTester,
    packages: list[Package],
    mocker: MockerFixture,
    project_path: Path,
    tmp_pyproject_path: Path,
):
    command_call = mocker.patch(
        "poetry.console.commands.command.Command.call",
        return_value=0,
    )
    mocker.patch(
        "poetry.version.version_selector.VersionSelector.find_best_candidate",
        side_effect=packages,
    )
    mocker.patch(
        "poetry.console.commands.installer_command.InstallerCommand.reset_poetry",  # noqa: E501
        return_value=None,
    )

    path = project_path / "expected_pyproject.toml"
    expected = parse(path.read_text())

    assert app_tester.execute("up --no-install") == 0
    assert parse(tmp_pyproject_path.read_text()) == expected
    command_call.assert_called_once_with(name="lock", args="--no-update")


def test_command_reverts_pyproject_on_error(
    app_tester: ApplicationTester,
    packages: list[Package],
    mocker: MockerFixture,
    tmp_pyproject_path: Path,
):
    command_call = mocker.patch(
        "poetry.console.commands.command.Command.call",
        side_effect=Exception,
    )
    mocker.patch(
        "poetry.version.version_selector.VersionSelector.find_best_candidate",
        side_effect=packages,
    )
    mocker.patch(
        "poetry.console.commands.installer_command.InstallerCommand.reset_poetry",  # noqa: E501
        return_value=None,
    )

    expected = parse(tmp_pyproject_path.read_text())

    assert app_tester.execute("up") == 1
    assert parse(tmp_pyproject_path.read_text()) == expected
    command_call.assert_called_once_with(name="update")


def test_pinned_without_latest_fails(app_tester: ApplicationTester):
    assert app_tester.execute("up --pinned") == 1
