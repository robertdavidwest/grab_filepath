import sys
import os
from pprint import pprint


def subset_by_index(query_str, paths):
    if not query_str[1:].isnumeric():
        return compare_query_str_to_paths("Try again: ", paths)
    
    index = int(query_str[1:].strip())
    return [paths[index - 1]]


def subset_exact_match(query_str, paths):
    query_str = query_str[:-1]
    paths = [p for p in paths if query_str == p] 
    return paths


def subset_by_substr(query_str, paths):
    paths = [p for p in paths if query_str in p] 
    return paths


def compare_query_str_to_paths(msg, paths):
    query_str = input(msg)
    if query_str[0] == '>':
        return subset_by_index(query_str, paths)

    if query_str[-1] == '/':
        return subset_exact_match(query_str, paths)
    
    return subset_by_substr(query_str, paths) 


def display_paths(paths):
    print("#-----------------------")
    for i, p in enumerate(paths):
        print(f"> {i+1}. {p}")


def show_available_dirs(new_paths, orig_paths):
    if len(new_paths) == 0: 
        new_paths = compare_query_str_to_paths("Try again: ", orig_paths)
    else: 
        display_paths(new_paths)
        new_paths = compare_query_str_to_paths("Choose: ", new_paths)
    return new_paths


def print_filepath(fp):
    print("/////////////////////////////////////////")
    print("/////////////////////////////////////////")
    print("Path to copy: ")
    print()
    print(fp)
    print()
    print("/////////////////////////////////////////")
    print("/////////////////////////////////////////")
    exit()
   

def check_if_final_dir(_dir):
    if os.path.isfile(_dir):
        print_filepath(_dir)

    paths = os.listdir(_dir)
    if len(paths) == 0:
        print_filepath(_dir)
    
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
