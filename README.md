# Logger

print and write logs to stdout, stderr and a logfile

## Functions

callable functions

### writeLog

Write string to logfile if logfilepointer is set.

@param string: String to write to logfile.

### error

Write error string to stderr and logfile if logfilepointer is set.
Exit program with given error code.

@param string: String to write to stderr and logfile.
@param error_type: used error_type, default 1.

### warning

Write warning string to stderr and logfile if logfilepointer is set.

@param string: String to write to stderr and logfile.

### printLog

Write datetime and string to stdout and logfile if logfilepointer is set.

@param string: String to write to stdout and logfile.
@param newline_before: Add newline before string, default False.
@param newline_after: Add newline after string, default True.
