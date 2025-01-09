# all generic sample codes add in this.

"""
Need to practice below type of codes:

setting the property to widget object.
class inheritance, mro related samples.

q) If you want to assign a callback to a widget which lacks the 'command' property, which method would you use?
    answer) bind() method will be used.
q) If you want to set a 'wdg' widgets property named 'x' with an integer value of 100, which of the code lines would you use?
    answer) wdg.config(x-100)
    answer) wdg["x"]=100
q) Let's assume that you are working on a project and have found out that manual invoking of your own callback can simplify the code. what can you do now?
    answer) invoke the 'invoke()' method from within a particular widget
    question) what is use of callback(), call() methods.
q) how to set background color to button widget. different ways. other ways which will not work?
q) what can be said about the Message widget?
    answer) It can automatically format its inner text.
    answer) It is very similar to Label widget.
question) try to create similar questions for other widgets also.
q) what can be said about the 'Entry' widget?
    answer) The input field content can be accessed through an observable variable
    answer) it can grab and lose focus
    answer) the input field content can be accessed as the get() method's result
q) you decided not to allow the user to change your application window size. what would you do?
    answer) invoke the 'resizable()' method from within the root window object.
---
q) which one of the geometry managers produces different layouts depending on the order of invocations?
q) what can be said about callbacks?
q)

"""

from tkinter import *
w = Tk()
x = IntVar()
#x.set(100)
print(type(x), x.get(), x)
# w = Tk()
# b1 = Button(w, text="A")
# b1.pack()
# b2 = Button(w, text="B")
# b2.pack()
# # what make the b1 button focused?
# b1.focus()
# print("window shoult apear.")
# w.mainloop()