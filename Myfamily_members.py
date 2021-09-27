from flask import Flask

app =Flask(__name__)

@app.route("/")
def home():
    return '''<h1> KHOKHAR HOUSE <h2> 
    
    <h3> 1. HEAD OF KHOKHAR HOUSE <h4>

    <h5> MUSHTAQ AHMAD <h6>
    <h5> ASIFA WAZIR <h6>

    <h3>2. MENS OF KHOKHAR HOUSE <h4>

    <h5> ASIM MUSHTAQ <h6>
    <h5> QASIM MUSHTAQ <h6>
    <h5> NAZIM MUSHTAQ <h6>
    <h5> ASGHAR HUSSAIN <h6>

    <h3> 3. WOMENS OF KHOKHARS HOUSE <h4>    
    
    <h5> NAEMMA AKHTER <h6>
    <h5> SHUMAILA SADAF <h6>
    <h5> ANJUM MUSHTAQ <h6>
    <h5> FAIZA AKBER <h6>
    
    <h3> 4. SONS OF KHOKHAR HOUSE<h4>

    <h5> MUGHEES-UR-REHMAN or MUGHEES ALI <h6>
    <h5> AHMAD MUSHTAQ <h6>
    <h5> ASFAND MUSHTAQ <h6>
    <h5> TAIMOOR MUSHTAQ <h6>
    <h5> SARMAD MUSHTAQ <h6>
    
    <h3> 5. DAUGHTER OF KHOKHAR HOUSE <h4>
    
    <h5> HAMNA MUSHTAQ <h6>
    <h5> ALINA MUSHTAQ <h6>'''


if __name__ == "__main__":
    app.run()