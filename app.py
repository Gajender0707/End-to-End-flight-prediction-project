from flask import Flask,redirect,render_template,request,url_for
import sklearn
from datetime import datetime
import pandas as pd
import pickle
import sklearn

app=Flask(__name__)

##load the model

model=pickle.load(open("Flight_price_model.pkl","rb"))

@app.route("/")
def homepage():
    return render_template("index.html")

# @app.route("/price/<int:p>")
# def price_prediction(p):
#       return render_template("test.html",value=p)


@app.route("/predict",methods=["POST","GET"])
def prediction():
    if request.method=="POST":

        airline=request.form['Airline']
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Other_Airline = 0

        if(airline=="Jet_Airways"):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Other_Airline = 0

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Other_Airline = 0

        elif (airline=='Air_India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Other_Airline = 0
             
            
        elif (airline=='Multiple_carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Other_Airline = 0
            
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Other_Airline = 0
            
        elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Other_Airline = 0

        elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Other_Airline = 0


        elif (airline=='Other_Airline'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Other_Airline = 1
        else:
            return "Sorry Please Select the Right Option "
        
        air_dict={"Jet_Airways":Jet_Airways,"IndiGo":IndiGo,"Air_India":Air_India,"Multiple Carriers":Multiple_carriers,"SpiceJet":SpiceJet,"Vistara":Vistara,"GoAir":GoAir,"Other Airline":Other_Airline}
        

    ## Feilds Fetch of source
        source=request.form["Source"]
        s_Chennai = 0
        s_Delhi = 0
        s_Mumbai = 0
        s_Banglore = 0
        s_Kolkata = 0
        if source=="Chennai":
                 s_Chennai = 1
                 s_Delhi = 0
                 s_Mumbai = 0
                 s_Banglore = 0
                 s_Kolkata = 0


        elif source=="Delhi":
                 s_Chennai = 0
                 s_Delhi = 1
                 s_Mumbai = 0
                 s_Banglore = 0
                 s_Kolkata = 0

        elif source=="Mumbai":
                 s_Chennai = 0
                 s_Delhi = 0
                 s_Mumbai = 1
                 s_Banglore = 0
                 s_Kolkata = 0

        elif source=="Banglore":
                 s_Chennai = 0
                 s_Delhi = 0
                 s_Mumbai = 0
                 s_Banglore = 1
                 s_Kolkata = 0

        elif source=="Kolkata":
                 s_Chennai = 0
                 s_Delhi = 0
                 s_Mumbai = 0
                 s_Banglore = 0
                 s_Kolkata = 1
        else:
             return "Please select the Valid Source"
        source_dict={"Delhi":s_Delhi,"Mumbai":s_Mumbai,"Kolkata":s_Kolkata,"Banglore":s_Banglore,"Chennai":s_Chennai}
        
        ##Destination
        destination=request.form["Destination"]
        d_Hyderabad = 0
        d_Delhi = 0
        d_Chochin = 0
        d_Banglore = 0
        d_Kolkata = 0
        if destination=="Hyderabad":
                 d_Hyderabad = 1
                 d_Delhi = 0
                 d_Chochin = 0
                 d_Banglore = 0
                 d_Kolkata = 0


        elif destination=="Delhi":
                 d_Hyderabad = 0
                 d_Delhi = 1
                 d_Chochin = 0
                 d_Banglore = 0
                 d_Kolkata = 0

        elif destination=="Chochin":
                 d_Hyderabad = 0
                 d_Delhi = 0
                 d_Chochin = 1
                 d_Banglore = 0
                 d_Kolkata = 0

        elif destination=="Banglore":
                 d_Hyderabad = 0
                 d_Delhi = 0
                 d_Chochin = 0
                 d_Banglore = 1
                 d_Kolkata = 0

        elif destination=="Kolkata":
                 d_Hyderabad = 0
                 d_Delhi = 0
                 d_Chochin = 0
                 d_Banglore = 0
                 d_Kolkata = 1
        
        else:
             
             return "Please select the Valid Source"
        
        destination_dict={"Delhi":d_Delhi,"Chochin":d_Chochin,"Kolkata":d_Kolkata,"Banglore":d_Banglore,"Hyderabad":d_Hyderabad}

        #this is for the Total_stops

        total_stops=request.form["Total_Stops"]
        stops=0
        if total_stops=="Non_Stop":
              stops=0
        
        elif total_stops=="1_Stop":
              stops=1

        elif total_stops=="2_Stops":
              stops=2

        elif total_stops=="3_Stops":
              stops=3

        elif total_stops=="4_Stops":
              stops=4
        else:
              return "Please Select the Valid Stops"
        stops_dict={"Stops: ":stops}

        # return f"You select the {air_dict} Airline and you source is {source_dict} and to you going to {destination_dict} with {stops_dict} Stops..."

        ##Journey date

        departure_time=request.form["Departure_Time"]
        journey_day=int(pd.to_datetime(departure_time).day)
        journey_month=int(pd.to_datetime(departure_time).month)

        ## Departure Hour and minute
        departure_hour=int(pd.to_datetime(departure_time).hour)
        departure_minute=int(pd.to_datetime(departure_time).minute)


        ##arrival hour and minute
        arrival_time=request.form["Arrival_Time"]
        arrival_hour=int(pd.to_datetime(arrival_time).hour)
        arrival_minute=int(pd.to_datetime(arrival_time).minute)

        ##Calculation Duration hour and Duration minute

        duration_hour=abs(arrival_hour-departure_hour)
        duration_minute=abs(arrival_minute-departure_minute)



        d={"Total Number of Stops":total_stops, "Journey Day":journey_day," Jouney Month":journey_month,"Arrival Hour":arrival_hour,
           "Arrival Minute":arrival_minute,"Departure Hour":departure_hour,"Departure Minute":departure_minute,
           "Duration Hour":duration_hour,
           "Durtion minute":duration_minute,
           "Airline You select":air_dict,
           "Source Airport":source_dict,
           "Destination Airport":destination_dict
           
           }
        

        output=model.predict([[stops,journey_day,journey_month,arrival_hour,arrival_minute,departure_hour,departure_minute,
                       duration_hour,duration_minute,Jet_Airways,IndiGo,Air_India,Multiple_carriers,Other_Airline,SpiceJet,Vistara,
                       s_Delhi,s_Kolkata ,d_Chochin,d_Delhi,d_Hyderabad,d_Kolkata]])
        
        
        # return str(round(output[0],2))
        pred=round(output[0],2)
        return render_template("show.html",p=pred)
    # return render_template("index.html")


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)