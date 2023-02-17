# AMI's
![Alt text](Images/AMI.png)

- AMI stands for Amazon Machine Image it is a supported and maintained image provided by AWS that provides the information required to launch an instance. It allows for companies to greatly reduce there costs as you will not have the instacne running th whole time you will just have it dormant until you need to run it again. 

# how to set up an AMI
### step 1 
- start your ec2 instacne of the app machine 
### step 2
- make sure that the app is working 
### step 3
- slect your app instacne and in actions find images and templates and select create and image 
### step 4
- all you need to do now is name the AMI and set the description so that any developer will know how to launch it so you will need to include what ports your are listening on. eg (3000, 22, 80)
### step 5
- you can now terminate your app instance as you have an image of it that you can launch whenever is needed. 
### step 6
- you will need to launch the instance after the ami is active and name it approprialty `name-group-db-ami` enter the key you have been using the entire time 
- select the exisitng security group you made when setting up an instance then launch the ami instance there. 