from bottle import Bottle, template
import json


app = Bottle()


@app.route('/main/<filename>')
def get_line(filename):
    with open('./static_files/{}.txt'.format(filename), 'r') as file:
        data = json.loads(file.read())
        lst = template('line', rows=data)
        main = template('main')
        return main + lst


@app.route('/miss/<filename>')
def get_line(filename):
    with open('./static_files/{}.txt'.format(filename), 'r') as file:
        data = json.loads(file.read())
        lst = template('missing_epg', rows=data)
        main = template('main')
        return main + lst


@app.route('/<filename>')
def get_gap(filename):
    with open('./static_files/{}.txt'.format(filename), 'r') as file:
        data = json.loads(file.read())
        lst = template('gaps_overlaps', rows=data)
        main = template('main')
        return main + lst


@app.route('/')
def main():
    return template('main')


if __name__ == '__main__':
    app.run(reloader=True, debug=False, host='0.0.0.0', port=8080)
