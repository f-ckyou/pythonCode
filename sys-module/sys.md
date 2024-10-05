## **Sys module**

- provides access to some variables and functions that interact with the Python runtime environment.
- allows to interact with the interpreter, manipulate system-specific parameters, handle input/output, and control the runtime behavior of python programs

----

## **Important Methods & Attributes**

- ` sys.argv ` : returns a list of command line arguments passed to a script
    - **When to use**: to capture arguments passed to your python script from the command line
    - Example:
    If you run the script as `python script.py arg1 arg2`, it will print `['script.py', 'arg1', 'arg2']`.


- `sys.exit([arg])` : exits from python
    - **When to use**: to gracefully exit a program or terminate it based on some conditions
    - Example: 
    ``` python
        import sys
        if some_error:
            sys.exit("An error occurred.")

    ```

- ` sys.path ` : returns a list of directories that python searches for modules to import


- ` sys.stdin, sys.stdout, sys.stderr ` : Represent standard input, output, and error streams



    - Example of `sys.stderr`: 
    ``` python
            import sys

            # Output error message in red
            sys.stderr.write("\033[91mThis is an error message in red.\033[0m\n")     
    ```
    **Explanation**: <br>
    ` \033[91m ` : starts the red color <br>
    ` \033[0m ` : resets the color to the default terminal color <br>
    ` sys.stderr.write() ` : sends the output to the error stream, which is often used for error messages


- ` sys.getsizeof(object) ` : returns the size of an object in bytes


- ` sys.version ` : returns the version of the Python interpreter in use


- ` sys.platform ` : returns a string that identifies the platform on which python is running


- ` sys.modules ` : returns a dictionary of all the modules that have been loaded in the current session


- ` sys.maxsize ` : returns the largest integer that python can handle on the system


