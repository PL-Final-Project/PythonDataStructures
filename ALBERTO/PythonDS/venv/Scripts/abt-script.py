#!C:\Users\aics1\Desktop\UPR\SMSTR_2_2019-2020\PROG_LANG\Project\PythonDataStructures\ALBERTO\PythonDS\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'abt==0.1.1','console_scripts','abt'
__requires__ = 'abt==0.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('abt==0.1.1', 'console_scripts', 'abt')()
    )
