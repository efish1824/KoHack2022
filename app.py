from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from flask_bcrypt import Bcrypt
import pymysql, re, json, random

#Initializes flask and session variable system
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
bcrypt = Bcrypt()

#Initializes mysql
conn = pymysql.connect(host="us-cdbr-east-05.cleardb.net", user="beabcdf8916140", passwd="b7d8437a", database="heroku_2957a4813044253", autocommit=True)
cursor = conn.cursor(pymysql.cursors.DictCursor)

#Landing Page
@app.route('/')
def index():
    name = session.get("name")
    if not name:
        return render_template('index.html', Name="Not Logged In")
    return render_template('index.html', Name=f"Logged in as {name}")

#Reservation page
@app.route('/reserve', methods = ['GET', 'POST'])
def reserves():
    '''
    This function implements feature 1
    This function takes in your Korban request and stores it into a database
    You can view your total Korbanot at the bottom of the page
    '''
    if request.method == 'POST':
        #get the name, date, time and korban.
        Name = session.get('name')
        Username = session.get('uname')
        Date = request.form.get('date')
        FTime = request.form.get('time')
        Korban = request.form.get('kban')
        Time = FTime[:-2]
        Cycle = FTime[-2:]
        #check if the date/time status is taken or not
        conn.ping(reconnect=True)
        cursor.execute(f"SELECT * FROM `reservations` WHERE date = '{Date}' AND time = '{Time}'")
        taken = cursor.fetchone()

        #If the time slot is taken, prompt user to take a different date
        if taken:
            username = session.get('uname')
            return render_template('reservations.html', status = f'''<span style="color:red;">This slot is taken</span>''', CARDS = reserveHTML(username), Name = Name)

        #if the date isn't taken, change status to taken and add fields to database.
        conn.ping(reconnect=True)
        cursor.execute(f"INSERT INTO `reservations` (date, time, name, korban, username, cycle) VALUES ('{Date}', '{Time}','{Name}','{Korban}','{Username}', '{Cycle}')")
        
        #returning your succesful reservation
        username = session.get('uname')
        return render_template('reservations.html', Name = Name, status = f'''<span style="color:green">Not Taken</span>''', Date=Date, Time=Time, Korban=Korban, CARDS=reserveHTML(username))
    else:
        #if they are not logged in , redirect to sign up page.
        if not session.get('name'):
            return render_template('signup.html', status = '')
        #if they are logged in , display their current reservations if they have.
        username = session.get('uname')
        return render_template('reservations.html', Name = session.get('name'), status = f'''<span style="color:green">Not Taken</span>''', CARDS = reserveHTML(username))    

def reserveHTML(uname):
    '''
    Helps implement Feature 1
    Creates new HTML code that shows the user their currently reserved Korbanot
    @param uname the current user's username
    @return HTML code with all of the users reserved Korbanot
    '''
    #Gets current user reservations data
    conn.ping(reconnect=True)
    cursor.execute(f"SELECT * FROM `reservations` WHERE username = '{uname}' ORDER BY `date` asc, `cycle` asc, `time` asc")
    rows = cursor.fetchall()
    code = f''''''
    #Adds this data into HTML code
    for appt in rows:
        code += f'''
            <div class="card">
                <h4> Name: <span style="color:green">{appt['name']}</span> </h4>
                <h4> Date: <span style="color:green">{appt['date']}</span> </h4>
                <h4> Time: <span style="color:green">{str(appt['time'])[:-3]} {appt['cycle']}</span> </h4>
                <h4> Korban: <span style="color:green">{appt['korban']}</span> </h4>
            </div><br>
        '''
    return code

