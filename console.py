#!/usr/bin/python3
"""This is a console app for the models created"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """This is tje class that contains the logic for the console"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """This exits the command line"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_create(self, model):
        """
        This command is used to create an object model
        Usage: create <class name>"""
        if not model:
            print("** class name missing **")
        elif model != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            print(new_model.id)

    def do_show(self, args):
        """
        This command prints the string representation of an object model
        Usage: show <class name> <id>"""

        data = storage.all()
        model = args.split(" ")

        if not model[0]:
            print("** class name missing **")
        elif model[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(model) != 2:
            print("** instance id missing **")
        else:
            for key, value in data.items():
                if model[1] == value.id:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """
        This command destroys an object model
        Usage: destroy <class name> <id>"""

        data = storage.all()
        model = args.split(" ")

        if not model[0]:
            print("** class name missing **")
        elif model[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(model) != 2:
            print("** instance id missing **")
        else:
            for key, value in data.items():
                if model[1] == value.id:
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, model):
        """
        This command prints all object model of a type
        Usage: all
               all <class name>"""

        data = storage.all()
        obj = []

        if not model:
            for key, value in data.items():
                obj.append(value.__str__())
            print(obj)
        else:
            for key, value in data.items():
                args = key.split('.')
                if args[0] == model:
                    obj.append(value.__str__())
            if len(obj) == 0:
                print("** class doesn't exist **")
                return
            print(obj)

    def do_update(self, args):
        """
        This command updates a field in the object module
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        data = storage.all()
        models = ["BaseModel"]

        model = args.split()
        if len(model) == 0:
            print("** class name missing **")
        elif model[0] not in models:
            print("** class doesn't exist **")
        elif len(model) == 1:
            print("** instance id missing **")
        elif len(model) == 2:
            print("** attribute name missing **")
        elif len(model) == 3:
            print("** value missing **")
        else:
            for key, value in data.items():
                tag = key.split('.')
                if model[0] == tag[0]:
                    if model[1] == value.id:
                        print(value)
                        return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
