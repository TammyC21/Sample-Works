'''
This is the Course4111 project for Taimin Chen &Zixi Tian at CU
All right reserved
'''
import os
  # accessible as a variable in index.html:
from sqlalchemy import *
import psycopg2
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, url_for
import pandas as pd
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

# Modify these with your own credentials you received from TA!
DATABASE_USERNAME = "xxxx"
DATABASE_PASSWRD = "xxxx"
DATABASE_HOST = "xx.xx.xx.xx" #
DATABASEURI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWRD}@{DATABASE_HOST}/project1"

#
engine = create_engine(DATABASEURI)
#

@app.before_request
def before_request():
	"""
	This function is run at the beginning of every web request 
	(every time you enter an address in the web browser).
	We use it to setup a database connection that can be used throughout the request.

	The variable g is globally accessible.
	""" 
	try:
		g.conn = engine.connect()
	except:
		print("uh oh, problem connecting to database")
		import traceback; traceback.print_exc()
		g.conn = None

@app.teardown_request
def teardown_request(exception):
	"""
	At the end of the web request, this makes sure to close the database connection.
	If you don't, the database could run out of memory!
	"""
	try:
		g.conn.close()
	except Exception as e:
		pass

#Website design and query function
@app.route('/')
def table():
        print(request.args)
        return render_template("table.html")

@app.route('/policy', methods = ['GET', 'POST'])
def policy():    
    context = None
    result2 = None
	#print(request.args)
    if request.method == 'GET':
        result = 'No action yet'
        select_query = "SELECT * from policy"
        cursor = g.conn.execute(text(select_query))
        data = []
        for result in cursor:
            data.append(result)
        context = pd.DataFrame(data, columns = ['policy_no', 'insured_id', 'insured_name', 'policyholder_id',\
                                                'policyholder_name', 'product_id', 'channel_id', 'strat_date',\
                                                    'operate_date', 'end_date', 'status', 'premium'])
    result = 'No action yet'
    if request.method == 'POST':
        value_id = request.form['value_id']
        select = request.form.get('selected_one')
        if select == 'policy_no':
            try:
                sql2 = "SELECT * from policy WHERE policy_no = :policy_no;"
                result2 = g.conn.execute(text(sql2), {'policy_no':value_id}) 
                data = []
                for result in result2:
                    data.append(result)
                if data == []:
                    result = 'No result found!'
                else:
                    result = 'Successfully search!'
                context = pd.DataFrame(data, columns = ['policy_no', 'insured_id', 'insured_name', 'policyholder_id',\
                                                        'policyholder_name', 'product_id', 'channel_id', 'strat_date',\
                                                            'operate_date', 'end_date', 'status', 'premium'])
            except error as e:
                pass
        if select == 'product_id':
            try:
                sql2 = "SELECT * from policy WHERE product_id = :product_id;"
                result2 = g.conn.execute(text(sql2), {'product_id':value_id}) 
                data = []
                for result in result2:
                    data.append(result)
                if data == []:
                    result = 'No result found!'
                else:
                    result = 'Successfully search!'
                context = pd.DataFrame(data, columns = ['policy_no', 'insured_id', 'insured_name', 'policyholder_id',\
                                                        'policyholder_name', 'product_id', 'channel_id', 'strat_date',\
                                                            'operate_date', 'end_date', 'status', 'premium'])
            except error as e:
                pass
        if select == 'start_date':
            try:
                sql2 = "SELECT * from policy WHERE EXTRACT(YEAR FROM start_date) = :start_date;"
                result2 = g.conn.execute(text(sql2), {'start_date':value_id}) 
                data = []
                for result in result2:
                    data.append(result)
                if data == []:
                    result = 'No result found!'
                else:
                    result = 'Successfully search!'
                context = pd.DataFrame(data, columns = ['policy_no', 'insured_id', 'insured_name', 'policyholder_id',\
                                                        'policyholder_name', 'product_id', 'channel_id', 'strat_date',\
                                                            'operate_date', 'end_date', 'status', 'premium'])
            except error as e:
                pass
        if select == 'end_date':
            try:
                sql2 = "SELECT * from policy WHERE EXTRACT(YEAR FROM end_date) = :end_date;"
                result2 = g.conn.execute(text(sql2), {'end_date':value_id}) 
                data = []
                for result in result2:
                    data.append(result)
                if data == []:
                    result = 'No result found!'
                else:
                    result = 'Successfully search!'
                context = pd.DataFrame(data, columns = ['policy_no', 'insured_id', 'insured_name', 'policyholder_id',\
                                                        'policyholder_name', 'product_id', 'channel_id', 'strat_date',\
                                                            'operate_date', 'end_date', 'status', 'premium'])
            except error as e:
                pass
        if select == 'status':
            try:
                sql2 = "SELECT * from policy WHERE status = :status;"
                result2 = g.conn.execute(text(sql2), {'status':value_id}) 
                data = []
                for result in result2:
                    data.append(result)
                if data == []:
                    result = 'No result found!'
                else:
                    result = 'Successfully search!'
                context = pd.DataFrame(data, columns = ['policy_no', 'insured_id', 'insured_name', 'policyholder_id',\
                                                        'policyholder_name', 'product_id', 'channel_id', 'strat_date',\
                                                            'operate_date', 'end_date', 'status', 'premium'])
            except error as e:
                pass
    try:
        g.conn.close()
    except Exception as e:
        pass
    return render_template('policy.html',tables=[context.to_html(classes='table table-striped')], result = result)
