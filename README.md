# CMPT120-Project

## TL;DR Summary
Text based adventure game for my Intro to Programming final project.

## Summary
This game is called <i>Nowhere</i> and the main objective is to get somewhere.<br>
The player starts in the middle of Nowhere, a foggy forest landscape with a few structures surrounds them. Using
their environment and wit they need to find their way back to somewhere before it is to late.

## Project Structure
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
* <i>main.py</i> The main function of the game