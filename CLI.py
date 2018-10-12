import argparse
import click

class CLI():

    @click.group()
    def main():
        pass

    @main.command()
    @click.argument('help')
    def show_help(help='all'):
        '''
        Show quick usage information and a list of available commands
        :return: print
        '''

        if 'all' == help:
            click.echo("Basic usage: Generate a query to retrieve a list of Github Issues.\n")

        if help in ['all', 'attributes']:
            click.echo("Use any of the following commands to set query arguments:")
            click.echo("   [add or delete or flag] *followed by an attribute or flag *followed by a comma seperated list of search terms.")
            click.echo("      The follow attributes are available for issue queries:")
            click.echo("         user\tTo add user search terms.")
            click.echo("         org\tTo add org search terms.")
            click.echo("         lang\tTo add language search terms.")
            click.echo("         label\tTo add label search terms.")
            click.echo("      The following commands to set query flags:")
            click.echo("         is_open\tDefaults to True."   )
            click.echo("         is_archived\tDefaults to False.")
            click.echo("         type\tDefaults to search PRs and issues, but can be set to PR for just PR or issue for just issues.\n")

        if help in ['all','output']:
            click.echo("The follow commands can be used for configure output. By default the search result will write to a text file.")
            click.echo("   output\tTo add an output format. Either text or console.\n")

        if help in ['all','status']:
            click.echo("The following commands can be used to show status for the current query.")
            click.echo("   show *followed by an argument\tWill give you current search terms for the query.")
            click.echo("      The following arguments can be shown:")
            click.echo("         user")
            click.echo("         org")
            click.echo("         lang")
            click.echo("         label")
            click.echo("         flags\tTo show the flags settings.")
            click.echo("         url\tTo show the query sent to github.com")
            click.echo("         output\tTo show the output settings.\n")
            click.echo("The help command can take an additional argument to show only a particular part of the help guide:")
            click.echo("   attributes\tTo show the available arguments that can be added or removed to query.")
            click.echo("   output\tTo show the available output commands")
            click.echo("   status\t\tTo show status commands.")

        return ''

    @main.command()
    @click.argument('add')
    def add_attribute(search_issue, add):
        pass

    @main.command()
    @click.argument('delete')
    def delete_attribute(search_issue, delete):
        pass

    @main.command()
    @click.argument('flag')
    def set_flag(search_issue, flag):
        pass

    @main.command()
    @click.argument('output')
    def set_output(search_issue, output):
        pass

    @main.command()
    @click.argument('status')
    def show_status(search_issue, status):
        pass

print(CLI().main())