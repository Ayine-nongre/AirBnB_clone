import cmd
import sys


class TurtleShell(cmd.Cmd):
    intro = "Welcome to my Turtle Shell\n"
    prompt = "Turtle$ "

    def do_hello(self, line):
        print("Welcome To Wylde Turtle Shell")

    def do_help(self, line):
        print("Enter Help or ? to display the list of help options")

    def do_quit(self, line):
        print("Exiting the Turtle Shell, Goodbye")
        return True


if __name__ == '__main__':
    shell = TurtleShell()
    shell.cmdloop()
