import os
import sys
from flask import Flask, render_template

def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try:
        lst = os.listdir(path)
    except OSError as errObj:
        print(errObj)
    else:
        for name in lst:
            fn = os.path.join(path, name)
            path = u'{0}'.format(path)
            #print("before split path is --- {0}".format(path))
            temp_path = path.split('/')
            #print("after split path is --- {0}".format(path))
            my_set = set(my_path.split('/'))
            #print("set is --- {0}".format(my_set))
            newPath = '/'.join([x for x in temp_path if x not in my_set])
            #print("new path is --- {0}".format(newPath))
            modPath = 'gotunandan'.join(newPath.split('/'))
            tree['children'].append(dict(
                name=u'{0}'.format(name), 
                newPath=modPath,
                myKey=my_key,
            ))
    return tree

def processFile(fileName):
    minus4 = fileName[-5:] if fileName.endswith('.webm') else  fileName[-4:]
    print("minus 4 is {0}".format(minus4))
    if minus4 in ['.wmv', '.mp4', '.avi', '.mov', '.mkv', '.webm', ]:
        print("video file is --- {0}".format(fileName))
        return render_template(
                'play.html',
                #fileName='gotunandan'.join(fileName.split('/')),
                #fileName=my_path + '/' + fileName,
                fileName=fileName,
                my_host=my_host,
                my_port=my_port,
        )
    else:
        print("directory name is --- {0}".format(fileName))
        return render_template('dirtree.html', tree=make_tree(my_path + '/' + fileName))




#path = os.path.expanduser(u'~')
#path = ("/media/drive2/AAA-Movies/ZZ-A-Team/")
#my_path = (u'/media/drive2/AAA-Movies')
my_path = u'{0}'.format(sys.argv[1])
my_host = sys.argv[2]
my_port = int(sys.argv[3])
print("MY PATH IS --- {0}".format(my_path))
my_key = 'gotunandan'
app = Flask(__name__)

@app.route('/')
def dirtree():
    return render_template('dirtree.html', tree=make_tree(my_path))

@app.route('/dir/<dir_name>')
def dir_name(dir_name):
    dir_name = '/'.join(dir_name.split('gotunandan'))
    return processFile("{0}".format(dir_name))

@app.route('/<vid_name>')
def vid_name(vid_name):
    vid_name = '/'.join(vid_name.split('gotunandan'))
    ret_val = "{0}/{1}".format(my_path, vid_name)
    print("retval is --- {0}".format(ret_val))
    return ret_val


if __name__ == "__main__":
    app.run(host=my_host, port=my_port, debug=True)


