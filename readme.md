Poker Hand Tracker
=================

This is a poker hand tracker for tournaments and SnGs played on ACR.   

This program processes the hand histories .txt files to extract some relevant data, such as hole cards, position, etc (see [List of extracted fields](#dataextracted)).

A CLI has been created for convenience, to update the database with new hand histories, create plots, create PrettyPrintable tables, etc (see [Examples](#examples)).
 
It has been built to make it easy to extend it and add your own plots or tables with whatever data or insight you're looking for (see [Adding my own plots or table](#createnew)).


## Content

* [Command Line Options](#commandlineoptions)
* [Installation](#installation)
* [Examples](#examples)
* [Adding my own plots or table](#createnew)
* [List of extracted fields](#dataextracted)
* [Folder structure and notes](#folderstructure)


<div id="commandlineoptions"></div>

Command Line Options
--------------------

| **command**   | **params**   | **description** |
| :----:    | :---:    | :---: |
| update-db | None     |  Updates the database with new tournaments |
| setup-database | None     |  Creates an empty database with the appropriate schema |
| show-money-graph | optional: buyin (float)     |  Shows a line plot of the money graph |
| show-reg-time-and-pos | optional: buyin (float)     |  Shows a box plot representing the relationship between registration time and final position|
| show-profit-rate | None     |  Updates the database with new tournaments |
| show-chip-graph | None     |  Updates the database with new tournaments |
| show-range | (required) player name (str), (required) position: blinds or early or middle or late    |  Shows the range of hands observed for a particular player  |
| show-last-n-tournaments | (required) n     |  Shows the last n tournaments |
| show-report-by-buyin | None     |  Shows statistics about each buy-in |


<div id="installation"></div>

Installation
--------------------

Step 1 | Make sure `matplotlib`, `scipy`, `PrettyTable` and `Click` are all installed.

Step 2 | Clone this repo, and run

    $ python cli.py setup-db

This will set up the database with the appropriate schema.

Step 3 | Open `GLOBAL_VARIABLES.py` and write this for the 4 variables:

`PLAYER_NAME` = your username    
`HAND_HISTORY_FOLDER` = replace `<>` with the the absolute path of the hand histories  
`TOURNEY_SUMMARY_FOLDER` = replace `<>` with the absolute path of the tournament summaries files  
`FOLDER_PLOT_DUMP` = replace `<>` with the absolute path of this project's code  
`DATABASE_LOCATION` = replace `<>` with the absolute path of the database .db file    
`TOURNAMENTS_TO_EXTRACT`: this one is slightly tricky. This is the list of tournaments you want to track, along with their buyins amount including rake. You need to find the common pattern between those filenames.
For example, let's say you play SnGs and cash games, and you want to track the $3 and $6 SnGs you are playing. So you hand history folder look like this:

```
...
HH20210223 SITGOID-G24121376T1 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt
HH20210223 SITGOID-G24121376T2 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt
HH20210223 SITGOID-G24120630T2 TN-$3 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt
... some cash game files ...
HH20210223 SITGOID-G24113211T3 TN-$6 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt
HH20210223 SITGOID-G24113211T1 TN-$6 Hold'Em Turbo - On Demand GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-T BUYIN-0.txt
...
```

The common pattern for the $3's could be `$3 Hold'Em Turbo - On Demand` for example. If you just write `$3` for example it will not work, 
since there's probably other files in this folder that have `$3` in their name but are not $3 SnGs. So for me, playing the $0.55, $1.65, $3.3 and $6.6 buy-in levels, this variable was always set to:

```python
TOURNAMENTS_TO_EXTRACT = {
    "$0{FULLSTOP}50 Hold'Em Turbo": 0.55,
    "$1{FULLSTOP}50 Hold'Em Turbo": 1.65,
    "$3 Hold'Em Turbo - On Demand": 3.30,
    "$6 Hold'Em Turbo - On Demand": 6.60}
```

Step 4 | Now, if you run `python cli.py update-db` it should import all your tournaments and hands. This can take a few minutes if you have a large number of hand histories. It will tell you how many tournaments/sngs it has added in the end. When you go back to playing, you'll have to re-run this command and it will import only the new hand histories.  
 
Step 5 | Run `python cli.py --help` to see the things you can do.


<div id="examples"></div>

Examples
--------------------
`$ python cli.py show-money-graph` 

![money graph](imgs/All_Profit_in_$_won_(all_buyins).jpg?raw=true "Money Graph")

--------------------

`$ python cli.py range PotNoodle99912 middle` 

![reg time pos](imgs/PotNoodle99912_middle.png?raw=true "reg time")

--------------------

`$ python cli.py show-chip-graph 23075960 15` 

![chip graph tournament](imgs/Chip_graph_for_Tournament_23075960.jpg?raw=true "chip graph")

--------------------

`$ python cli.py show-profit-rate` 

![reg time pos](imgs/Profit_rate_per_tournament_(across_all_tournament_buyins).jpg?raw=true "profit rate")

--------------------

`$ python cli.py show-reg-time-and-pos` 

![reg time pos](imgs/Relationship_between_regging_level_and_final_position.jpg?raw=true "relationship reg time pos")



<div id="createnew"></div>

Adding my own plots or table
--------------------


For example, let's say you want to see the amount of chips won / lost by position. The entire hand history is also stored in the database, in the `hand_txt` sql column in case you want to access it directly. 

1. Create a script that queries the SQL database and displays it in a table form (see `/db_api/` for some examples).
2. Create a new file in `cli_commands/` containing the CLI script that gets run when the command is called from the terminal. You can use this a wrapper, so if you have one command that does something, another that does something else and a third one that combines everything, you can wrap them up here.
3. Finally update `cli.py` to use that new script from the CLI for convenience


<div id="dataextracted"></div>

List of extracted fields
--------------------

There are 2 tables in the database: `hands` and `tournaments`.  

Every time you process a new hand history / tournament summary using `$ python cli.py update-db`, it will extract the following data:

| hands table | tournaments table    |
|    :----:   |          :---: |
| time, level, my_cards, board_cards, tournament_id, id, starting_stack_size_bb, main_pot_winner, side_pot_1_winner, side_pot_2_winner , side_pot_3_winner, main_pot_size_bb, side_pot_1_size_bb, side_pot_2_size_bb , side_pot_3_size_bb, nb_occupied_seats, table_type, BTN_player_name, SB_player_name, BB_player_name, UTG_player_name, UTGp1_player_name, MP_player_name, MPp1_player_name, MPp2_player_name, CO_player_name, BTN_stack, SB_stack, BB_stack, UTG_stack, UTGp1_stack, MP_stack, MPp1_stack, MPp2_stack, CO_stack, BTN_cards, SB_cards, BB_cards, UTG_cards, UTGp1_cards, MP_cards, MPp1_cards, MPp2_cards, CO_cards       | hands, id, price, finish_time, elapsed_time, prize, position, opponents, nb_of_participants   |

and save it in the database.




<div id="folderstructure"></div>


Folder structure and notes
--------------------

* I have use SQLite as my database of choice, for ease of use and easy debugging. I recommend using the excellent [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) to be able to open the .db database file.
* As per the license, the author is not responsible if you misuse this tool or lose your hand histories.
* To make it easy to build the complex Hand and Tournament classes, I have used the Builder Design pattern.
* I do not intend to compete in any way with the major commercial poker trackers when I built this project. I did it for fun, and to practice a variety of skills. Use this tool if you know how to code and want to derive interesting stats about your play with SQL/Python and don't want to build the database code to do so.
* I play on ACR, so it is using the ACR hand histories and the tournament summaries files. It should not be hard to port this tool to be used with other sites like PokerStars.
* This is built for tournaments and SnGs and I never used it for cash games. But you should also be able to port this code easily if you want to track cash games. 

```
    cli.py                                # the CLI code
    GLOBAL_VARIABLES.py                   # variables used by this project, 
                                          # for eg. your player username
    run_all_tests.py                      # little script to run all the tests at once

    ├── /cli_commands/                    # the Click commands used by cli.py
    
    ├── /import_new_tournaments/          # code that finds the new hand 
                                          # histories/tournaments summaries, processes 
                                          # them and stores in the database

    ├── /plots_dump/                      # folder where the plots are saved 

    ├── /db_api/                          # the scripts that make use of the 
                                          # data in the db to plot stuff, create tables etc.

    ├── /tests/                           # all the tests. follows the same folder 
                                          # structure as the entire project.

    ├── /utils/                           # some scripts to avoid duplicate code
```

Copyright
--------------------

Copyright (c) 2021 Michael Cukier. See [LICENSE](LICENSE) for details.