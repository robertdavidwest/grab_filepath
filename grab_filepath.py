import sys
import os
from pprint import pprint


def compare_query_str_to_paths(msg, paths):
    query_str = input(msg)
    if query_str[-1] == '/':
        query_str = query_str[:-1]
        paths = [p for p in paths if query_str == p] 
    else:
        paths = [p for p in paths if query_str in p] 
    return paths


def display_paths(paths):
    print("#-----------------------")
    for p in paths:
        print("> " + p)


def show_available_dirs(new_paths, orig_paths):
    if len(new_paths) == 0: 
        new_paths = compare_query_str_to_paths("Try again: ", orig_paths)
        return new_paths
    
    display_paths(new_paths)
    new_paths = compare_query_str_to_paths("Choose: ", new_paths)
    return new_paths


def copy_to_clipboard(fp):
    print("Path copied to clipboard: %s" % fp)
    exit()
   

def check_if_final_dir(_dir):
    if os.path.isfile(_dir):
        copy_to_clipboard(_dir)

    paths = os.listdir(_dir)
    if len(paths) == 0:
        copy_to_clipboard(_dir)
    
    return paths

    
def choose_next_level(_dir):
    paths = check_if_final_dir(_dir)
    new_paths = show_available_dirs(paths, paths)
    while len(new_paths) != 1: 
        new_paths = show_available_dirs(new_paths, paths)
    
    return os.path.join(_dir, new_paths[0])


def main():
    _dir = sys.argv[1]
    while True:
        _dir = choose_next_level(_dir)


if __name__ == '__main__':
    main()
