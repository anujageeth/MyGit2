import sys

def cat():
    print('Meow')

def default():
    print('hello')

def main():
    default()

if __name__=='__main__':
    if sys.argv[1] == 'cat':
        cat()
    else:
        main()
