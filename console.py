#!/usr/bin/python3
"""
pending
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """pending"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        ctrl+d (event)
        """
        print('')
        return True

    def do_quit(self, line):
        """
        quit (event)
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
