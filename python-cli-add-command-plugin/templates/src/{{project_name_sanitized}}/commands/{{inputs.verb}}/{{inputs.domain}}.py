import click

@click.command()
@click.argument("{{inputs.argument}}")
@click.pass_context
def {{inputs.domain}}(ctx, {{inputs.argument}}: str):
    """{{inputs.domain_description}}"""
    print("Command {} with argument value {}!".format("{{inputs.domain}}", "{{inputs.argument}}"))