#

@app.route('/policyholder', methods = ['GET', 'POST'])
def policyholder():    
    context = None
    result2 = None
	#print(request.args)
    if request.method == 'GET':
        result = 'No action yet'
        select_query = "SELECT * from policyholder"
        cursor = g.conn.execute(text(select_query))
        data = []
        for result in cursor:
            data.append(result)
        context = pd.DataFrame(data, columns = ['policyholder_id', 'policyholder_name', 'birthdate', 'gender', 'age'])
    result = 'No action yet'
    if request.method == 'POST':
        policyholder_id = request.form['policyholder_id']
        try:
            sql2 = "SELECT * from policyholder WHERE policyholder_id = :policyholder_id;"
            result2 = g.conn.execute(text(sql2), {'policyholder_id':policyholder_id}) 
            data = []
            for result in result2:
                data.append(result)
            if data == []:
                result = 'No result found!'
            else:
                result = 'Successfully search!'
            context = pd.DataFrame(data, columns = ['policyholder_id', 'policyholder_name', 'birthdate', 'gender', 'age'])
        except error as e:
            pass
    try:
        g.conn.close()
    except Exception as e:
        pass
    return render_template('policyholder.html',tables=[context.to_html(classes='table table-striped')], result = result)
#

@app.route('/insured', methods = ['GET', 'POST'])
def insured():    
    context = None
    result2 = None
	#print(request.args)
    if request.method == 'GET':
        result = 'No action yet'
        select_query = "SELECT * from insured"
        cursor = g.conn.execute(text(select_query))
        data = []
        for result in cursor:
            data.append(result)
        context = pd.DataFrame(data, columns = ['insured_id', 'insured_name', 'birthdate', 'gender', 'state', 'age'])
    result = 'No action yet'
    if request.method == 'POST':
        insured_id = request.form['insured_id']
        try:
            sql2 = "SELECT * from insured WHERE insured_id = :insured_id;"
            result2 = g.conn.execute(text(sql2), {'insured_id':insured_id}) 
            data = []
            for result in result2:
                data.append(result)
            if data == []:
                result = 'No result found!'
            else:
                result = 'Successfully search!'
            context = pd.DataFrame(data, columns = ['insured_id', 'insured_name', 'birthdate', 'gender', 'state', 'age'])
        except error as e:
            pass
    try:
        g.conn.close()
    except Exception as e:
        pass
    return render_template('insured.html',tables=[context.to_html(classes='table table-striped')], result = result)
#

@app.route('/channel', methods = ['GET', 'POST'])
def channel():    
    context = None
    result2 = None
	#print(request.args)
    if request.method == 'GET':
        result = 'No action yet'
        select_query = "SELECT * from channel"
        cursor = g.conn.execute(text(select_query))
        data = []
        for result in cursor:
            data.append(result)
        context = pd.DataFrame(data, columns = ['Channel_id','Channel_name','Channel_type','Channel_grade'])
    result = 'No action yet'
    if request.method == 'POST':
        channel_id = request.form['channel_id']
        try:
            sql2 = "SELECT * from channel WHERE channel_id = :channel_id;"
            result2 = g.conn.execute(text(sql2), {'channel_id':channel_id}) 
            data = []
            for result in result2:
                data.append(result)
            if data == []:
                result = 'No result found!'
            else:
                result = 'Successfully search!'
            context = pd.DataFrame(data, columns = ['Channel_id','Channel_name','Channel_type','Channel_grade'])
        except error as e:
            pass
    try:
        g.conn.close()
    except Exception as e:
        pass
    return render_template('channel.html',tables=[context.to_html(classes='table table-striped')], result = result)
