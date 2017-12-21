from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'swapneel'}
    return '''
<html>
    <head>
       <title>Web Application Page</title>
    </head>
    <body>
      <h1>Hello, ''' + user['username'] + ''' </h1>
    </body>
</html>'''
