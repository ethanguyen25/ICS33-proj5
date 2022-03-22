import controller
import model   # Pass a reference to this module when calling each update in update_all

# Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running     = False
cycle_count = 0
sims        = set()
name        = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running = False
    cycle_count = 0
    sims.clear()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    """
    The step button stops the simulation after executing one cycle: if it is running, 
    it stops after one more cycle: if it is stopped it starts for one cycle and then stops again.
    """
    global running#, cycle_count
    if running == True:
#         cycle_count += 1
        update_all()
        running = False
    else:
        running = True
#         cycle_count += 1
        update_all()
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    """
    The select_object function remembers (using a global name) the string of the button clicked 
    (which it is passed as an argument: see object_button in the controller module
    """
    global name
    name = kind
    print(f'Selected object: {kind}')


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    """
    creates an object from the last remembered selection at the (x,y) coordinates of the click: 
    using eval makes this method small, and easily extendable to other classes of simultons
    """
    global name
#     print((x,y))
    if name == None:
        print("Nothing Selected")
    elif name == "Remove":
#         print(x,y)
        try:
            for stuff in sims:
                if stuff.contains((x,y)):
                    sims.discard(stuff)
        except Exception:
            pass
    else:
        sims.add(eval(name + "(" + str(x) + "," + str(y) + ")"))

#add simulton s to the simulation
def add(s):
    global sims
    sims.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global sims
    sims.discard(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global sims
    lis = [x for x in sims if p(x) == True]
    return lis


#call update for every simulton (passing each model) in the simulation
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global running, cycle_count, sims
    if running:
        cycle_count += 1
        for x in sims.copy():
            x.update(model)

#To animate: first delete every simulton from the canvas; then call display on
#  each simulton being simulated to add it back to the canvas, possibly in a
#  new location; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in sims:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(sims))+" sims/"+str(cycle_count)+" cycles")

