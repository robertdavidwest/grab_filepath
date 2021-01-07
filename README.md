# grab_filepath

I think I spend too much time trying to grab filepaths when I'm SSHing on a linux server. This is designed to quickly drill down through directories to get a filepath to a file.

## Quick Usage

    $ fp ~/some_directory

then follow on screen instructions to drill down to needed filepath. Optional second parameter of number of directory to show per page (defaults to 30).

e.g.

    $ fp ~/some_directory 10 

for 10 dirs per page 


## Installation 

Uses only the python3 standard library 

1. Clone the repo: `$ git clone https://github.com/robertdavidwest/grab_filepath.git`
2. `cd` into repo: `cd ~/path/to/grab_filepath`
3. Check that you have python3 installed in `/usr/bin/env/python3.6` or update the shebang on line 1 of `fp.py` to use a differnt filepath to python3 
4. make `fp.py` executable: `chmod +x fp.py`
5. make a bin dir in your home dir `$ mkdir ~/bin`
6. copy the file as follows `$ cp fp.py ~/bin/fp` 

Now you can use the tool on the command line as per usage above.

## Example usage: 


### Select by substring

* Step 1: 

```
rwest ~ $ fp ~/example/

#-----------------------
Displaying 1 to 2 of 2

/home/rwest/example/...
> 1. subdir1
> 2. subdir2

Type substring of dir to to make selection,
or select by number by prefacing '>', e.g: > 1.
Choose:
```

* Step 2:
```
Choose: subdir2

#-----------------------
Displaying 1 to 1 of 1

/home/rwest/example/subdir2/...
> 1. example.csv

Type substring of dir to to make selection,
or select by number by prefacing '>', e.g: > 1.
Choose: 
```

* Step 3

```
Choose: ex
/////////////////////////////////////////
/////////////////////////////////////////
Path to copy:

/home/rwest/example/subdir2/example.csv

/////////////////////////////////////////
/////////////////////////////////////////
rwest ~ $
```

### Select by number :

* Step 1: 

```
rwest ~ $ fp ~/example/

#-----------------------
Displaying 1 to 2 of 2

/home/rwest/example/...
> 1. subdir1
> 2. subdir2

Type substring of dir to to make selection,
or select by number by prefacing '>', e.g: > 1.
Choose:
```

* Step 2:
```
Choose: > 2. 

#-----------------------
Displaying 1 to 1 of 1

/home/rwest/example/subdir2/...
> 1. example.csv

Type substring of dir to to make selection,
or select by number by prefacing '>', e.g: > 1.
Choose: 
```

* Step 3

```
Choose: > 1.
/////////////////////////////////////////
/////////////////////////////////////////
Path to copy:

/home/rwest/example/subdir2/example.csv

/////////////////////////////////////////
/////////////////////////////////////////
rwest ~ $
```


