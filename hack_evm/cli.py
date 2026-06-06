"""
Command-line interface for hack-evm.

Provides various commands for attempting to hack EVMs
through the terminal. All commands fail hilariously.
"""

import click

from hack_evm.core import (
    alien_mode,
    bollywood_mode,
    conspiracy,
    explain,
    hack,
    quantum_mode,
    time_machine,
)


@click.group()
@click.version_option(version="0.1.0", prog_name="hack-evm")
def main() -> None:
    """
    🚀 hack-evm - The World's Most Advanced EVM Hacking Toolkit™

    \b
    ⚠️  THIS IS SATIRE. This tool cannot actually hack anything.
    It's designed to fail in increasingly humorous ways.

    \b
    Commands:
      hack          Attempt to hack an EVM (will fail)
      quantum       Activate quantum hacking mode (will also fail)
      explain       Get an explanation for the failure
      conspiracy    Generate conspiracy theories
      alien-mode    Alien technology hacking
      time-machine  Time travel hacking attempt
      bollywood-mode Dramatic Bollywood-style hack sequence
    """
    pass


@main.command()
@click.option(
    "--level",
    "-l",
    type=click.Choice(["basic", "advanced", "expert", "god_mode"], case_sensitive=False),
    default="basic",
    help="Hacking sophistication level",
)
def hack_command(level: str) -> None:
    """
    Attempt to hack an EVM.

    This command initiates a sophisticated hacking sequence
    that will inevitably fail in a creative and amusing way.
    """
    click.echo("")
    hack(level=level)
    click.echo("")


@main.command()
def quantum() -> None:
    """
    Activate quantum hacking mode.

    Leverages quantum mechanics to attempt EVM hacking.
    Schrödinger's cat declines to participate.
    """
    click.echo("")
    quantum_mode()
    click.echo("")


@main.command()
def explain_command() -> None:
    """
    Explain why the last hack attempt failed.

    Provides a detailed, pseudo-technical explanation
    that is entirely made up.
    """
    click.echo("")
    explain()
    click.echo("")


@main.command()
@click.option(
    "--level",
    "-l",
    type=int,
    default=1,
    help="Conspiracy intensity level (1-9000+)",
)
def conspiracy_command(level: int) -> None:
    """
    Generate conspiracy theories about EVMs.

    The higher the level, the more ridiculous the theory.
    It's over 9000!
    """
    if level < 1:
        click.echo(click.style("Error: Conspiracy level must be ≥ 1", fg="red"))
        return

    click.echo("")
    conspiracy(level=level)
    click.echo("")


@main.command()
def alien_mode_command() -> None:
    """
    Activate alien technology for hacking.

    Contacts extraterrestrial hackers who are
    surprisingly unhelpful.
    """
    click.echo("")
    alien_mode()
    click.echo("")


@main.command()
def time_machine_command() -> None:
    """
    Use time travel to hack EVMs.

    Travels through time to hack elections.
    Usually creates paradoxes instead.
    """
    click.echo("")
    time_machine()
    click.echo("")


@main.command()
def bollywood_mode_command() -> None:
    """
    Activate Bollywood-style hacking sequence.

    Complete with dramatic music, unnecessary slow motion,
    and a surprise dance number.
    """
    click.echo("")
    bollywood_mode()
    click.echo("")


if __name__ == "__main__":
    main()
