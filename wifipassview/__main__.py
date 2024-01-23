import click

import wifipassview.wifipassview as wpv
from wifipassview import __version__


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__)
def cli() -> None:
    """Utility to view Wi-Fi profiles and their passwords.

    Copyright (c) 2024 frosty.
    """
    pass


@cli.command(name="list")
def list_command() -> None:
    """List all Wi-Fi profiles on the system."""

    if profiles := wpv.get_profiles_list():
        for profile in profiles:
            click.echo(f" - {profile}")
    else:
        click.echo("No profiles found.")


@cli.command(name="view")
@click.argument("profile", type=str)
def view_command(profile: str) -> None:
    """View the password for a profile."""

    if password := wpv.get_password(profile):
        click.echo(password)
    else:
        click.echo(
            f"No password found for profile '{profile}', does it exist?"
        )


if __name__ == "__main__":
    cli()
