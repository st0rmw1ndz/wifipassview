import click

import wifipassview.wifipassview as wpv


@click.group()
def cli() -> None:
    pass


@cli.command(name="list", help="List all Wi-Fi profiles on the system.")
def list_command() -> None:
    if profiles := wpv.get_profiles_list():
        for profile in profiles:
            click.echo(f" - {profile}")
    else:
        click.echo("No profiles found.")


@cli.command(name="view", help="View the password for a profile.")
@click.argument("profile", type=str)
def view_command(profile: str) -> None:
    if password := wpv.get_password(profile):
        click.echo(password)
    else:
        click.echo(
            f"No password found for profile '{profile}', does it exist?"
        )


if __name__ == "__main__":
    cli()
