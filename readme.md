### TODO
* more testing, look into coverage and try to get 100%. Add functional tests?
* save the hhs txt in this folder!
* fix pb database: Main Pot, Side Pot etc. and add position.
* create public fork without the tracker link generator and without my own stuff in global variable
* create helpers/convert_json_to_pretty_table.py  
* create db apis to generate JSON data OR plot image path :


    [txt] total rake payed per tracked tourney
    [txt] get number of games played per tracked tourney
    [txt] get avg prize and profit per tracked tourney
    [txt] get lifetime win/loss per tracked tourney
    [txt] get % of cash per tracked tourney
    
    [plot] find the most common money spot: extract the hands where I won the pot, and categorize them (coolers, PFAI, ..). 
           Aggregate the number of chips won and make pie chart + figure out % of stack invested in a hand
    [DONE] [plot] rate of profit/game plot: does the profit/game increases or decreases over time?
    [plot] relationship between position and first hand's level: does regging early improve my chances of winning?
    [DONE] [plot] plot $ won/lost per buyin sharkscope style
    [DONE] [plot] plot chips won/lost during tournament x
    
    [table] show all opponents sorted by most seen first 
    [table] show all n tournaments   
    params: all time / last n sng | sort by [most recent, highest prizes]
    [table] show all n hands   
    params: all time / from last n sng | how many to get | type | sort_by [pot_size, level]
    [table] show all hands from tournament x 
    [table] show equity of my hand vs others when allin before river

* create note-taking db and api
* rewrite this doc
_______


Challenges and solutions:
* finding a way to architect this app while remaining flexible
* finding an appropriate testing strategy
* dealing with missing tourney summaries
* dealing with hand histories split into multiple files
* i dont know what this app's gonna be, so better to create an API to access the DB that always returns JSON data OR path to plot image
* the goal of this program is to have an easy-to-use API that 1) updates the database and 2) allows me to answer questions about the data in this db. However I don't know all of those questions, so I built this app always coming back to the data import when I needed more informations I didnt extracted already
* its very hard and tiring to look at data, so I reverse-engineering a website where you can upload your hand history and it replays it.
* clear separations of tasks in folder/files/functions, fully tested and 0 code repetition. 


Problems/trade-offs of current implementation:
* hand histories get auto deleted after 30 days, so the data I didnt extract "on time" is lost.
* adding a hand is somewhat slow (+- 2secs) because an API call has to be made
* not following a particular design pattern
* SQL design pattern breach: winner in hands table contains multiple items sometimes (side pots)


Skills:
* testing 
* data pipeline testing/building
* data exploration and understanding: there was tons of irrelevant hands where im not playing (fold pre), there were tournaments where the HH summary wasn't saved at all (missing data). 
* SQL
* documentation
* plotting

Why I did this project?
* make more money playing this game
* show off skills to employers
* have fun building a project 
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

