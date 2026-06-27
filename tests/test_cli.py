"""
Tests for the CLI interface.

Tests all CLI commands to ensure they execute without errors
and produce expected output.
"""

import pytest
from click.testing import CliRunner

from hack_evm.cli import main


@pytest.fixture
def runner() -> CliRunner:
    """Create a Click CLI runner for testing."""
    return CliRunner()


class TestCLIBasicCommands:
    """Test basic CLI commands."""

    def test_main_no_args(self, runner: CliRunner) -> None:
        """Test that main with no args shows help."""
        result = runner.invoke(main)
        assert result.exit_code in (0, 2)
        assert "hack-evm" in result.output
        assert "SATIRE" in result.output.upper()

    def test_help_flag(self, runner: CliRunner) -> None:
        """Test --help flag."""
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "SATIRE" in result.output.upper()
        assert "hack" in result.output.lower()

    def test_version_flag(self, runner: CliRunner) -> None:
        """Test --version flag."""
        result = runner.invoke(main, ["--version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.output


class TestHackCommand:
    """Test the hack CLI command."""

    def test_hack_basic(self, runner: CliRunner) -> None:
        """Test basic hack command."""
        result = runner.invoke(main, ["hack"])
        assert result.exit_code == 0
        assert "FAILED" in result.output
        assert "HACK-EVM" in result.output

    def test_hack_expert(self, runner: CliRunner) -> None:
        """Test hack with expert level."""
        result = runner.invoke(main, ["hack", "--level", "expert"])
        assert result.exit_code == 0
        assert "FAILED" in result.output

    def test_hack_god_mode(self, runner: CliRunner) -> None:
        """Test hack with god_mode."""
        result = runner.invoke(main, ["hack", "--level", "god_mode"])
        assert result.exit_code == 0
        assert "GOD MODE" in result.output

    def test_hack_invalid_level(self, runner: CliRunner) -> None:
        """Test hack with invalid level fails gracefully."""
        result = runner.invoke(main, ["hack", "--level", "impossible"])
        assert result.exit_code != 0


class TestQuantumCommand:
    """Test quantum command."""

    def test_quantum(self, runner: CliRunner) -> None:
        """Test quantum command runs."""
        result = runner.invoke(main, ["quantum"])
        assert result.exit_code == 0
        assert "QUANTUM" in result.output


class TestExplainCommand:
    """Test explain command."""

    def test_explain(self, runner: CliRunner) -> None:
        """Test explain command runs."""
        result = runner.invoke(main, ["explain"])
        assert result.exit_code == 0
        assert "went wrong" in result.output


class TestConspiracyCommand:
    """Test conspiracy command."""

    def test_conspiracy_basic(self, runner: CliRunner) -> None:
        """Test conspiracy command with default level."""
        result = runner.invoke(main, ["conspiracy"])
        assert result.exit_code == 0
        assert "CONSPIRACY" in result.output

    def test_conspiracy_custom_level(self, runner: CliRunner) -> None:
        """Test conspiracy command with custom level."""
        result = runner.invoke(main, ["conspiracy", "--level", "42"])
        assert result.exit_code == 0
        assert "Level 42" in result.output

    def test_conspiracy_invalid_level(self, runner: CliRunner) -> None:
        """Test conspiracy with invalid level."""
        result = runner.invoke(main, ["conspiracy", "--level", "0"])
        assert result.exit_code == 0
        assert "Error" in result.output


class TestEasterEggCommands:
    """Test easter egg commands."""

    def test_alien_mode(self, runner: CliRunner) -> None:
        """Test alien-mode command."""
        result = runner.invoke(main, ["alien-mode"])
        assert result.exit_code == 0
        assert "ALIEN" in result.output

    def test_time_machine(self, runner: CliRunner) -> None:
        """Test time-machine command."""
        result = runner.invoke(main, ["time-machine"])
        assert result.exit_code == 0
        assert "TIME MACHINE" in result.output

    def test_bollywood_mode(self, runner: CliRunner) -> None:
        """Test bollywood-mode command."""
        result = runner.invoke(main, ["bollywood-mode"])
        assert result.exit_code == 0
        assert "BOLLYWOOD" in result.output


class TestOutputFormatting:
    """Test that output contains expected formatting."""

    def test_hack_output_has_steps(self, runner: CliRunner) -> None:
        """Test hack output shows steps."""
        result = runner.invoke(main, ["hack"])
        assert "[*]" in result.output

    def test_hack_output_shows_failure(self, runner: CliRunner) -> None:
        """Test hack output shows failure message."""
        result = runner.invoke(main, ["hack"])
        assert "FAILED" in result.output or "failed" in result.output.lower()

    def test_all_commands_dont_crash(self, runner: CliRunner) -> None:
        """Test all commands execute without exceptions."""
        commands = [
            "hack",
            "quantum",
            "explain",
            "conspiracy",
            "alien-mode",
            "time-machine",
            "bollywood-mode",
        ]
        for cmd in commands:
            result = runner.invoke(main, [cmd])
            assert result.exit_code == 0, f"Command '{cmd}' failed with: {result.exception}"
