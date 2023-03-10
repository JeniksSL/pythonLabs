# no OOP
def inputDimensions():
    while True:
        try:
            n = int(input("Input rectangle width (less than 100): "))
            m = int(input("Input rectangle height (less than 100): "))
            if n < 1 or n > 100 or m < 1 or m > 100:
                raise ValueError()
            return {"width": n, "height": m, "squares": 0}
        except ValueError:
            print('Invalid format')


def divideOnSquare(rectangle):
    if isinstance(rectangle, dict) and ("width" in rectangle) and ("height" in rectangle) and ("squares" in rectangle):
        print("Incoming rectangle with width: " + str(rectangle["width"]) + ", and height: " + str(rectangle["height"]))
        if rectangle["width"] == rectangle["height"]:
            rectangle["squares"] += 1
            print("This is square with width: " + str(rectangle["width"]) + ", and height: " + str(rectangle["height"]))
            print("Total squares: " + str(rectangle["squares"]))
            return
        elif rectangle["width"] > rectangle["height"]:
            rectangle["width"] -= rectangle["height"]
            rectangle["squares"] += 1
        else:
            rectangle["height"] -= rectangle["width"]
            rectangle["squares"] += 1
            divideOnSquare(rectangle)
    else:
        print("Unsupported parameter")


divideOnSquare(inputDimensions())
