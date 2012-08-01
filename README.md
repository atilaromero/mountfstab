This tiny application mounts squash files that have HD images in it, 
and then mount them too.

INSTALL
=======

**Do not use "make"**

The Makefile is used **after** instalation, to mount the images.

Ubuntu/Debian
-------------
- Create a .deb:

    dpkg -b deb/ mountfstab.deb

- Install mountfstab.dev:

    sudo dpkg -i mountfstab.deb

- Copy Makefile to your images directory:

    cp Makefile ~/mydir/

Usage
=====
Suppose your directory has these files:

    images.squash
    Makefile

Run make once:

    make

It will:

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

Umount
======

Run:

    make umount

It will umount the dd files and the squash ones.