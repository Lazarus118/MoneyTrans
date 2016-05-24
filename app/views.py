from flask import render_template, flash, redirect, session, url_for, request, g, abort
from app import app
#*********************************#
import os
import stripe
#*********************************#
import twilio.twiml
from twilio.rest import TwilioRestClient


#***********************************************************************#
# // Fix for PythonAnywhere Server "Unhandled Expression" error //
#***********************************************************************#
from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP

Connection.set_proxy_info (
    "proxy.server",
    3128,
    proxy_type=PROXY_TYPE_HTTP )


# Find these values at https://twilio.com/user/account
account_sid = "AC18d08fbe124a82b91b3d5c16050bde97"
auth_token = "2b0f2c2a29c1337db6952a5fe1a2c43b"
client = TwilioRestClient(account_sid, auth_token)


# set the secret key.
app.secret_key = '\xa2\x944\x05\x11\x0b\x98?\xbd\x1a\xc5\xc5\xc4\xb1\xfc;\xe4\x8d\x98Z\x8b\xe3\xa9\xe9'


#***********************************************************************#
# // Twilio send //
#***********************************************************************#
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    amount = ""
    number = ""
    link = "http://bit.ly/1TgUFmf"
    resp = twilio.twiml.Response()
    body = request.values.get('Body')
    
    if "Sending " + amount +" to "+ number in body:
        resp.message("You've just sent \n " + amount +"  to  "+ number +", \nThank you for using BHyv Money Transfer \n'A simplier, easier way to move funds'\n\n....Full App coming soon....")
        message = client.messages.create(to=number, from_="+12242314065", 
        body="You've just received \n " + amount +"  from  "+ number +", \nThank you for using BHyv Money Transfer \n'A simplier, easier way to move funds'\n\n....Full App coming soon....")

    elif "Receiving  " + amount +"  from  " + number in body:
        resp.message("You've just received \n " + amount +"  from  "+ number +", \nThank you for using BHyv Money Transfer \n'A simplier, easier way to move funds'\n\n....Full App coming soon....")


    else:
        resp.message("<<< BHyv >>>\nYou said: **{0}**, \nwith just 2 simple steps you can Send or Receive funds from FRIENDS and FAMILY.\nTry by:\nSending " + amount +"  to  "+ number +"  or\nReceiving  " + amount +"  from  " + number +.format(body))
    
    return str(resp)

#***********************************************************************#
# // AUTH KEYS //
#***********************************************************************#
'''
stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}
stripe.api_key = stripe_keys['secret_key']
'''
stripe.api_key = "sk_test_R7pdJ0WZzf3kxQ2pfDTh7Vww"

#***********************************************************************#
# // 404 PAGE //
#***********************************************************************#
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404	

#***********************************************************************#
# // INDEX PAGE //
#***********************************************************************#
@app.route('/')
def index():
	#return render_template('index.html', key=stripe_keys['publishable_key'])
    return render_template('index.html', key="pk_test_kAnTf771XL7BkvdHit80WPV0")

#***********************************************************************#
# // CHARGE PAGE //
#***********************************************************************#	
@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

