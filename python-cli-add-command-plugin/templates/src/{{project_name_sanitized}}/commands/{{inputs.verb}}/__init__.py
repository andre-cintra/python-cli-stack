import click

from {{project_name_sanitized}}.commands.{{inputs.verb}}.{{inputs.domain}} import {{inputs.domain}}

@click.group()
def {{inputs.verb}}():
    """{{inputs.verb_description}}"""
    pass

{{inputs.verb}}.add_command({{inputs.domain}})