# CMPT120-Project

## TL;DR Summary
Text based adventure game for my Intro to Programming final project.

## Summary
This game is called <i>Nowhere</i> and the main objective is to get somewhere.<br>
The player starts in the middle of Nowhere, a foggy forest landscape with a few structures surrounds them. Using
their environment and wit they need to find their way back to somewhere before it is to late.

## Dependencies
* Pygame
  * Installation instructions are platform specific - see 
  <a href="http://www.pygame.org/wiki/GettingStarted#Pygame Installation">their website</a> for details.

## Project Structure
* Assets<br>
  Textuers for the game. all background images are 936x527 all map icons are 47x26
* CommandFramework<br>
  Contains code related to how the user's input is interpreted as commands
* <b>EntityFramework</b><br>
  Contains code related to constructing the 
  <a href="http://www.richardlord.net/blog/ecs/what-is-an-entity-framework.html">entity framework</a>
  * <b>Nodes</b>
    Contains defined nodes (used to store attributes for entities)
  * <b>Systems</b>
    Code related to systems
    * <b>ImplementedSystems</b>
      Defined systems (how it will behave)
    * <i>Engine.py</i>
      The central game engine that controls the running of systems
    * <i>ISystem.py</i>
      Interface for building a system
  * <i>Entity.py</i>
    Definition of what an entity should be (essentially a container for nodes).
* <b>PygameLibraries</b> Libraries that add to the functionality of pygame. These need to be bundled with the program 
source.
  * <i>eztext.py</i> Library for text input in the pygame gui
* <i>main.py</i> The main function of the game