#!/usr/bin/python3
"""
Console module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def do_EOF(self, my_input):
        """
        ctrl+d (event)
        """
        print('')
        return True

    def emptyline(self):
        """
        manage empty line
        """
        pass

    def do_quit(self, my_input):
        """
        quit (event)
        """
        return True

    def do_create(self, my_input):
        """
        create <class> | create a object 
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
        show <class> <id> | show an specific object
        <class name>.show(<id>) |show an specific object
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
        destroy <class> <id> | destroy an specific object
        <class name>.destroy(<id>) | destroy an specific object
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
        all |show all objects
        all <class> |show all objects by class
        <class name>.all() | show all objects by class
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
        update <class> <attr_name> <new_value> | update an object with the new values
        <class name>.update(<id>, <attribute name>, <attribute value>) | update an object with the new values
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

    def precmd(self, my_input):
        """Precommand method"""
        try:
            tmp1 = my_input.split('.')
            try:
                item = eval(tmp1[0] + '()')
                if not isinstance(item, BaseModel):
                    raise Exception
            except Exception:
                return my_input
            my_class = tmp1[0]
            tmp2 = tmp1[1].split('(')
            my_cmd = tmp2[0]
            my_args = tmp2[1][:-1]
            list_args = my_args.split(',')
            new_cmd = ' '.join(list_args)
            return " ".join([my_cmd, my_class, new_cmd])
        except Exception:
            return my_input

    def do_count(self, my_input):
        """<class name>.count() | a counter of specific class"""
        try:
            my_cmd = shlex.split(my_input)
        except Exception:
            return
        c = 0
        for k, item in storage.all().items():
            if item.__class__.__name__ == str(my_cmd[0]):
                c += 1
        print(c)
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
