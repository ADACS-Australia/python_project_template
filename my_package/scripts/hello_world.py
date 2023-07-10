
#!/usr/bin/env python

# The above is a shebang that tells the shell what interpreter to use

# This will import your function from the package
from my_package.my_file import my_function

# This is the main function that will be run when the script is called
def main():
    my_function()

if __name__ == "__main__":
    main()