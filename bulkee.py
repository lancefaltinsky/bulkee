import argparse
import os 
from os.path import isfile, getsize
from time import ctime

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    valid_tags = {
        '.ct': 'The time the file was created',
        '.mt': 'The last time the file was modified',
        '.sk': 'The file size in KB',
        '.sm': 'The file size in MB',
        '.sg': 'The file size in GB',
        '.t': 'The file type'
    }
    parser.add_argument('pattern', type=str, nargs='*',
                    help="""The pattern that each file rename should follow. This is NOT regular expression. You can either just use a normal string, but you may also include the special tags below. If using a normal string, be sure to not use the reserved special characters ($).
                    \nTags:""" + '\n'.join(valid_tags.keys()) + """\n
                    Example: A pattern of "Foo $t" will rename all EXE files in the directory to "Foo exe".
                    """)
    

    args = parser.parse_args()
    pattern = ' '.join(args.pattern)

    # we will add every file we touch here and .count the list for occurrences of potential file names, that way we can resolve same-name conflicts
    duplicate_file_names = []
    # iterate through files relative to the CWD
    for f in os.listdir('.'):
        if isfile(f) and f != "bulkee.py":
            file_type = f.split('.')[-1]
            new_name = ""
            new_name = pattern.replace('.ct', ctime(os.path.getctime(f)))
            new_name = new_name.replace('.mt', ctime(os.path.getmtime(f)))
            new_name = new_name.replace('.sk', str(getsize(f)/1024))
            new_name = new_name.replace('.sm', str(getsize(f)/1048576))
            new_name = new_name.replace('.sg', str(getsize(f)/1073741824))
            new_name = new_name.replace('.t', file_type)
            duplicate_file_names.append(new_name)
            duplicate_count = duplicate_file_names.count(new_name)
            if duplicate_count > 1:
                new_name += f' ({duplicate_count-1})'
            new_path = new_name + '.' + file_type
            try:
                os.rename(f, new_path)
            except FileExistsError:
                print(new_path, "already exists, so this file could not be renamed")
            #file_names.append()
