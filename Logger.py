'''
print and write logs to stdout, stderr and a logfile.
'''

import datetime
import sys
from io import TextIOWrapper

class Logger():
    '''
    Logger class to print and write logs to stdout, stderr and a logfile.
    '''
    
    def __init__(self, logfilepointer: TextIOWrapper = None):
        self.lp = logfilepointer

    def writeLog(self, string : str, flush : bool = False) -> None:
        '''
        Write string to logfile if logfilepointer is set.

        Parameters
        ----------
        string : str
            Message to write to logfile
        '''
        if self.lp is not None:
            self.lp.write(string)

            if flush:
                self.lp.flush()

    def error(self, string : str, error_type : int = 1) -> None:
        '''
        Write error string to stderr and logfile if logfilepointer is set.
        Exit program with given error code.
        
        Parameters
        ----------
        string : str
            Message to write to stderr and logfile
        error_type : int
            used error_type, default 1
        '''
        sys.stderr.write(f'ERROR: {string}\n')
        self.writeLog(f'ERROR: {string}\n')
        sys.exit(error_type)

    def warning(self, string : str) -> None:
        '''
        Write warning string to stderr and logfile if logfilepointer is set.
        
        Parameters
        ----------
        string : str
            Message to write to stderr and logfile
        '''
        sys.stderr.write(f'WARNING: {string}\n')
        self.writeLog(f'WARNING: {string}\n')

    def printLog(self, string : str, newline_before : bool = False, newline_after : bool = True) -> None:
        '''
        Write datetime and string to stdout and logfile if logfilepointer is set.
        
        Parameters
        ----------
        string : str
            Message to write to stdout and logfile.
        newline_before : bool
            Add newline before string, default False.
        newline_after : bool
            Add newline after string, default True.
        '''
        if newline_before:
            sys.stdout.write('\n')
            self.writeLog('\n')
            
        sys.stdout.write(f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")} LOG: {string}')
        self.writeLog(f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")} LOG: {string}')
        
        if newline_after:
            sys.stdout.write('\n')
            self.writeLog('\n')

    def close(self) -> None:
        '''
        Close TextIOWrapper
        '''
        if self.lp is not None:
            self.lp.close()