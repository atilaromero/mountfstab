#!/usr/bin/python
import os,sys
import optparse

def main():
    p=optparse.OptionParser(usage="usage: %prog [options] <paths...>")
    p.add_option('--basemountdir',
                 default='')
    p.add_option('-o','--options',
                 default='ro,iocharset=utf8,gid=root,umask=0227')
    options, arguments = p.parse_args()
    if len(arguments)<1:
        p.error('path is not optional')
    for path in arguments:
        printparts(path,options.basemountdir,options.options)

def printparts(rpath,basemountdir,appendoptions):
  x=0
  y=0
  opj=os.path.join
  opd=os.path.dirname
  if not basemountdir:
      basemountdir=opd(rpath)
  for particao in readpartitiontable(rpath):
      if particao['size']=='204800':
          dest=opj(basemountdir,'Boot'+str(y))
          y+=1
      else:
          dest=opj(basemountdir,chr(ord('C')+x))
          x+=1
      options=','.join(['offset=%i'%particao['offset'],appendoptions])
      if rpath.endswith('.iso'):
          print rpath,dest,'iso9660',options.replace(',umask=0227','')
      else:
          print rpath,dest,'auto',options

def readpartitiontable(ddfilepath):
  particoes=[]
  for line in os.popen('sfdisk -d '+ ddfilepath).readlines()[3:]:
    virgs=line.rstrip().split(',')
    start=virgs[0].split('=')[-1].strip()
    size=virgs[1].split('=')[-1].strip()
    type=virgs[2].split('=')[-1].strip()
    if not(type=='f' or size=='0'):
      particoes.append({'offset':int(start)*512,
                        'size':size,
                        'type':type})
  if not particoes:
    tipoparticao='auto'
    particoes.append({'offset':0,
                      'size':0,
                      'type':tipoparticao})
  return particoes

if __name__=='__main__':
  main()