#

@app.route('/product', methods = ['GET', 'POST'])
def product():    
    context = None
    result2 = None
	#print(request.args)
    if request.method == 'GET':
        result = 'No action yet'
        select_query = "SELECT * from product"
        cursor = g.conn.execute(text(select_query))
        data = []
        for result in cursor:
            data.append(result)
        context = pd.DataFrame(data, columns = ['Product_Id','Product_name','Baseline_premium','Multiplier_Up','Multiplier_Low', 'Classcode','Classname'])
    result = 'No action yet'
    if request.method == 'POST':
        product_id = request.form['product_id']
        try:
            sql2 = "SELECT * from product WHERE product_id = :product_id;"
            result2 = g.conn.execute(text(sql2), {'product_id':product_id}) 
            data = []
            for result in result2:
                data.append(result)
            if data == []:
                result = 'No result found!'
            else:
                result = 'Successfully search!'
            context = pd.DataFrame(data, columns = ['Product_Id','Product_name','Baseline_premium','Multiplier_Up','Multiplier_Low', 'Classcode','Classname'])
        except error as e:
            pass
    try:
        g.conn.close()
    except Exception as e:
        pass
    return render_template('product.html',tables=[context.to_html(classes='table table-striped')], result = result)
#

@app.route('/contract', methods = ['GET', 'POST'])
def contract():    
    context = None
    result2 = None
	#print(request.args)
    if request.method == 'GET':
        result = 'No action yet'
        select_query = "SELECT * from contract"
        cursor = g.conn.execute(text(select_query))
        data = []
        for result in cursor:
            data.append(result)
        context = pd.DataFrame(data, columns = ['Contract_id','Contract_name','Coverage','Net_premium'])
    result = 'No action yet'
    if request.method == 'POST':
        contract_id = request.form['contract_id']
        try:
            sql2 = "SELECT * from contract WHERE contract_id = :contract_id;"
            result2 = g.conn.execute(text(sql2), {'contract_id':contract_id}) 
            data = []
            for result in result2:
                data.append(result)
            if data == []:
                result = 'No result found!'
            else:
                result = 'Successfully search!'
            context = pd.DataFrame(data, columns = ['Contract_id','Contract_name','Coverage','Net_premium'])
        except error as e:
            pass
    try:
        g.conn.close()
    except Exception as e:
        pass
    return render_template('contract.html',tables=[context.to_html(classes='table table-striped')], result = result)
#

@app.route('/cover', methods = ['GET', 'POST'])
def cover():    
    context = None
    result2 = None
	#print(request.args)
    if request.method == 'GET':
        result = 'No action yet'
        select_query = "SELECT * from cover"
        cursor = g.conn.execute(text(select_query))
        data = []
        for result in cursor:
            data.append(result)
        context = pd.DataFrame(data, columns = ['Cover_id','Product_id','Contract_id'])
    result = 'No action yet'
    if request.method == 'POST':
        value_id = request.form['value_id']
        select = request.form.get('selected_one')
        if select == 'cover_id':
            try:
                sql2 = "SELECT * from cover WHERE cover_id = :cover_id;"
                result2 = g.conn.execute(text(sql2), {'cover_id':value_id}) 
                data = []
                for result in result2:
                    data.append(result)
                if data == []:
                    result = 'No result found!'
                else:
                    result = 'Successfully search!'
                context = pd.DataFrame(data, columns = ['Cover_id','Product_id','Contract_id'])
            except error as e:
                pass
        if select == 'product_id':
            try:
                sql2 = "SELECT * from cover WHERE product_id = :product_id;"
                result2 = g.conn.execute(text(sql2), {'product_id':value_id}) 
                data = []
                for result in result2:
                    data.append(result)
                if data == []:
                    result = 'No result found!'
                else:
                    result = 'Successfully search!'
                context = pd.DataFrame(data, columns = ['Cover_id','Product_id','Contract_id'])
            except error as e:
                pass
    try:
        g.conn.close()
    except Exception as e:
        pass
    return render_template('cover.html',tables=[context.to_html(classes='table table-striped')], result = result)
