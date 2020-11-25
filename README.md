# PiWeeklyTimer

This project is an initial draft of how a weekly timer could be used for household shores using a raspberry pi and some diodes.

## Ideas:

_Board:_
```
  ...........
  .  X   B  .
  .  X   B  .
  .  X   B  .
  .  X   B  .
  .    b    .
  ...........
```
  
 X = Lamp,
 B = Reset Button.
 The bottom button (b) is the change number of days of a timer.

  * A button resets a timer to 0 and the lamp will turn off.
  * If the reset button is pressed all lamps should flash on/off with 1sec interval: If a "lamp" button is then pressed only that will flash faster, meaning it is configuarable. Then we will count the amount of times the adjecent button is pressed, for example 3 times = 3 days. When the bottom button (b) is then again pressed the chosen timer lamp will flash the chosen number of days, i.e. 3 times before all lamps go back to their last state.
