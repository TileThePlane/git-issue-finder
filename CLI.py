import argparse

class CLI():

    @staticmethod
    def show_help(show_section='all'):
        '''
        Show quick usage information and a list of available commands
        :return: print
        '''

        if 'all' == show_section:
            print("Basic usage: Generate a query to retrieve a list of Github Issues.\n")

        if show_section == 'all' or show_section == 'attributes':
            print("Use any of the following commands to set query arguments:")
            print("   [add or delete] *followed by an attribute or flag *followed by a comma seperated list of search terms.")
            print("      The follow attributes are available for issue queries:")
            print("         user\tTo add user search terms.")
            print("         org\tTo add org search terms.")
            print("         lang\tTo add language search terms.")
            print("         label\tTo add label search terms.")
            print("      The following commands to set query flags:")
            print("         is_open\tDefaults to True."   )
            print("         is_archived\tDefaults to False.")
            print("         type\tDefaults to search PRs and issues, but can be set to PR for just PR or issue for just issues.\n")

        if show_section == 'all' or show_section == 'output':
            print("The follow commands can be used for configure output. By default the search result will write to a text file.")
            print("   output\tTo add an output format. Either text or console.\n")

        if show_section == 'all' or show_section == 'status':
            print("The following commands can be used to show status for the current query.")
            print("   show *followed by an argument\tWill give you current search terms for the query.")
            print("      The following arguments can be shown:")
            print("         user")
            print("         org")
            print("         lang")
            print("         label")
            print("         flags\tTo show the flags settings.")
            print("         url\tTo show the query sent to github.com")
            print("         output\tTo show the output settings.\n")
            print("The help command can take an additional argument to show only a particular part of the help guide:")
            print("   attributes\tTo show the available arguments that can be added or removed to query.")
            print("   output\tTo show the available output commands")
            print("   status\t\tTo show status commands.")

    @staticmethod
    def add_attribute(search_issue, attribute_arg, value):
        pass

    @staticmethod
    def delete_attribute(search_issue, attribute_arg, value):
        pass

    @staticmethod
    def set_flag(search_issue, flag, value):
        pass

    @staticmethod
    def set_output(search_issue, output_arg, value):
        pass

    @staticmethod
    def show_status(search_issue, status_arg, value):
        pass

print(CLI().show_help())