#


# Adding new data to the database
@app.route('/add_policy', methods=['GET', 'POST'])
def add_policy():
	if request.method == 'POST':
		policy_no = request.form['policy_no']
		insured_id = request.form['insured_id']
		insured_name = request.form['insured_name']
		policyholder_id = request.form['policyholder_id']
		policyholder_name = request.form['policyholder_name']
		product_id = request.form['product_id']
		channel_id = request.form['channel_id']
		start_date = request.form['start_date']
		operate_date = request.form['operate_date']
		end_date = request.form['end_date']
		status = request.form['status']
		premium = request.form['premium']
		query = """
		INSERT INTO policy (policy_no, insured_id, insured_name, policyholder_id, policyholder_name, product_id, channel_id, start_date, operate_date, end_date, status, premium)
		VALUES (:policy_no, :insured_id, :insured_name, :policyholder_id, :policyholder_name, :product_id, :channel_id, :start_date, :operate_date, :end_date, :status, :premium)
		"""
		params = {
		'policy_no': policy_no,
	    'insured_id': insured_id,
	    'insured_name': insured_name,
	    'policyholder_id': policyholder_id,
	    'policyholder_name': policyholder_name,
	    'product_id': product_id,
	    'channel_id': channel_id,
	    'start_date': start_date,
	    'operate_date': operate_date,
	    'end_date': end_date,
	    'status': status,
	    'premium': premium
	    }
		try:
			g.conn.execute(text(query), params)
			g.conn.commit()
			message = "Add successfully!"
			g.conn.close()
		except Exception as e:
			message = "Failed to add!"
		return render_template('add_policy.html', message=message)
	else:
		return render_template('add_policy.html')

@app.route('/add_insured', methods=['GET', 'POST'])
def add_insured():
	if request.method == 'POST':
		insured_id = request.form['insured_id']
		insured_name = request.form['insured_name']
		birthdate = request.form['birthdate']
		gender = request.form['gender']
		state = request.form['state']
		age = request.form['age']
		query = """
		INSERT INTO insured (insured_id, insured_name, birthdate, gender, state, age)
		VALUES (:insured_id, :insured_name, :birthdate, :gender, :state, :age)
		"""
		params = {
        	'insured_id': insured_id,
        	'insured_name': insured_name,
        	'birthdate': birthdate,
        	'gender': gender,
        	'state': state,
        	'age': age,
    		}
		try:
			g.conn.execute(text(query), params)
			g.conn.commit()
			message = "Add successfully!"
			g.conn.close()
		except Exception as e:
			message = "Failed to add!"

		return render_template('add_insured.html', message=message)
	else:
		return render_template('add_insured.html')
     
@app.route('/add_policyholder', methods=['GET', 'POST'])
def add_policyholder():
	if request.method == 'POST':
		policyholder_id = request.form['policyholder_id']
		policyholder_name = request.form['policyholder_name']
		birthdate = request.form['birthdate']
		gender = request.form['gender']
		age = request.form['age']
		query = """
		INSERT INTO policyholder (policyholder_id, policyholder_name,birthdate, gender, age)
		VALUES (:policyholder_id, :policyholder_name, :birthdate, :gender,:age)
		"""
		params = {
        	'policyholder_id': policyholder_id,
        	'policyholder_name': policyholder_name,
        	'birthdate': birthdate,
        	'gender': gender,
        	'age': age,
    		}
		try:
			g.conn.execute(text(query), params)
			g.conn.commit()
			message = "Add successfully!"
			g.conn.close()
		except Exception as e:
			message = "Failed to add!"

		return render_template('add_policyholder.html', message=message)
	else:
		return render_template('add_policyholder.html')

