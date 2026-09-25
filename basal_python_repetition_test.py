import basal_python_repetition

# Alle følgende funktioner er testfunktioner
# Din opgave er at oprette dem i filen basal_python_repetition.py
# fx. skal der oprettes en funktion navngivet return_hello
# return_hello-funktionen skal returnere en string "Hello, World!"
# når filen basal_python_repetition pushes til github vil testen køres
# Efterfølgende kan man se på github hvordan testen gik.
# når 100 points er givet på github er alle tests fuldført.

# OBS DENNE FIL MED TESTFUNKTIONERNE MÅ DER IKKE ÆNDRES I!

# lav funktionen return_hello, så at testen fuldføres
def test_return_hello():
    assert basal_python_repetition.return_hello() == "Hello, World!"

# lav funktionen average_of_two_numbers, så at testen fuldføres
def test_average_of_two_numbers():
    assert basal_python_repetition.average_of_two_numbers(10, 20) == 15

def test_average_of_two_numbers_floating():
    assert basal_python_repetition.average_of_two_numbers(999.999, 333.333) == 666.666

# lav funktionen rectangle_area, så at testen fuldføres
def test_rectangle_area():
    assert basal_python_repetition.rectangle_area(10, 40) == 400

def test_rectangle_area_floating():
    assert basal_python_repetition.rectangle_area(1337, 13.37) == 17875.69

# Lav funktionen så at testen fuldføres brug: T(°C) = (T(°F) - 32) × 5/9
def test_fahrenheit_to_celsius():
    assert basal_python_repetition.fahrenheit_to_celsius(108) == 42.22222222222222

def test_fahrenheit_to_celsius_floating():
    assert basal_python_repetition.fahrenheit_to_celsius(13.37) == -10.350000000000001

# Lav funktionen så at testen fuldføres brug: T(°F) = T(°C) × 9/5 + 32
def test_celsius_to_fahrenheit():
    assert basal_python_repetition.celsius_to_fahrenheit(37) == 98.6

def test_celsius_to_fahrenheit_floating():
    assert basal_python_repetition.celsius_to_fahrenheit(13.37) == 56.066

# Skriv en funktion, der tager en streng som parameter. 
# Navngiv funktionen "echo" Den skal returnere de første tre tegn fra strengen, gentaget tre gange. 
# Hvis der er mindre end tre tegn i strengen, skal den returnere hele strengen
    # sørg for at de to tests fuldføres
def test_echo():
    assert basal_python_repetition.echo("Python") == "PytPytPyt"

def test_echo_less_than_3_chars():
    assert basal_python_repetition.echo("Na") == "NaNaNa"