import json
from datetime import datetime
from flask import request, Response
from Backendproj import app,db
from Backendproj.models import Payer,Transaction

@app.route("/")
@app.route("/home/")
def home():
    return "<h1>Test</h1>"


@app.route("/api/user/new_action", methods=['PUT'])
def new_action():
    form = request.json
    payer1 = str(form['payer'])
    points = int(form['points'])
    timestamp = str(form['timestamp'])
    payer = Payer.query.filter_by(name=payer1).first()
    transaction = Transaction(points=points, payer_id=payer.id,time_posted=timestamp)
    db.session.add(transaction)
    db.session.commit()
    return Response('{"message":"Transaction Successful"}',status=200)


#this route is used to for users to spend their points
@app.route("/api/user/spend", methods=['PUT'])
def spend_points():
    form = request.json
    payer1 = str(form['payer'])
    points = int(form['points'])
    payer=Payer.query.filter_by(name=payer1).first()
    if points<= payer.balance:
        transaction= Transaction(points=points,payer_id=payer.id)
        db.session.add(transaction)
        payer.balance=payer.balance-points
        db.session.commit()
        transjson=json.dumps(transaction)
        return transjson



#get the balance for all Users
@app.route("/api/user/balance", methods=['GET'])
def check_balance():
    payers=Payer.query.filter_by().all()
    balances=''
    for i in payers:
        a=json.dumps(i)
        balances=balances+a
    return balances

