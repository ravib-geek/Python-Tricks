#!/usr/bin/python


scores = {
   "Foo" : 10,
   "Bar" : 34,
   "Moo" : 88,
   "Pierre": 42, 
   "Anne": 33, 
   "Zoe": 24
}


new_list = list()

for key, val in scores.items():
    new_list.append( (val, key) )

new_list.sort(reverse=True)

for key, val in new_list:
    print key, val
