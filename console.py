#!/usr/bin/python3
"""
pending
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User

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

    def do_create(self, my_input):
        """
        pending
        """
        try:
            my_cmd = shlex.split(my_input)
        except Exception:
            return
        if len(my_cmd) < 1:
            print("** class name missing **")
            return
        try:
            new_item = eval(my_cmd[0] + '()')
            if not isinstance(new_item, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        print(new_item.id)
        storage.new(new_item)
        storage.save()
        return

    def do_show(self, my_input):
        """
        pending
        """
        try:
            my_cmd = shlex.split(my_input)
        except Exception:
            return
        if len(my_cmd) < 1:
            print("** class name missing **")
            return
        try:
            item = eval(my_cmd[0] + '()')
            if not isinstance(item, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        if len(my_cmd) < 2:
            print("** instance id missing **")
            return

        k = my_cmd[0] + '.' + my_cmd[1]
        if k not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[k])
        return

    def do_destroy(self, my_input):
        """
        pending
        """
        try:
            my_cmd = shlex.split(my_input)
        except Exception:
            return
        if len(my_cmd) < 1:
            print("** class name missing **")
            return
        try:
            item = eval(my_cmd[0] + '()')
            if not isinstance(item, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        if len(my_cmd) < 2:
            print("** instance id missing **")
            return
        k = my_cmd[0] + '.' + my_cmd[1]
        if k not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[k]
        storage.save()
        return

    def do_all(self, my_input):
        """
        pending
        """
        try:
            my_cmd = shlex.split(my_input)
        except Exception:
            return
        items = list(storage.all().values())
        if len(my_cmd) < 1:
            print([str(item) for item in items])
            return
        try:
            try_obj = eval(my_cmd[0] + '()')
            if not isinstance(try_obj, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        print([str(item) for item in items
               if my_cmd[0] == item.__class__.__name__])
        return

    def do_update(self, my_input):
        """
        pending
        """
        try:
            my_cmd = shlex.split(my_input)
        except Exception:
            return
        if len(my_cmd) < 1:
            print("** class name missing **")
            return
        try:
            item = eval(my_cmd[0] + '()')
            if not isinstance(item, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        if len(my_cmd) < 2:
            print("** instance id missing **")
            return
        k = my_cmd[0] + '.' + my_cmd[1]
        if k not in storage.all():
            print("** no instance found **")
            return
        if len(my_cmd) < 3:
            print("** attribute name missing **")
            return
        if len(my_cmd) < 4:
            print("** value missing **")
            return
        try:
            my_cmd[3] = int(my_cmd[3])
        except Exception:
            try:
                my_cmd[3] = float(my_cmd[3])
            except Exception:
                pass
        k = my_cmd[0] + '.' + my_cmd[1]
        setattr(storage.all()[k], my_cmd[2], my_cmd[3])
        setattr(storage.all()[k], 'updated_at', datetime.now())
        storage.save()
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
