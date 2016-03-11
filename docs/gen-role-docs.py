#!/usr/bin/python

'''This script will find README.md documents in the given tree and assemble
them into a final document with a table of contents.'''

import os
import sys
import tempfile
import argparse

def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument('--before-toc')
    p.add_argument('--after-toc')
    p.add_argument('--footer')
    p.add_argument('roledir')

    return p.parse_args()

def main():
    args = parse_args()

    prefix = '../playbooks/roles'

    docfd = tempfile.TemporaryFile()
    toc = []

    args.roledir = os.path.normpath(args.roledir)
    for dirpath, dirnames, filenames in os.walk(args.roledir):
        if 'README.md' in filenames:
            role = dirpath[len(args.roledir)+1:]
            level = len(role.split('/'))

            toc.append(role)

            docfd.write('{mark} <a id="{role}">{role}</a>\n\n'.format(
                mark='#' * (level+1),
                role=role))

            with open(os.path.join(dirpath, 'README.md')) as fd:
                docfd.write(fd.read())

            docfd.write('\n')

    if args.before_toc:
        with open(args.before_toc) as fd:
            sys.stdout.write(fd.read())

    for role in toc:
        sys.stdout.write('- [{role}](#{role})\n'.format(
            role=role))
    sys.stdout.write('\n')

    if args.after_toc:
        with open(args.after_toc) as fd:
            sys.stdout.write(fd.read())

    docfd.seek(0)
    sys.stdout.write(docfd.read())

    if args.footer:
        with open(args.footer) as fd:
            sys.stdout.write(fd.read())


if __name__ == '__main__':
    main()
