from flask import Flask, render_template, request
app = Flask(__name__) 
 
@app.route("/greet") 
def greet(): 
    username = request.args.get('name') 
    return render_template('index.html', name=username)
@app.route('/download')
def download():
    video = request.args.get('video')
    return render_template('download.html', video='Download')

 
if __name__ == "__main__": 
    app.run()
