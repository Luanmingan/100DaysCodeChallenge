import os
import re
import fnmatch
from collections import Counter


def main():
    file_pattern = '../*/*.py'
    search_pattern = r'^import '

    py_files = gen_files(file_pattern)
    lines = gen_lines(py_files)
    grep_lines = gen_grep(search_pattern, lines)
    package_name = gen_count(grep_lines)

    for line in package_name:
        print(line)


def gen_files(pattern):
    """Generate files that match a given filename patter"""
    for root, dirs, files in os.walk(pattern.split('/')[0]):
        for filename in fnmatch.filter(files, pattern.split('/')[2]):
            yield os.path.join(root, filename)


def gen_lines(files):
    for file in files:
        with open(file, 'r') as fin:
            for line in fin.readlines():
                yield line


def gen_grep(pattern, lines):
    """docstring for gen_grep"""
    for line in lines:
        if re.search(pattern, line):
            yield line


def gen_count(lines):
    lines = list(lines)
    lines = [line.split()[1] for line in lines]
    c = Counter(lines)
    for package, count in c.most_common():
        yield '{} {}'.format(count, package)


if __name__ == '__main__':
    main()
