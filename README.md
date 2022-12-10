# bulkee
bulkee makes it easy to batch-rename an entire directory. 

# Usage
`python bulkee.py pattern` with the .py file in the directory you want to batch-rename.
Your "pattern" can be any string, and can also contain special flags which will rename the file with the file metadata.  
Flags:   
```  
.ct - The time the file was created
.mt - The last time the file was modified
.sk - The file size in KB
.sm - The file size in MB
.sg - The file size in GB
.t: - The file type
```  
So basically, if you wanted to do `python bulkee.py hello world! .sk .ct`, that would be valid syntax.
