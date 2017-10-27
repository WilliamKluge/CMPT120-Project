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

## Grading Project 3
* **Use lists to store location data** See Engine::Locations
  * **Store all location descriptions in one list instead of separate variables.** See DescriptionNode (this just holds
   the variable for describing the location) used in Entity::components
  * **Store the boolean “has been there” values in another list.** See LocationsVisitedNode applied in 
  Entity::Components. The boolean aspect of this can be seen as LocationsVisited::has_visited(), even though 
  LocationsVisited's main purpose is to record (in order) where the player discovered.
  * **Your game must now define at least eight (8) different locations.** See main()
  * **Draw a diagram of your game world that shows all paths between locations.** See game map.pdf
  * **Continue refactoring your code to rely on functions for specific tasks.**
    * **Show introduction** See TitleScreenSystem added to queue in main.
    * **Customize Player** See TitleScreenSystem line 68
    * **Initialize Game Data** See main() (any lines with entities or engine)
    * **Do game loop** See Engine::update()
    * **Show ending** See QuitSystem, not really tied to main but triggered by events in systems initialized in main()
  * **Make a function to handle the game loop itself** See Engine::Update
    * **Show Scene** See DrawLocationSystem
    * **Process Input** See UpdateCommandSystem
    * **Update Game** See pretty much any system
  * **Make a goto function that handles moving the player and updating the score** See MoveSystem
    * **Case Insensitive** See UpdateCommandSystem line 41
    * **Two new commands** See MapCommand and PointsCommand
  * **Add a "time limit"** See Engine line 99-101
  