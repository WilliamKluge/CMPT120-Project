# Holds the Entity class
# Author: William Kluge
# Date: 2017-9-18


class Entity(object):
    """
    The entity class from which all game items are composed.
    An entity contains a dictionary of components. These components can be used by processes. By having a general
    definition of what an entity is and what components a process needs to run, the program is able to use the same
    process for many different types of entities.
    """

    def __init__(self):
        self.components = dict()

    def add_component(self, component):
        """
        Adds a component to this entity
        :param component: A data to be used by a process. This must be a new-style class
        :return: None
        """
        self.components[component.__class__.__name__] = component

    def remove_component(self, component_class):
        """
        Removes a specific component from this entity
        :param component_class: Class of a component to remove from this entity
        :return: None
        """
        del self.components[component_class]

    def get_component(self, component_class):
        """
        Gets the value of a component from this entity
        :param component_class: Class of the component to get
        :return: Value associated with component_class
        """
        return self.components[component_class]
