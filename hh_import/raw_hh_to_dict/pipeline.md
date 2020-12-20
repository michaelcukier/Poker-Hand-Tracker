
### Description of the pipeline

`task_1.py` | Query the local SQL database to get the tournaments IDs  
returns `db_tourney_ids = [...]`

____

`task_2.py` | Query the local filesystem to get all the .txt filenames in the hand history folder  
returns `tourney_filenames = [...]`

____

`task_3.py` | remove the tournaments IDs already in the db  
takes `db_tourney_ids` and `tourney_filenames` and returns `filtered`
____

`task_4.py` | remove the tournaments that aren't tracked   
takes `TOURNAMENTS_TO_EXTRACT` and `filtered` and returns `filtered`

____

`task_5.py`  | group the remaining ones like this: {tourney_ID: [filename1, filename2, ...]}  
takes `filtered` and returns `filtered`

____

`task_6.py`  | concatenate the multiple .txt files into one big list of hands 
takes a dict `{tourney_ID: [filename1, filename2, ...]}` and returns `tourney_ID: {hands: [...]}`
____

`task_7.py`  | clean that list of hands to remove the hands where i'm not playing 
    ("will be allowed to play after the button" thing)

____

`task_8.py`  | extracts the tourney summary from filesystem into a string

____

`run.py`  | create the final dict: 

```
final_hhs = [{

    id: int,
    title: str
    summary: dict or None,
    hands: list
    
}, {

    ...

}]
```


