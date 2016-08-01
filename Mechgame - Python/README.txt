Python Command Prompt Battletech Game
=====================================

Present Goals:
--------------

A working game that allows for:
	- Accurately displaying menu of assorted Mechs
	- Choosing a player Mech
	- Putting player in a rudimentary level with several opponents
	- Follows Battletech rules (2D6 rolls, etc.) to determine turn outcomes

Some notes on the ongoing Python project organized by filename:

|-------------|
| mechgame.py |
|-------------|

Purpose: Main python execution file, imports constructors and JSON, intial player choices
Notes:
	- Imports custom Mech class constructor
	- Loads built JSON objects (preserved structure)
	- Allows for player choice from menu of built JSON objects
	- Constructs one player Mech from choice with Mech class constructor (tested)

|---------------|
| mechdata.json |
|---------------|

Purpose: JSON data file containing all general mech construction data
Notes:
	- Four example Mechs, sample info

|------------------|
| mechweapons.json |
|------------------|

Purpose: JSON data file containing all available weapon construction data
Notes:
	- (TODO) Need to construct weapon JSON objects according to mechdata.json file structure

|----------|
| mechs.py |
|----------|

Purpose: Class constructor for Mechs
Notes:
	- Preliminary initialization finished
	- Preliminary accessors and mutators finished
	- (TODO) Need basic action methods defined

|------------|
| weapons.py |
|------------|

Purpose: Class constructor for Mech weapons
Notes:
	- (TODO) Need to finalize initialization method
	- (TODO) Need accessors and mutators (???)
	- (TODO) Need basic action methods defined