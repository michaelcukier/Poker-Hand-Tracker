
### Folder structure

This program automatically imports the hand histories from the raw .txt files into a .sqlite database. 
It performs some transformations on those raw .txt files to extract the relevant data.  

    run.py                                # 10-line python code to use this program
    
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
