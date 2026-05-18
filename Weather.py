weather = (1, 0, 0, 0, 1, 1, 0)
rain = 0
sunny = 0

for x in weather:
    if weather[x] == 0:
        sunny += 1

    else:
        rain += 1

if sunny>rain :
    print("This week will have more sunny weather")
    print("Next day is most likely to be sunny")

else:
    print("this week will have more rainy weather ")
    print("Next day is most likely to be rainy")
        