#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:34:37 2017

@author: vmang
"""
import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(.005)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    
    van = turtle.Turtle()
    van.shape("arrow")
    van.color("red")
    van.circle(100)
    
    window. exitonclick()
draw_square()


