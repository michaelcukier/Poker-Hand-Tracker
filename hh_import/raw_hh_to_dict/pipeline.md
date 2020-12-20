
### Description of the pipeline

Task #1: Query the local SQL database to get the tournaments IDs  
returns `db_tourney_ids = [...]`

____

Task #2: Query the local filesystem to get all the .txt filenames in the hand history folder  
returns `tourney_filenames = [...]`

____

Task #3: Filter down the list of .txt filenames:  
takes `db_tourney_ids` and `tourney_filenames` and returns `new_hhs`

    * remove the ones already in the db
    * remove the ones that aren't tracked 
    * group the remaining ones by {tourney_ID: [filename1, filename2, ...]}

____
Task #4: Extract tournament summary and content in a dict  

    * concatenate the multiple .txt files into one big string
    * extracts the tourney summary from filesystem into a dict
    * selects the first filename and assign it to title

takes `new_hhs` and returns a dict:
```
final_hhs = [{

    id: int,
    title: str
    summary: dict or None,
    hands: str
    
}, {

    ...

}]
```


