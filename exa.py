import click

def sum(a,b):
    return a+b

def subs(a,b):
    return a-b


@click.group()
def cli1():
    "this is a calculator"

@cli1.command("add")
@click.argument('a',type=float)
@click.argument('b',type=float)
def add_command(a,b):
    click.echo(click.style(str(sum(a,b)),fg="green"))

@cli1.command("substract")
@click.argument('a',type=float)
@click.argument('b',type=float)
def subs_command(a,b):
    click.echo(click.style(str(subs(a,b)),fg="green"))


if __name__=="__main__":
    cli1()