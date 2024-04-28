"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    pass
    x = 1
    for i in range(101):
        print(i)

    print()

    for i  in range(100, -1, -1):
        print(i)
    print()
    for i in range(101):
        if i % 2 == 0:
            print(i)
    print()
    for i in range(100):
        if i % 2 > 0:
            print(i)

    for i in range(501):
        if i % 2 == 0:
            print(f"{i} even ")
        if i % 2 > 0:
            print(f"{i} odd")




    for i in range(778):
        if i % 7 == 0:
            print(i)

    for i in range(2012, 2025):
        print('These are all the years I have been alive' + str(i))

    for i in range(3):
        for j in range(3):
            print(f"{i} {j}")

    for i in range(0,9,3):
        for j in range( i +1, i + 4 ):
            print( f'{j} ', end = '')
        print("")


    for i in range(-1, 100, 1):
        for j in range(i +1, i+ 2):
                print(f'{i} {j} {i} {j} {i} {j} {i} {j} {i} {j}', end = "")
        print('')


    for i in range(5):
        for j in range(i + 1):
           print( '* ' , end = '')
        print('')












