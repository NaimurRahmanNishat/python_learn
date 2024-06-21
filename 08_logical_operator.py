"""
and = both condition has to full fill (I mean both condition is must be true)
or = at least one condition fill (I mean at least one condition is must be true)
"""

has_pc = True     # This is case sensitive. {not true (True is right syntex)}
has_resource = True
if has_pc and has_resource:
    print("I learn python")
# Output is: I learn python

has_pc = True     # This is case sensitive. {not true (True is right syntex)}
has_resource = False
if has_pc and has_resource:
    print("I learn python")
# Output is: blank output.

has_pc = True     # This is case sensitive. {not true (True is right syntex)}
has_phone = False
has_resource = True
if (has_pc or has_phone) and has_resource:
    print("I learn python")
# Output is: I learn python

has_pc = True     # This is case sensitive. {not true (True is right syntex)}
has_phone = not True
has_resource = not False
if (has_pc or has_phone) and has_resource:
    print("I learn python")
# Output is: blank output.


# Not Operator
has_pc = True     # This is case sensitive. {not true (True is right syntex)}
has_phone = True
has_resource = False
if (has_pc or has_phone) and not has_resource:
    print("I learn python")
# Output is: I learn python

has_pc = True     # This is case sensitive. {not true (True is right syntex)}
has_phone = True
has_resource = True
if (has_pc or has_phone) and not has_resource:
    print("I learn python")
# Output is: blank output.


