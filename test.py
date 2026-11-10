def main():
    print('This program draws rectangles with a height of 1.')

    width = int(input('Please enter the width of the rectangle as an integer: '))
    height = int(input('Please enter the height of the rectangle as an integer: '))

    print('Below is a rectangle with a height of', height, end='')
    print('and a width of ', end='')
    print(width, end='')
    print('.')

    # ---> Insert your code here to draw a line with width
    #      number of '#' characters. <-----
    i=0
    
    while i < height:
        j=0
        while j<width:
            print("#", end='')
            j=j+1
        i = i+1
        print()

    print('The rectangle is drawn above.  Goodbye.')


if __name__ == "__main__":
    main()