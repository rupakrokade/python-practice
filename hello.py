import sys

def Hello(name):
    if name == 'Alice' or name == 'Nick':
        name = name + '????'
    name = name + '!!!!'
    print 'Hello', name

#hello world function definition
def main():
    Hello(sys.argv[1])

#call hello function
if __name__ == '__main__':
    main()
