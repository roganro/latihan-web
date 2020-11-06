from flask import (Flask, render_template, request, make_response, 
                    session ,url_for, redirect, flash)
app = Flask(__name__)
app.secret_key = '\x8e2m\xb4I\xe3\xf9\x90f\x9f4\tD\x99G\x04X\xdbF ?\x99D\xc7'

@app.route('/')
def hello():
    return 'Halo BosQu!!'

@app.route('/setting')
def show_setting():
    return 'Halo kamu di halaman setting!!'

@app.route('/profile/<username>')
def show_profile(username):
    return 'Halo kamu di halaman profile %s' % username

@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    return 'Halo kamu ada diblog nomer %d' % blog_id

@app.route('/jinja')
def jinja_html():
    return render_template('index.html')

@app.route('/jinja/profile/<namapengguna>')
def jinja_html_profile(namapengguna):
    return render_template('profile.html', nama=namapengguna)

@app.route('/jinja/login', methods=['GET', 'POST'])
def jinja_html_login():
    if request.method == 'POST':
        return 'Username ' + request.form['username'] + ' Telah Login'
    
    return render_template('login.html')

@app.route('/search')
def search():
    search = request.args.get('cari')
    video = request.args.get('video')
    if not search:
        return render_template('index.html')

    return 'hasil search adalah '+ search +' film '+ video

@app.route('/search-2')
def search2():
    search = request.args.get('cari')
    cari2 = request.args.get('dan')
    return render_template('index.html', search=search, cari=cari2)

@app.route('/login-cookie', methods=['GET', 'POST'])
def login_cookie():
    if request.method == 'POST':
        tanggapan = make_response('Username ' + request.form['username'] + ' Telah Login')
        tanggapan.set_cookie('id_user', request.form['username'])
        session['userid'] = request.form['username']
        return tanggapan

    if 'userid' in session:
        userid = session['userid']
        return redirect(url_for('jinja_html_profile', namapengguna=userid))
    
    return render_template('login.html')

@app.route('/login-flash', methods=['GET', 'POST'])
def login_flash():
    if request.method == 'POST':
        session['userid'] = request.form['username']
        flash('kamu berhasil login!', 'success')
        return redirect(url_for('jinja_html_profile', namapengguna=session['userid']))

    if 'userid' in session:
        userid = session['userid']
        return redirect(url_for('jinja_html_profile', namapengguna=userid))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('login_cookie'))

@app.route('/getcookie')
def getcookie():
    username = request.cookies.get('id_user')
    return 'Username yang tersimpan di cookie adalah ' + username