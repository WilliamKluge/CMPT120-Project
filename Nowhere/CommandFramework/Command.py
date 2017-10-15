# Holds the Command class
# Author: William Kluge
# Date: 2017-10-13


class Command:
    """
    Defines what a command will do, what the user needs to enter to activate it, and the help string to describe it
    """

    def __init__(self, key, system, help_string):
        """
        Initializes the command class with its core data
        :param key: Key the user needs to enter to activate this command
        :param system: System this command uses to impact the game world
        :param help_string: String to show the user if they need help with this command
        """
        self.key = key
        self.system = system
        self.help_string = help_string
        self.target = None  # This is the entity that this command will target (if the command targets an entity)
        self.using = None  # This is the entity that this command will use (if this command uses an entity)

    def set_target(self, target):
        """
        Sets the entity for this command to target
        :param target: Entity to target (must already be an entity, cannot be the string the user entered)
        :return: None
        """
        self.target = target

    def set_using(self, using):
        """
        Sets the entity for this command to use
        :param using: Entity to use (must already be an entity, cannot be the string the user entered)
        :return: None
        """
        self.using = using

    def run(self):
        pass
