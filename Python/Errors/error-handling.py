# https://www.youtube.com/watch?v=NIWwJbo-9_8

try:
    f = open('corrupt_file.txt')
    # FileNotFoundError
    # f = open('textfile.txt')
    # NameError
    # var = bad_var

    # Can be put here but may raise some unexpected errors
    # print(f.read())
    # f.close()

    #! Custom Exception
    if f.name == 'corrupt_file.txt':
        raise Exception

except FileNotFoundError:
    print('Sorry, This file does not exists')

except Exception as e:
    # print("Sorry, Something Went Wrong")
    print("Exception")

else:
    # runs only if exception is not raised
    print(f.read())
    f.close()

finally:
    # runs no matter the exception is raised or not
    print("Executing Finally....")
