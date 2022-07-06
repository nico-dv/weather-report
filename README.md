# weather-report

A small script that runs everyday on AWS using EventBridge, Lambda and SNS. 

This solution can support any similar tasks that needs to run periodically.


How to deploy it to AWS:
  
It can be entirely build using IaC tools, but since it's quite basic I'm using the AWS Console. 
  
  
1. Lambda

Create the function and upload your code. Make sure you add the relevant dependecies. You can find more on how to deploy at https://docs.aws.amazon.com/lambda/latest/dg/welcome.html 

    
2. EventBridge

This is our trigger. It can run the function at any given time. When you create the new rule make sure the Schedule expression* is implemented properly. 
For example if you want your function to run every minute you would use something like this: cron(0/1 * * * ? *)
More about Cron expressions here: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html

  
3. SNS

There are multiple ways to do this. For convenience I've decided to create my topic plus subscription and have AWS Lambda publish to it. 


Room for improvement:

1. Automate the infrastructe provisioning
2. Build a CI/CD pipeline
