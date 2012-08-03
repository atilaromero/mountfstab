This tiny application mounts squash files that have dd images in it, 
and then mount them too.

It also install Upstart services to mount and umount these images.

With a few modifications, it can just mount dd images.

INSTALL
=======

Ubuntu
-------------
- Create a .deb:

    dpkg -b deb/ mountfstab.deb

- Install mountfstab.dev:

    sudo dpkg -i mountfstab.deb

- Go to /etc/mountfstab and create mountfstab.config. Suggestion of contents:

    SUBDIRS=/mnt/mysubdir
    GROUP=
    all: subdirs
    umount: umountsubdirs

- Link the Makefile to your images directory:

    ln -s /etc/mountfstab/Makefile ~/mydir/

Usage
=====
Suppose your directory has these files:
(Makefile is a link to /etc/mountfstab/Makefile)

    images.squash
    Makefile

Run make:

    make

It will create a file named mountfstab.config, which must be edited.
The GROUP variable must be defined.

Run make again. Now it will:

- create squash.list from existing '.squash' files (format: file mountpoint)

- create squash.fstab from squash.list

- mount squash.fstab

- create dd.list.example from existing '.dd' files (format: file mountpoint)

The dd.list.example must be editted and saved as 'dd.list':

    nano dd.list.example
    mv dd.list.example dd.list

Run make again:

    make

It will:

- create dd.fstab from dd.list

- mount dd.fstab

.list files
===========
The .list files are used just to create the .fstab files. They aren't 
needed if the .fstab already exists.

If the .fstab exists, the program won't read the .list files at all.

Umount
======

Run:

    make umount

It will umount the dd files and the squash ones.