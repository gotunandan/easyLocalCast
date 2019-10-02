import os
import sys
from operator import itemgetter
from flask import Flask, render_template
from flask import send_file

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
            temp_path = path.split('/')
            my_set = set(my_path.split('/'))
            newPath = '/'.join([x for x in temp_path if x not in my_set])
            modPath = 'gotunandan'.join(newPath.split('/'))
            tree['children'].append(
                dict(
                    name=u'{0}'.format(name), 
                    newPath=modPath,
                    myKey=my_key,
                    )
            )
    tree['children'] = sorted(tree['children'], key=itemgetter('name'))
    return tree

def processFile(fileName):
    if fileName.endswith(b'.webm') or fileName.endswith(b'.webp') or fileName.endswith(b'.jpeg'):
        minus4 = fileName[-5:]
    else:
        minus4 = fileName[-4:]
    print("minus 4 is {0}".format(minus4))
    if minus4.decode().lower() in ['.wmv', '.m4v', '.mp4', '.avi', '.mov', '.mkv', '.flv', '.webm',]:
        print("video file is --- {0}".format(fileName))
        return render_template(
                'play.html',
                fileName=fileName,
                my_host=my_host,
                my_port=my_port,
        )
    elif minus4.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp']:
        print("image file is --- {0}".format(fileName))
        return render_template(
                'image.html',
                fileName=fileName,
                my_host=my_host,
                my_port=my_port,
        )
    else:
        fileName = fileName.decode()
        print(u"directory name is --- {0}".format(fileName))
        return render_template(u'dirtree.html', tree=make_tree(my_path + u'/' + u'{0}'.format(fileName)))


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
    dir_name = u'/'.join(dir_name.split('gotunandan'))
    return processFile(dir_name.encode("utf-8"))

@app.route('/<vid_name>')
def vid_name(vid_name):
    vid_name = '/'.join(vid_name.split('gotunandan'))
    ret_val = u"{0}/{1}".format(my_path, vid_name)
    print("retval is --- {0}".format(ret_val.encode("utf-8")))
    return ret_val


if __name__ == "__main__":
    app.run(host=my_host, port=my_port, debug=True)


