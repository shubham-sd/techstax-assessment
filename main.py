from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhookcall", methods=["POST"])
def webhook():
    # 1. Get the Event Type
    event_type = request.headers.get('X-GitHub-Event')
    
    # 2. Get the Data
    data = request.json

    # --- PUSH EVENT ---
    if event_type == "push":
        author = data['pusher']['name'] 
        to_branch = data['ref'].split('/')[-1] 
        timestamp = data['head_commit']['timestamp']

        print(f"--- PUSH DETECTED ---")
        print(f"{author} pushed to {to_branch} on {timestamp}")

    # --- PULL REQUEST / MERGE EVENT ---
    elif event_type == "pull_request":
        action = data.get('action') 
        
        # Common data for both PR and Merge
        author = data['pull_request']['user']['login']
        from_branch = data['pull_request']['head']['ref']
        to_branch = data['pull_request']['base']['ref']
        timestamp = data['pull_request']['created_at']

        # CASE 1: MERGE (Closed + Merged=True)
        if action == "closed" and data['pull_request'].get('merged') == True:
            print(f"--- MERGE DETECTED ---")
            print(f"{author} merged branch {from_branch} to {to_branch} on {timestamp}")
        
        # CASE 2: PR OPENED
        elif action == "opened":
            print(f"--- PR OPENED ---")
            print(f"{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}")

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)