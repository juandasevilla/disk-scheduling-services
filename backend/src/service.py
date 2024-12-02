from flask import Flask, request, jsonify

from flask_cors import CORS

from cscan import cscan
from scan import scan

app = Flask(__name__)
CORS(app)

from fcfs import fcfs
from sstf import sstf
from look import look
from clook import clook

@app.route("/", methods=['GET'])
def hello():
  return {
    "message": "use /usage to get information"
  }
  
@app.route("/usage", methods=['GET'])
def help():
  return {
    "message": "use FIFO, SSTF, SCAN or CSCAN algorithms",
    "instructions":{
      "endpoint":"/sched",
      "method": "POST",
      "payload":{
        "algorithm": "1:FCFS, 2:SSTF, 3:SCAN, 4:CSCAN, 5:LOOK, 6:CLOOK",
        "tracks": "number of cylinders",
        "arm": "initial position",
        "requests":"list of tracks"
      },
      "payload_example":{
        "algorithm": 1,
        "tracks":200,
        "arm": 96,
        "requests":[125,17,23,67,90,128,189,115,97]
      },
      "description": "This endpoint perform disk scheduling algorithms"
    }
  }
  
@app.route("/sched", methods=['POST'])
def sched():
  data = request.get_json()
  algorithm = data.get("algorithm")
  tracks = data.get("tracks")
  arm = data.get("arm")
  requests = data.get("requests")
  
  if algorithm == 1:  ## FCFS
    result = fcfs(arm, requests)
  elif algorithm == 2: ## SSTF
    result = sstf(arm, requests)
  elif algorithm == 3: #SCAN
    result = scan(arm, requests, tracks)
  elif algorithm == 4: #CSCAN
    result = cscan(arm, requests, tracks)
  elif algorithm == 5: #LOOK
    result = look(arm, requests, tracks)
  elif algorithm == 6: #CLOOK
    result = clook(arm, requests, tracks)
  else:
    return jsonify({"error": "Invalid algorithm"}), 400
  
  return jsonify({
    "result": result
  }), 200
    
  
  

  
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)

