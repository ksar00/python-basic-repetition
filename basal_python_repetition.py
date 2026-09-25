def return_hello():
    return "Hello, World!"

def average_of_two_numbers(a,b):
    average = (a + b) / 2
    return average

def rectangle_area(w,h):
    area = w * h
    return area

def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    return c

def fahrenheit_to_celsius_floating(f):
    c = (f - 32) * 5/9
    return c

def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

def echo(text):
    if len(text) < 3:
        return text *3
    return text[:3] *3