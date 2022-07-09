import requests
import os
import boto3


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat" : 51.509865,
    "lon" :  -0.118092,
    "appid" : os.getenv('api_key'),
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
sns = boto3.client('sns')



def lambda_handler(event, context):   
    for index in range(1,13):    
        id = weather_data["hourly"][index]["weather"][0]["id"]
       
        if id < 700:
            sns.publish(TopicArn=topic_arn, 
            Message="Today is going to rain. :( Don't forget to bring an umbrella!", 
            Subject="Daily Weather Report")
             
        else:
            sns.publish(TopicArn=os.getenv('topic_arn'), 
            Message="Today's weather is going to be sunny! Enjoy =D", 
            Subject="Daily Weather Report")
                 
                      
   
   
