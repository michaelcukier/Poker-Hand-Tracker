
### REFACTOR

### then rewrite this doc

#### create VARIABLES.py with:
- player name
- list of tracked tourney
- folder for hh (hh and summary)
- local database folder

#### make extract_data_from_raw_hh.py a folder instead 

### THEN MAKE THE TESTS WORK

_______

### What is PokerHUDv2?

This program automatically imports the hand histories from the raw .txt files into a .sqlite database. 
It performs some transformations on those raw .txt files to extract the relevant data. It then conveniently exposes a Python API to explore this database and create plots, pretty-printable tables, etc. 

### Folder structure


    run.py                                # 10-line python code to use this program
    
    ├── /__tests__/     
    
    ├── /database/     

    ├── /hh_import/                       
        ── get_raw_hh_from_file.py        # returns an array of not-yet-processed .txt files
        ── extract_from_raw_hh.py         # extracts relevant data from .txt files
        ── store_hh_sqlite_db.py          # stores new data in the sqlite db
        
    ├── /add_notes/                        
        ── add_hand_note.py               # adds a note linked to a hand ID
        ── add_tournament_note.py         # adds a note linked to a tournament ID
        
    ├── /db_api/                         
        ├── /tournaments/                 # 
            ── get_tournaments.py         # 
        ├── /hands/                       # 
        ├── /summaries/                   # 
        
    ├── /helpers/                         


### How to use
