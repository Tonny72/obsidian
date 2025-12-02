---
title: Wait(-1)
updated: [[2020-02-15]]T18:14:44.0000000+01:00
created: [[2020-02-15]]T18:11:47.0000000+01:00
---

**Example:** Basic Key/Touchscreen Handler. Below is a skeleton for a basic keyboard and touchscreen handler using the [WAIT(-1)](https://en.hpprime.club/docs/reference/WAIT) command. By passing -1 as the argument, WAIT will essentially pause the program and wait for input from either the keyboard or the touchscreen. If no input is received after a minute, then -1 is returned. Otherwise, either the key number (for a keypress) or a "mouse" list (for touchscreen gestures) will be returned.
Due to the different types of objects (integer vs list) returned by this command, and the fact that mis-matched object types in a branch (such as an IF THEN END statement) will cause run-time errors, we must carefully parse the value(s) returned by WAIT. (Note that the touchscreen events MUST be parsed first in this implementation and that only part of the handler is shown; the necessary subroutines would need to be added accordingly.)

EXPORT KMINPUT()  
BEGIN LOCAL run := 1, key;  
// change run to 0 to exit the while loop  
key := WAIT(-1);  
CASE IF TYPE(key) == 6 THEN // we have touchscreen events  
CASE IF key(1) == 0 THEN kmMouseDown(); END;  
IF key(1) == 1 THEN kmMouseUp(); END;  
// ... more mouse events  
IF key(1) == 7 THEN kmMouseLongClick(); END;
kmMouseEvent(); // default handler  
END;  
END;
// at this point, all touch events were handled due to the  
// TYPE(key) == 6 check; so only key-presses are left  
// and if a touch event occurred, these tests below are  
// never reached
IF key == 0 THEN kmDoAppsKey(); END;  
// ... more key definitions here  
IF key == 50 THEN kmDoPlusKey(); END;
kmOtherEvents(); // handle all remaining undefined keys  
END;
END;
**Remark:** The way WAIT(-1) processes a mouse event is not the way one might expect. That is, a mouse click generates three separate events, so that three consecutive instances of WAIT(-1) are required to finally capture the mouse click.
So when a mouse click occurs, the first instance of WAIT(-1) returns a mouse-down event, the second instance of WAIT(-1) returns a mouse-up event, and finally the third instance of WAIT(-1) returns a mouse-click. The same goes for long clicks and other types of events. Please keep this in mind when creating a mouse/keyboard handler.

*Van \<<https://en.hpprime.club/articles/hans-hp-prime-programming-introduction/>\>*
