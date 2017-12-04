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
* **Assets**  
  Textures for the game. all background images are 936x527 all map icons are 47x26
* **CommandFramework**  
  Contains code related to how the user's input is interpreted as commands
  * **ImplementedCommands**  
  Contains the definitions of *ICommand* children that are the actual commands of the game
* **EndConditionFramework**  
  Contains code related to defining conditions that the game should end within the user quitting
  * **ImplementedCommands**
  Contains children of *IEndCondition* that define the actual conditions that end the game
* **EntityFramework**  
  Contains code related to constructing the 
  <a href="http://www.richardlord.net/blog/ecs/what-is-an-entity-framework.html">entity framework</a>
  * **Nodes**  
    Contains defined nodes (used to store attributes for entities)
  * **Systems**  
    Code related to systems
    * **ImplementedSystems**  
      Defined systems (how it will behave)
    * *Engine.py*  
      The central game engine that controls the running of systems
    * *ISystem.py*  
      Interface for building a system
  * *Entity.py*  
    Definition of what an entity should be (essentially a container for nodes).
* **PygameLibraries** Libraries that add to the functionality of pygame. These need to be bundled with the program 
source.
  * *eztext.py* Library for text input in the pygame gui
* *main.py* The main function of the game

## Grading Project 4
* **Change your handling of player movement to rely on a matrix.** This is a slightly abstract was of thinking about it,
but the dictionary located in Engine::locations serves as the first dimension and then the contents of the entities
within act as the second dimension. For simple look at how I would use a traditional matrix, see MatrixMovement.py.
* **Your game must now define at least ten (10) different locations.** See main.py
  * **Add a new list to the short name for each location (such as “the beach”).** See main.py location initialization,
  added a NameNode to locations.
  * **After discovering a location, subsequent visits show only the short name.** See DrawLocationSystem lines 46-51
* **Player must now have an inventory and some locations contain items.** See main.py player initializing, adding
InventoryNode
  * **The inventory is a list that holds items the player picks up.** See InventoryNode::inventory
  * **You will need another list of the items at each location.** See main.py location initialization, adding
  InventoryNode
  * **At least three (3) of your locations must contain an item at the start.** See main.py location initialization,
  parameters when adding InventoryNode
  * **One item must be a map – “map” command works only if player has it.** See main.py line 43
* **Add new player commands:**
  * **Look around – displays the long description of a location.** See LookCommand
  * **Search/Examine – reveals the item (if any) at the current location.** See SearchCommand
    * **Record whether locations have been searched using a list of booleans.** See InventoryNode::searched
  * **Take – add item to the inventory (and remove from current location).** See TakeCommand
    * **Only allow the player to take an item if she has first searched the area.** See TakeCommand::is_possible
* **Add new win and loss conditions in addition to what you have so far.** See main.py lines 145-147
  * **Bringing a specific item to a specific location wins the game.** See MapTowerWinCondition
  * **Entering a specific location without a specific item loses the game.** See MapRiverLossCondition