@app.route('/add_channel', methods=['GET', 'POST'])
def add_channel():
	if request.method == 'POST':
		channel_id = request.form['channel_id']
		channel_name = request.form['channel_name']
		channel_type = request.form['channel_type']
		channel_grade = request.form['channel_grade']
		query = """
		INSERT INTO channel (channel_id, channel_name, channel_type, channel_grade)
		VALUES (:channel_id, :channel_name, :channel_type, :channel_grade)
		"""
		params = {
		'channel_id': channel_id,
        	'channel_name': channel_name,
        	'channel_type': channel_type,
        	'channel_grade': channel_grade,
    		}
		try:
			g.conn.execute(text(query), params)
			g.conn.commit()
			message = "Add successfully!"
			g.conn.close()
		except Exception as e:
			message = "Failed to add!"

		return render_template('add_channel.html', message=message)
	else:
		return render_template('add_channel.html')

@app.route('/add_contract', methods=['GET', 'POST'])
def add_contract():
	if request.method == 'POST':
		contract_id = request.form['contract_id']
		contract_name = request.form['contract_name']
		coverage = request.form['coverage']
		net_premium = request.form['net_premium']
		query = """
		INSERT INTO contract (contract_id, contract_name, coverage, net_premium)
		VALUES (:contract_id, :contract_name, :coverage, :net_premium)
		"""
		params = {
		'contract_id': contract_id,
        	'contract_name': contract_name,
        	'coverage': coverage,
        	'net_premium': net_premium,
        	#'product_id': product_id,
    		}
		try:
			g.conn.execute(text(query), params)
			g.conn.commit()
			message = "Add successfully!"
			g.conn.close()
		except Exception as e:
			message = "Failed to add!"

		return render_template('add_contract.html', message=message)
		return render_template('add_contract.html')
	else:
		return render_template('add_contract.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
	if request.method == 'POST':
		product_id = request.form['product_id']
		product_name = request.form['product_name']
		baseline_premium = request.form['baseline_premium']
		multiplier_up = request.form['multiplier_up']
		multiplier_low = request.form['multiplier_low']
		classcode = request.form['classcode']
		classname = request.form['classname']
		query = """
		INSERT INTO product (product_id, product_name, baseline_premium, multiplier_up, multiplier_low, classcode, classname)
		VALUES (:product_id, :product_name, :baseline_premium, :multiplier_up, :multiplier_low, :classcode, :classname)
		"""
		params = {
		'product_id': product_id,
        	'product_name': product_name,
        	'baseline_premium': baseline_premium,
        	'multiplier_up': multiplier_up,
        	'multiplier_low': multiplier_low,
        	'classcode': classcode,
        	'classname': classname,
    		}
		try:
			g.conn.execute(text(query), params)
			g.conn.commit()
			message = "Add successfully!"
			g.conn.close()
		except Exception as e:
			message = "Failed to add!"

		return render_template('add_product.html', message=message)
	else:
		return render_template('add_product.html')

@app.route('/add_cover', methods=['GET', 'POST'])
def add_cover():
	if request.method == 'POST':
		cover_id = request.form['cover_id']
		product_id = request.form['product_id']
		contract_id = request.form['contract_id']
		query = """
		INSERT INTO cover (cover_id, product_id, contract_id)
		VALUES (:cover_id, :product_id, :contract_id)
		"""
		params = {
		'cover_id': cover_id,
        	'product_id': product_id,
        	'contract_id': contract_id,
        	#'product_id': product_id,
    		}
		try:
			g.conn.execute(text(query), params)
			g.conn.commit()
			message = "Add successfully!"
			g.conn.close()
			return render_template('add_cover.html', message=message)
			pass
		except Exception as e:
			message = "Failed to add!"
			return render_template('add_cover.html', message=message)
	else:
		return render_template('add_cover.html')

#Delete Function
@app.route('/delete_policy', methods=['GET', 'POST'])
def delete_policy():
    if request.method == 'POST':
        policy_no = request.form['policy_no']
        query = "DELETE FROM policy WHERE policy_no = :policy_no"
        params = {'policy_no': policy_no}
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = f"Policy with policy number {policy_no} has been successfully deleted."
            g.conn.close()
        except Exception as e:
            message = " Failed to delete"

        return render_template('delete_policy.html', message=message)
    else:
        return render_template('delete_policy.html')

@app.route('/delete_insured', methods=['GET', 'POST'])
def delete_insured():
    if request.method == 'POST':
        insured_id = request.form['insured_id']
        query = "DELETE FROM insured WHERE insured_id = :insured_id"
        params = {'insured_id': insured_id}
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = f"Insured with insured_id {insured_id} has been successfully deleted."
            g.conn.close()
        except Exception as e:
            message = " Failed to delete"

        return render_template('delete_insured.html', message=message)
    else:
        return render_template('delete_insured.html')

@app.route('/delete_policyholder', methods=['GET', 'POST'])
def delete_policyholder():
    if request.method == 'POST':
        policyholder_id = request.form['policyholder_id']
        query = "DELETE FROM policyholder WHERE policyholder_id = :policyholder_id"
        params = {'policyholder_id': policyholder_id}
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = f"Policyholder with policyholder_id {policyholder_id} has been successfully deleted."
            g.conn.close()
        except Exception as e:
            message = " Failed to delete"

        return render_template('delete_policyholder.html', message=message)
    else:
        return render_template('delete_policyholder.html')

@app.route('/delete_product', methods=['GET', 'POST'])
def delete_product():
    if request.method == 'POST':
        product_id = request.form['product_id']
        query = "DELETE FROM product WHERE product_id = :product_id"
        params = {'product_id': product_id}
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = f"Product with product_id {product_id} has been successfully deleted."
            g.conn.close()
        except Exception as e:
            message = " Failed to delete"
        return render_template('delete_product.html', message=message)
    else:
        return render_template('delete_product.html')

@app.route('/delete_channel', methods=['GET', 'POST'])
def delete_channel():
    if request.method == 'POST':
        channel_id = request.form['channel_id']
        query = "DELETE FROM channel WHERE channel_id = :channel_id"
        params = {'channel_id': channel_id}
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = f"Chanenl with channel_id {channel_id} has been successfully deleted."
            g.conn.close()
        except Exception as e:
            message = " Failed to delete"
        return render_template('delete_channel.html', message=message)
    else:
        return render_template('delete_channel.html')

@app.route('/delete_contract', methods=['GET', 'POST'])
def delete_contract():
    if request.method == 'POST':
        contract_id = request.form['contract_id']
        query = "DELETE FROM contract WHERE contract_id = :contract_id"
        params = {'contract_id': contract_id}
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = f"Contract with contract_id {contract_id} has been successfully deleted."
            g.conn.close()
        except Exception as e:
            message = " Failed to delete"
        return render_template('delete_contract.html', message=message)
    else:
        return render_template('delete_contract.html')

@app.route('/delete_cover', methods=['GET', 'POST'])
def delete_cover():
    if request.method == 'POST':
        cover_id = request.form['cover_id']
        query = "DELETE FROM cover WHERE cover_id = :cover_id"
        params = {'cover_id': cover_id}
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            g.conn.close()
            message = f"Cover with cover_id {cover_id} has been successfully deleted."
            pass
        except Exception as e:
            message = 'Failed to delete'
            pass
        return render_template('delete_cover.html', message=message)
    else:
        return render_template('delete_cover.html')


#Update Function
@app.route('/update_policy', methods=['GET', 'POST'])
def update_policy():
    if request.method == 'POST':
        policy_no = request.form['policy_no']
        insured_id = request.form['insured_id']
        insured_name = request.form['insured_name']
        policyholder_id = request.form['policyholder_id']
        policyholder_name = request.form['policyholder_name']
        product_id = request.form['product_id']
        channel_id = request.form['channel_id']
        start_date = request.form['start_date']
        operate_date = request.form['operate_date']
        end_date = request.form['end_date']
        status = request.form['status']
        premium = request.form['premium']

        query = """
            UPDATE policy SET 
                insured_id = :insured_id, 
                insured_name = :insured_name, 
                policyholder_id = :policyholder_id, 
                policyholder_name = :policyholder_name, 
                product_id = :product_id, 
                channel_id = :channel_id, 
                start_date = :start_date, 
                operate_date = :operate_date,
                end_date = :end_date, 
                status = :status, 
                premium = :premium
            WHERE policy_no = :policy_no
        """
        params = {
            'policy_no': policy_no,
            'insured_id': insured_id,
            'insured_name': insured_name,
            'policyholder_id': policyholder_id,
            'policyholder_name': policyholder_name,
            'product_id': product_id,
            'channel_id': channel_id,
            'start_date': start_date,
            'operate_date': operate_date,
            'end_date': end_date,
            'status': status,
            'premium': premium
        }
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = "Update successful!"
            g.conn.close()
        except Exception as e:
            message = "Failed to update."

        return render_template('update_policy.html', message=message)
    else:
        return render_template('update_policy.html')

@app.route('/update_insured', methods=['GET', 'POST'])
def update_insured():
    if request.method == 'POST':
        insured_id = request.form['insured_id']
        insured_name = request.form['insured_name']
        birthdate = request.form['birthdate']
        gender = request.form['gender']
        state = request.form['state']
        age = request.form['age']

        query = """
            UPDATE insured SET
                insured_name = :insured_name,
                birthdate = :birthdate,
                gender = :gender,
                state = :state,
                age = :age
            WHERE insured_id = :insured_id
        """
        params = {
            'insured_id': insured_id,
            'insured_name': insured_name,
            'birthdate': birthdate,
            'gender': gender,
            'state': state,
            'age': age
        }
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = "Update successful!"
            g.conn.close()
        except Exception as e:
            message = "Failed to update."

        return render_template('update_insured.html', message=message)
    else:
        return render_template('update_insured.html')

@app.route('/update_policyholder', methods=['GET', 'POST'])
def update_policyholder():
    if request.method == 'POST':
        policyholder_id = request.form['policyholder_id']
        policyholder_name = request.form['policyholder_name']
        birthdate = request.form['birthdate']
        gender = request.form['gender']
        age = request.form['age']

        query = """
            UPDATE policyholder SET
                policyholder_name = :policyholder_name,
                birthdate = :birthdate,
                gender = :gender,
                age = :age
            WHERE policyholder_id = :policyholder_id
        """
        params = {
            'policyholder_id': policyholder_id,
            'policyholder_name': policyholder_name,
            'birthdate': birthdate,
            'gender': gender,
            'age': age
        }
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = "Update successful!"
            g.conn.close()
        except Exception as e:
            message = "Failed to update."

        return render_template('update_policyholder.html', message=message)
    else:
        return render_template('update_policyholder.html')

@app.route('/update_channel', methods=['GET', 'POST'])
def update_channel():
    if request.method == 'POST':
        channel_id = request.form['channel_id']
        channel_name = request.form['channel_name']
        channel_type = request.form['channel_type']
        channel_grade = request.form['channel_grade']

        query = """
            UPDATE channel SET
            channel_name = :channel_name,
            channel_type = :channel_type,
            channel_grade = channel_grade,
            WHERE channel_id = :channel_id
        """
        params = {
            'channel_id' :channel_id,
            'channel_name' :channel_name,
            'channel_type' :channel_type,
            'channel_grade' :channel_id,

        }
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = "Update successful!"
            g.conn.close()
        except Exception as e:
            message = "Failed to update."

        return render_template('update_channel.html', message=message)
    else:
        return render_template('update_channel.html')

@app.route('/update_product', methods=['GET', 'POST'])
def update_product():
    if request.method == 'POST':
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        baseline_premium = request.form['baseline_premium']
        multiplier_up = request.form['multiplier_up']
        multiplier_low = request.form['multiplier_low']
        classcode = request.form['classcode']
        classname = request.form['classname']

        query = """
            UPDATE product SET
                product_name = :product_name,
                baseline_premium = :baseline_premium,
                multiplier_up = :multiplier_up,
                multiplier_low = :multiplier_low,
                classcode = :classcode,
                classname = :classname
            WHERE product_id = :product_id
        """
        params = {
            'product_id': product_id,
            'product_name': product_name,
            'baseline_premium': baseline_premium,
            'multiplier_up': multiplier_up,
            'multiplier_low': multiplier_low,
            'classcode': classcode,
            'classname': classname
        }
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = "Update successful!"
            g.conn.close()
        except Exception as e:
            message = "Failed to update."

        return render_template('update_product.html', message=message)
    else:
        return render_template('update_product.html')

@app.route('/update_contract', methods=['GET', 'POST'])
def update_contract():
    if request.method == 'POST':
        contract_id = request.form['contract_id']
        contract_name = request.form['contract_name']
        coverage = request.form['coverage']
        net_premium = request.form['net_premium']
        query = """
        UPDATE contract SET 
            contract_name = :contract_name,
            coverage = :coverage,
            net_premium = :net_premium
        WHERE contract_id = :contract_id
        """
        params = {
            'contract_id': contract_id,
            'contract_name' :contract_name,
            'coverage' :coverage,
            'net_premium' :net_premium
        }
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = "Update successful!"
            g.conn.close()
        except Exception as e:
            message = "Failed to update."

        return render_template('update_contract.html', message=message)
    else:
        return render_template('update_contract.html')

@app.route('/update_cover', methods=['GET', 'POST'])
def update_cover():
    if request.method == 'POST':
        cover_id = request.form['cover_id']
        product_id = request.form['product_id']
        contract_id = request.form['contract_id']
        query = """
        UPDATE cover
        SET product_id = :product_id, contract_id = :contract_id
        WHERE cover_id = :cover_id
        """
        params = {
            'cover_id': cover_id,
            'product_id': product_id,
            'contract_id': contract_id,
        }
        try:
            g.conn.execute(text(query), params)
            g.conn.commit()
            message = "Update successful!"
            g.conn.close()
        except Exception as e:
            message = "Failed to update."

        return render_template('update_cover.html', message=message)
    else:
        return render_template('update_cover.html')

#This is a Machine Learning based underwriting evaluation system
### UDS
@app.route('/evaluate', methods = ['GET', 'POST'])
def evaluate():    
    result = None
    score = None
    comment = None
	#print(request.args)
    if request.method == 'GET':
        result = 'No action yet, please enter something'
    result = 'No action yet'
    if request.method == 'POST':
        #
        age = request.form['age']
        try:
            age = int(age)
        except Exception as e:
            result = 'illegal input,check your input'
            return render_template('evaluate.html', result = result, score = score, comment = comment)
            pass
        premium = request.form['premium']
        try:
            premium = float(premium)
        except Exception as e:
            result = 'illegal input,check your input'
            return render_template('evaluate.html', result = result, score = score, comment = comment)
            pass
        gender = request.form.get('gender')
        if gender == 'Male':
            gender = 1 
        else:
            gender = 0
        #
        select_query = "SELECT p.policy_no, i.age, i.gender, p.premium, p.status\
                         FROM policy as p LEFT JOIN insured as i\
                         ON p.insured_id = i.insured_id\
                         WHERE p.status in ('Due', 'Paid')"
        try:
            cursor = g.conn.execute(text(select_query))
        except Exception as e:
            result = 'Input incorrect, check and try again!!!'
            pass
        data = []
        for result in cursor:
            data.append(result)
        df = pd.DataFrame(data, columns = ['policy_no','age','sex', 'premium', 'status'])
        df['sex'] = df['sex'].apply(lambda x: 1 if x == 'male' else 0)
        df['status'] = df['status'].apply(lambda x: 1 if x == 'Due' else 0)
        df = df.dropna()
        try:
            import numpy as np
            from sklearn.linear_model import LogisticRegression
            #Logistic_regression Fit in
            X_train = df[['sex', 'age', 'premium']]
            y_train = df['status']
            lr = LogisticRegression()
            lr.fit(X_train, y_train)
            #Calculate the Prob of new data point
            x_new = [gender, age, premium]
            x_new = np.array(x_new).reshape(1, -1)
            probabilities = lr.predict_proba(x_new)
            score = 100*probabilities[0][0].round(4)
            result = 'Input data successfully analysed, result as follow~'
            if score >= 0.8:
                comment = 'Highly suggested to underwrite'
            elif score >=0.4:
                comment = 'Consider before underwrite, require more information'
            else:
                comment = 'Not suggest to underwrite'
        except Exception as e:
            result = 'Input incorrect, check and try again'
            pass
    try:
        g.conn.close()
    except Exception as e:
        pass
    return render_template('evaluate.html', result = result, score = score, comment = comment)
#

#To run the front-end Flask
@app.route('/login')
def login():
	abort(401)
	this_is_never_executed()


if __name__ == "__main__":
	import click

	@click.command()
	@click.option('--debug', is_flag=True)
	@click.option('--threaded', is_flag=True)
	@click.argument('HOST', default='0.0.0.0')
	@click.argument('PORT', default=8111, type=int)
	def run(debug, threaded, host, port):
		"""
		This function handles command line parameters.
		Run the server using:

			python server.py

		Show the help text using:

			python server.py --help

		"""

		HOST, PORT = host, port
		print("running on %s:%d" % (HOST, PORT))
		app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

run()
