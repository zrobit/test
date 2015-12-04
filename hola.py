import shutil
# import os
# print os.path.abspath(__file__).split('/')[1:-1]

# src = '/home/zrobit/projects/dirpic/media/temp/hola.jpeg'

# root, ext = os.path.splitext(src)

# _rename = False
# if not ext.islower():
#     ext = ext.lower()
#     _rename = True

# if ext == '.jpeg':
#     ext = '.jpg'
#     _rename = True

# if _rename:

#     os.rename(src, root+ext)
#     print 'renombro arcchivo: ' + root + ext

shutil.copy(
    '/home/zrobit/projects/test/uno.txt',
    '/home/zrobit/projects/test/dos/')
