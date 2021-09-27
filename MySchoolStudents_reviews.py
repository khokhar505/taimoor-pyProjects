from flask import Flask

app =Flask(__name__)

@app.route("/")
def home():
    return '''
     <h1> District Public School & College, Kasur. <h2>
    
    <h3> teachers of 7th red <h4>

    <h5> sir muhammad saleem makki <h6>
    <h5> sir muhammad adil<h6>
    <h5> sir zeeshan <h6>
    <h5> sir dawood sikandar <h6>
    <h5> sir atif hammed <h6>
    <h5> sir zulifqar ali <h6>
    <h5> sir umer <h6>

    <h3> good students of 7th red <h4>
    
    <h5> umer rana <h6>
    <h5> ibrahim ahmad(don)
    <h5> salman akram <h6>
    <h5> noman ahamd <h6>
    <h5> taimoor mushtaq <h6>
    <h5> salman dameer <h6>
    <h5> shazaib asim <h6>
    <h5> sohail waseem <h6>

    <h3> medium students of 7th red <h4>

    <h5> ahmad maqsood <h6>
    <h5> azan bilal <h6>
    <h5> usman iftikhar  <h6>
    <h5> wasif mushtaq <h6>
    <h5> wasif zulfiqar <h6>
    <h5> muneeb hussain <h6>
    <h5> waleed  <h6>
    <h5> moeen-u-deen <h6>
    <h5> mirza <h6>

    <h3>  Shameless students of 7th red <h4>

    <h5> hussnain basharat <h6>
    <h5> abdurehman sohail (bhola record) <h6>
    <h5> hafiz ali haider  <h6>
    
    <h1> my first ever web page<h2>
    <h1> Just for fun!!! because i can't think about which should i make my webpage, so i wrote this. <h2>
    <h1> TAIMOOR MUSHTAQ <h2> '''

if __name__ == "__main__":
    app.run()


# (بے غیرت)