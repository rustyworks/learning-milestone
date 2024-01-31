'''
You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

    Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
    Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
    Spaces and punctuation are counted as engraved units.

Write a function cost_of_project() that takes two arguments:

    engraving - a Python string with the text of the engraving
    solid_gold - a Boolean that indicates whether the ring is solid gold

It should return the cost of the project. This question should be fairly challenging, and you may need a hint.
'''

def cost_of_project(engraving, solid_gold):
    cost = len(engraving) * 10 + 100 if solid_gold else len(engraving) * 7 + 50
    return cost


# The solution approach
# Explanation:
# we assume that solid_gold is always boolean, and the solid_gold will be "flag" for the formula
# the solid_gold will implicitly converted into integer (zero or one)
def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost
