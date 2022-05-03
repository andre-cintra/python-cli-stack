from click.testing import CliRunner
from {{project_name_sanitized}}.cli import cli

def test_say_hello():
    runner = CliRunner()
    result = runner.invoke(cli, ["{{inputs.verb}}", "{{inputs.domain}}", "stacker"])
    
    assert result.exit_code == 0
    assert result.output == "Command {{inputs.verb}} with argument value stacker!\n"