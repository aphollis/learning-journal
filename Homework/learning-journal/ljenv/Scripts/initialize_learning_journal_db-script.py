#!C:\Users\aphollis\onedrive\pycert\webpython\homework\learning-journal\ljenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'learning-journal','console_scripts','initialize_learning_journal_db'
__requires__ = 'learning-journal'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('learning-journal', 'console_scripts', 'initialize_learning_journal_db')()
    )
