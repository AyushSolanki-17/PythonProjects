import os

def createIfNotExist(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)

def moveFiles(foldername,files):
    for f in files:
        os.replace(f,f'{foldername}/{f}')

def arrangeFiles(current_dir_files,subdirectory_name,file_extensions):
    exts = [x.split('.')[1] for x in current_dir_files]
    if any(file in exts for file in file_extensions):
        imgs = [f for f in current_dir_files if os.path.splitext(f)[1][1:].lower() in file_extensions]
        createIfNotExist(subdirectory_name)
        moveFiles(subdirectory_name,imgs)

files = os.listdir()
files.remove('main.py')
files = [fl for fl in files if os.path.isfile(fl)]
img_extensions = ['png', 'jpg', 'jpeg', 'svg']
js_extensions = ['js',]
css_extensions = ['css',]
docs_extensions = ['pdf','docx','xlsx']
py_extensions = ['py']

arrangeFiles(files,'img',img_extensions)
arrangeFiles(files,'docs',docs_extensions)
arrangeFiles(files,'css',css_extensions)
arrangeFiles(files,'js',js_extensions)
arrangeFiles(files,'py',py_extensions)