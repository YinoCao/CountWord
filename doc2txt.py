# coding=utf-8
# _author_ YinoCao 1/31/2020
# 将docx 或者 doc格式转化为txt格式文件，并以utf-8格式保存

from win32com import client as wc
import os

_BASEDIR = os.path.dirname(__file__)

_FILE = os.path.join(_BASEDIR, 'sources')


def traslateType():
    files = os.listdir(_FILE)

    print(files)

    word = wc.Dispatch('word.Application')

    for file in files:

        if '~$' in file:
            continue
        if file[-5:] == '.docx':
            txtFileNameWithDir = os.path.join(_BASEDIR, 'files', file[:-5] + '.txt')
        elif file[-4:] == '.doc':
            txtFileNameWithDir = os.path.join(_BASEDIR, 'files', file[:-4] + '.txt')
        else:
            continue
        print("-----" + os.path.join(_FILE, file))
        doc = word.Documents.Open(os.path.join(_FILE, file))
        print(txtFileNameWithDir)
        doc.SaveAs(txtFileNameWithDir, 4)
        doc.Close()
        try:
            with open(txtFileNameWithDir, encoding='utf-8') as fp:
                fp.read()
        except:
            with open(txtFileNameWithDir) as fp1:
                with open('t.txt', 'w', encoding='utf-8') as fp2:
                    fp2.write(fp1.read())
            os.remove(txtFileNameWithDir)
            os.rename('t.txt', txtFileNameWithDir)
        finally:
            fp.close()

    word.Quit()


if __name__ == '__main__':
    traslateType()
