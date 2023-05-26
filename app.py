from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish/<name>/')
def wish(name):
    return f'hi hellow how are you{name}'
if __name__=='__main__':
    FAI.run(debug=True,port=5001,host='192.168.1.223')