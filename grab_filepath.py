#!/usr/bin/env python3
import sys
import os
from pprint import pprint


def subset_by_index(query_str, paths):
    index = query_str[1:].strip().replace('.', '')
    if not index.isnumeric():
        return compare_query_str_to_paths("Try again: ", paths)
    
    index = int(index)
    return [paths[index - 1]]


def subset_exact_match(query_str, paths):
    query_str = query_str[:-1]
    paths = [p for p in paths if query_str == p] 
    return paths


def subset_by_substr(query_str, paths):
    paths = [p for p in paths if query_str in p] 
    return paths


def compare_query_str_to_paths(msg, paths, query_str=None):
    if not query_str:
        query_str = input(msg)

    if query_str[0] == '>':
        return subset_by_index(query_str, paths)

    if query_str[-1] == '/':
        return subset_exact_match(query_str, paths)
    
    return subset_by_substr(query_str, paths) 


def display_paths_page(paths, page_count, total_paths, _dir):
    print()
    print("#-----------------------")
    m = page_count + len(paths) - 1
    print(f"Displaying {page_count} to {m} of {total_paths}")
    print()
    print(os.path.join(_dir, '...'))

    for i, p in enumerate(paths):
        i += page_count - 1
        print(f"> {i+1}. {p}")
    if len(paths) < total_paths:
        print('...')
    
    print()
    print("Type substring of dir to to make selection, ")
    print("or select by number by prefacing '>', e.g: > 1.")
    if total_paths > len(paths):
        return input("type PAGE for next page or make selection: ")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def display_paths(paths, _dir):
    if len(paths) > DIRS_PER_PAGE:
        pages = chunks(paths, DIRS_PER_PAGE)
        page_count = 1
        for i, p in enumerate(pages):
            query = display_paths_page(p, page_count, len(paths), _dir)
            if query != 'PAGE':
                return query
            page_count += len(p)
    
    else:
        display_paths_page(paths, 1, len(paths), _dir)


def show_available_dirs(new_paths, orig_paths, _dir):
    if len(new_paths) == 0: 
        new_paths = compare_query_str_to_paths("Try again: ", orig_paths)
    else: 
        query = display_paths(new_paths, _dir)
        new_paths = compare_query_str_to_paths("Choose: ", new_paths, query_str=query)
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
    new_paths = show_available_dirs(paths, paths, _dir)
    while len(new_paths) != 1: 
        new_paths = show_available_dirs(new_paths, paths, _dir)
    
    return os.path.join(_dir, new_paths[0])


def main(_dir):
    while True:
        _dir = choose_next_level(_dir)


DIRS_PER_PAGE = 30
if __name__ == '__main__':

    if len(sys.argv) not in [2, 3]:
        raise AssertionError("Must provide 'directory'")
    if len(sys.argv) == 3:
        DIRS_PER_PAGE = int(sys.argv[2])
    _dir = sys.argv[1]
    main(_dir)