#Login page
@app.route('/login', methods=["GET", "POST"])
def login():
    '''
    This function logs you in based on a username and password
    which you have previously signed in with
    '''
    if request.method == 'POST':
        uname = request.form.get('name')
        pwd = request.form.get('pwd').encode('utf-8')
        #Checks whether the form was filled out
        if not uname or not pwd:
            return render_template('login.html', status='Please fill out all fields')
        #Checks whether the username and password were both correct
        conn.ping(reconnect=True)
        cursor.execute(f"SELECT * FROM `users` WHERE upper(username) = upper('{uname}')")
        if cursor.rowcount == 0:
            return render_template('login.html', status='Username or password is incorrect')
        row = cursor.fetchone()
        #Checks if the password is equivalent to the hash
        if not bcrypt.check_password_hash(row['pwd'].encode('utf-8'), pwd):
            return render_template('login.html', status='Username or password is incorrect')
        else:
            #Creates a new session variable with your name to keep you logged in
            session['name'] = row['name']
            session['uname'] = row['username']
            return redirect('https://maimomikdash.herokuapp.com/')
    #Checks whether you've been logged in or not
    if not session.get('name'):
        return render_template('login.html', status='')
    else:
        return redirect('https://maimomikdash.herokuapp.com/')

#Signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    This function signs you up for a new account in order to log into this website
    All account data is stored in the SQL table named `users`
    '''
    if request.method == 'POST':
        uname = request.form.get('uname')
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        #Checks whether the form was filled out
        if not uname or not name or not pwd:
            return render_template('signup.html', status = 'Please fill out all fields')
        #Checks whether the username is valid
        if len(uname) < 6 or len(uname) > 32:
            return render_template('signup.html', status = 'Usernames must be between 6 and 32 characters')
        #Checks whether the username is in use
        conn.ping(reconnect=True)
        cursor.execute(f"SELECT * FROM `users` WHERE upper(username) = upper('{uname}')")
        row = cursor.fetchone()
        if row:
            return render_template('signup.html', status = 'This username is already in use')        
        #Checks whether the password meets the following conditions: Contains one uppercase letter, one lowercase letter, one number, and is between 6-99 characters
        if not re.search('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{6,99}$', pwd):
            return render_template('signup.html', status = 'Passwords must be between 6 and 99 characters and contain at least one capital letter, one lowercase letter, and one number')
        #Hashes password
        newpwd = bcrypt.generate_password_hash(pwd).decode('utf-8')
        #Signs you up and signs you in with your new account
        conn.ping(reconnect=True)
        cursor.execute(f"INSERT INTO `users` (username, name, pwd) VALUES ('{uname}', '{name}', '{newpwd}');")
        session['name'] = name
        session['uname'] = uname
        return redirect('https://maimomikdash.herokuapp.com/')
    #Checks whether you are signed in
    if not session.get('name'):
        return render_template('signup.html', status = '')
    else:
        return redirect('https://maimomikdash.herokuapp.com/')
        
#Sanhedrin Request Page
@app.route('/sanhedrin', methods=['GET', 'POST'])
def sanhedrin():
    '''
    Implements feature 3
    This function allows you to submit a request to bring somebody to court at the Sanhedrin
    '''
    if request.method == 'POST':
        #Gets form data
        offender = request.form.get('offender')
        reason = request.form.get('reason')
        date = request.form.get('date')
        other = request.form.get('other')
        #Checks whether there is an available court date for you
        conn.ping(reconnect=True)
        cursor.execute(f"SELECT * FROM `sanhedrin` WHERE date = '{date}'")
        if cursor.rowcount >= 5:
            return render_template('sanhedrin.html', current = curAppts(), status = '<script>alert("There are no open slots today")</script>')
        #Stores the court date in the database `sanhedrin`
        conn.ping(reconnect=True)
        cursor.execute(f"INSERT INTO `sanhedrin` (date, name, username, offender, reason, other) VALUES ('{date}', '{session['name']}', '{session['uname']}', '{offender}', '{reason}', '{other}')")
        return redirect('https://maimomikdash.herokuapp.com/sanhedrin')
    #Checks whether you are logged in
    if not session.get('name'):
        return redirect('https://maimomikdash.herokuapp.com/login')
    else:
        return render_template('sanhedrin.html', current = curAppts(), status='')
        
def curAppts():
    '''
    Helps implement feature 3
    Creates HTML code that shows the end user their current court dates
    @return HTML code that shows the user their currently filed court dates
    '''
    conn.ping(reconnect=True)
    cursor.execute(f"SELECT * FROM `sanhedrin` WHERE username = '{session['uname']}' ORDER BY `date` asc")
    appts = cursor.fetchall()

    #Creates a table to store all of the court dates
    code = '''
    <table>
    <tr>
    <th>Offender</th>
    <th>Reason</th>
    <th>Date</th>
    <th>Comments</th>
    </tr>
    '''
    #Checks whether there are any court dates
    if not appts:
        return ''
    #Puts all court dates into the table
    for appt in appts:
        code += f'''
        <tr>
        <td>{appt['offender']}</td>
        <td>{appt['reason']}</td>
        <td>{appt['date']}</td>
        <td>{appt['other']}</td>
        </tr>
        '''
    code += '</table>'
    return code

#Kohen page
@app.route('/kohen', methods = ['GET', 'POST'])
def kohen():
    '''
    This function provides the main implementation for feature 2
    It checks whether you are logged in as a Kohen, and if you are, it allows you to view the daily jobs of the Kohanim and enter the raffle for the jobs
    '''
    if request.method == 'POST':
        #Logs you in as a Kohen
        uname = request.form.get('name')
        pwd = request.form.get('pwd').encode('utf-8')
        if not uname or not pwd:
            return render_template('kohen_login.html', status='Please fill out all fields')
        #Checks whether you are a Kohen
        conn.ping(reconnect=True)
        cursor.execute(f"SELECT * FROM `kohanim` WHERE upper(username) = upper('{uname}')")
        if cursor.rowcount == 0:
            return render_template('kohen_login.html', status='You are not a Kohen. Please use the standard login')
        row = cursor.fetchone()
        #Checks if the password is equivalent to the hash.
        if not bcrypt.check_password_hash(row['pwd'].encode('utf-8'), pwd):
            return render_template('kohen_login.html', status='You are not a Kohen. Please use the standard login')
        else:
            #Logs you in as a Kohen
            session['kname'] = row['name']
            session['uname'] = row['username']
            session['doneIncense'] = bool(row['doneIncense'])
            session['isKohenGadol'] = bool(row['gadol'])
            return redirect('https://maimomikdash.herokuapp.com/kohen')
    #Checks whether you are logged in as a Kohen or not
    if not session.get('kname'):
        return render_template('kohen_login.html', status = '')
    else:
        return render_template('kohen.html', jobs = kohenHTML(), status = '')

def kohenHTML():
    '''
    This function helps implement feature 2
    It creates a table with columns containing the different jobs, their recipients for today, and the option to enter the lottery for tomorrow
    If the user is the Kohen Gadol, it allows them to run the lottery
    @return HTML code with all of the Kohanim's current jobs and the ability for them to enter the lottery for these jobs
    '''
    #Creates table headers
    code = '''
    <table class="ktable">
    <tr>
    <th>Job</th>
    <th>Today's Worker</th>
    <th>Sign Up for Tomorrow's Lottery</th>
    </tr>
    '''
    conn.ping(reconnect=True)
    cursor.execute('SELECT * FROM `lottery`')
    rows = cursor.fetchall()

    #Creates table rows for every job and its lottery entry link
    for query in rows:
        code += f'''
        <tr>
        <td>{query['job']}</td>
        <td>{query['winner_today']}</td>
        <td><form action="https://maimomikdash.herokuapp.com/enterLottery" method="POST">
        <input type="hidden" name="job" value="{query['job']}">
        {'You have already offered the Ketoret' if (query['job'] == 'Offer the Ketoret' and session['doneIncense']) else '<input type="submit" value="Enter">'}
        </form>
        </tr>
        '''
    code += '</table>'
    if session['isKohenGadol']:
        code += '''
            <form action="https://maimomikdash.herokuapp.com/lottery" method="POST">
            <input type="submit" value="Run Lottery">
            </form>
        '''
    return code

#Kohen lottery enter
@app.route('/enterLottery', methods = ['POST'])
def enterLottery():
    '''
    This function helps implement feature 2
    This function signs a Kohen up for the specific lottery that they want
    '''
    job = request.form.get('job')
    conn.ping(reconnect=True)
    cursor.execute(f"SELECT * FROM `lottery` WHERE job = '{job}'")
    query = cursor.fetchone()
    #Retrieves existing JSON of lottery entries from the SQL table `lottery`
    names = list(json.loads(query['entries']))
    #Checks whether you've signed up for the specific lottery yet
    if session['uname'] in names:
        return render_template('kohen.html', jobs = kohenHTML(), status = '<script>alert("You have already entered the lottery for this job")</script>')
    #Adds you to the lottery so your name can get picked later
    names.append(session['uname'])
    conn.ping(reconnect=True)
    cursor.execute(f"UPDATE lottery SET entries = '{json.dumps(names)}' WHERE job = '{job}'")
    return render_template('kohen.html', jobs=kohenHTML(), status = "<script>alert('You have been entered!')</script>")

#Kohen lottery
@app.route('/lottery', methods=['POST'])
def lottery():
    '''
    This function helps implement feature 2
    This function allows the Kohen Gadol to execute the lottery
    '''
    conn.ping(reconnect=True)
    cursor.execute('SELECT * FROM `lottery`')
    query = cursor.fetchall()
    winners = []
    #Loops through different lotteries to pick winner
    for row in query:
        entries = list(json.loads(row['entries']))
        if not entries:
            return render_template('kohen.html', jobs=kohenHTML(), status = "<script>alert('At least one Kohen has to be entered into each lottery. To enter all Kohanim, go to https:////maimomikdash.herokuapp.com//simulateLottery')</script>")
        #Chooses random index of winner
        winningIndex = random.randint(0, len(entries) - 1)
        cursor.execute(f"SELECT * FROM `kohanim` WHERE username = '{entries[winningIndex]}'")
        winner = (cursor.fetchone())['name']
        #Makes sure that the winner hasn't won already on that day
        while winner in winners and len(entries) > 1:
            entries.pop(winningIndex)
            winningIndex = random.randint(0, len(entries) - 1)
            cursor.execute(f"SELECT * FROM `kohanim` WHERE username = '{entries[winningIndex]}'")
            winner = (cursor.fetchone())['name']
        winners.append(winner)    
        #Sets the person executing the job to the new winner
        cursor.execute(f"UPDATE lottery SET winner_today = '{winner}' WHERE job = '{row['job']}'")
        #Makes sure nobody does the Ketoret more than once (Yoma 2:4)
        if row['job'] == 'Offer the Ketoret':
            cursor.execute(f"UPDATE kohanim SET doneIncense = true WHERE username = '{entries[winningIndex]}'")
        conn.ping(reconnect=True)
        cursor.execute("UPDATE `lottery` SET `entries`='[]'")
    return redirect("https://maimomikdash.herokuapp.com/kohen")

#Kohen lottery simulation
@app.route('/simulateLottery')
def simulate():
    '''
    Adds all the Kohanim to the lottery
    For demonstration only
    '''
    #Gets all Kohanim in database
    conn.ping(reconnect=True)
    cursor.execute('SELECT * FROM `kohanim`')
    kohanim = cursor.fetchall()
    cursor.execute('SELECT * FROM `lottery`')
    lotteryjobs = cursor.fetchall()
    #Adds all Kohanim to each lottery
    for row in lotteryjobs:
        names = list(json.loads(row['entries']))
        for person in kohanim:
            if row['job'] == 'Offer the Ketoret' and bool(person['doneIncense']):
                continue
            if person['username'] not in names:
                names.append(person['username'])
        conn.ping(reconnect=True)
        cursor.execute(f"UPDATE lottery SET entries = '{json.dumps(names)}' WHERE job = '{row['job']}'")
    return redirect('https://maimomikdash.herokuapp.com/kohen')

#Logout
@app.route('/clear')
def clear():
    '''
    Clears your session variables
    For demonstration only
    '''
    session['name'] = ''
    session['kname'] = ''
    session['uname'] = ''
    session['doneIncense'] = ''
    session['isKohenGadol'] = ''
    return redirect('https://maimomikdash.herokuapp.com/')
    

#Help page
@app.route('/help')
def help():
    return render_template('help.html')

#App run
if __name__ == '__main__':
    app.run()
