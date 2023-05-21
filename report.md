# AI - HW 1 - Report
The task is unclear. We don't know what sensors the agent have, so it can be implemented in many ways.

I assumed the agent only has a dirt sensor, so it moves randomly, sometimes hits the wall (it tries to move, but the environment doesn't allow it), and after each move checks if there is anything to clean.

The agent is so simple. I wrote it as a class with two methods:
```python
Agent.choose_action(percept:str) -> action:str
Agent.increase_performance() -> None
```

The first one gets an string from the environment as perception (`'clean'` or `'dirty'`) and returns an action (a random move or `'clean'`)
The second one increases the performance by 1. Performance is given by environment and stored in the agent memory. (I don't know why I wrote it that way!)

The environment is more complex. It can generate itself, random dirty locations, keep track of visited locations, add agents to itself, run, ...

Although the question wants the agent to go through all locations, I made the program stop when all dirty locations are cleaned (the environment can check it with `Environment.is_done()`). I kept track of visited locations for future improvement (maybe I'll add a footprint sensor later!).

To run the program, run `main.py`. You'll be asked for dimensions and initial position of the agent, and the agent starts to  search and clean dirty locations. Sample output during running:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ o o               o     o o   o o   o   ┃
┃                                   o o   ┃
┃           o o               o o     o o ┃
┃ o         o o           o o o   o   o o ┃
┃                   o           o o o   o ┃
┃                                   o   o ┃
┃         o   o o               A o o o o ┃
┃         o   o       o           o   o   ┃
┃         o   o   o o o o             o o ┃
┃ o       o   o o       o o               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

STEP: 265   | ACTION: down 
searching for dirt ...
Agent Performance: 42
```
___

Thanks for your time :)

Hossein Shojaeifar,
M. Sc. Computational Linguistics,
SID 830499057