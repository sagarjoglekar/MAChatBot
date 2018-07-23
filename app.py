# from storage.data_models import connect_to_mongo, News
from endpoints.gdelt import *
from endpoints.gdelt import app

connect_to_mongo()
start_server()

print 'Starting to run the server'



if __name__ == '__main__':
  #global variables

  #run the server
  print "www"
  app.secret_key = 'super secret key'
  app.config['SESSION_TYPE'] = 'filesystem'
  app.run(host='0.0.0.0', port=5005, debug=True, threaded=True)