#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='migrations', url='postgresql://root:root@localhost/aiohttpdemo', debug='False')
