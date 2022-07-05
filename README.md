# Logger

print and write logs to stdout, stderr and a logfile

# writeLog


Write string to logfile if logfilepointer is set.

Parameters
----------
string : str
    Message to write to logfile

# error

Write error string to stderr and logfile if logfilepointer is set.
Exit program with given error code.

Parameters
----------
string : str
    Message to write to stderr and logfile
error_type : int
    used error_type, default 1

# warning

Write warning string to stderr and logfile if logfilepointer is set.
        
Parameters
----------
string : str
    Message to write to stderr and logfile

# printLog

Write datetime and string to stdout and logfile if logfilepointer is set.
        
Parameters
----------
string : str
    Message to write to stdout and logfile.
newline_before : bool
    Add newline before string, default False.
newline_after : bool
    Add newline after string, default True.