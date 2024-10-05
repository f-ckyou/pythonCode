## **os module**

- provides a way to interact with the operating system in a platform-independent way
- offers functionality for handling files, directories, environment variables, processes, and system information


----

## **Important Methods & Attributes**

- ` os.getcwd() ` : get current working directory

- ` os.chdir(path) ` : changes the current working directory to the specified `path`

- ` os.listdir(path) ` : returns a list of all files and directories in the specified `path`

- ` os.mkdir(path) ` : creates a single directory

- ` os.makedirs(path) ` : creates intermediate directories if they do not 

- ` os.remove(path) ` : deletes a file

- ` os.rmdir(path) ` : deletes an empty directory

- ` shutil.rmtree() ` : to remove a non-empty directory

- ` os.path ` methods : path manipulation utilities
    - `os.path.join(path1, path2, ...)` : joins one or more path components intelligently
    - ` os.path.exists(path)` : checks if a given path exists
    - `os.path.isfile(path)` : checks if the given path is a file
    - ` os.path.isdir(path)` : checks if the given path is a directory

- ` os.system(command) ` : runs a system command ( as if you were typing it in the terminal)
    - Note: Consider using the `subprocess` module for more complex system commands.

- ` os.getlogin() ` : returns the name of the uesr currently logged into the system

