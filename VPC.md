# VPC
![Alt text](Images/VPC.png)
### what is VPC
- Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

### What are the benefits ofa VPC 
- Greater control 
- enhanced security 
- cost saving 
- flexibility

### What are the benefitsd of a VPC for DevOps
- Security and compliance: private network environment for more secure and compliant deployments
- scalibility: easy to scale infatstructure based on demnd 
- collaboratio, provides a central and secure network for imporved colaboration and productivity. 

# Subnet/s
-A subnet, or subnetwork, is a network inside a network. Subnets make networks more efficient. Through subnetting, network traffic can travel a shorter distance without passing through unnecessary routers to reach its destination.

# Public and private subnets
- The instances in the public subnet can send outbound traffic directly to the internet, whereas the instances in the private subnet can't. Instead, the instances in the private subnet can access the internet by using a network address translation (NAT) gateway that resides in the public subnet.

# CIDR blocks
- CIDR (Classless Inter-Domain routing) block is a range of ip adresses that are used to define the network adress space for VPC or a subnet within the VPC
- an example of this is a CIDR block of 10.0.0.0/16 represents the IP address range from 10.0.0.0 to 10.0.255.255.

# Internet gateway
- A computer that sits between different networks or applications. The gateway converts information, data or other communications from one protocol or format to another. A router may perform some of the functions of a gateway. An Internet gateway can transfer communications between an enterprise network and the Internet.

# Route table/s
- A route table contains a set of rules, called routes, that determine where network traffic from your subnet or gateway is directed.


# How to set up vpc For app

## step 1
- go to VPC on aws 
- Create VPC
- when creating a VPC make it VPC only 
- name tag make it the usual nnaming conventio (name-tech201-VPC)
- ipv4 CIDR block 10.0.0.0/42
- now create the vpc
## Step 2
- Creatign an Internet gateway 
- just make a name with normal naming convention just add IG so that you know what you have done 
- Creat the IG
## step 3
- Creating a subnet 
- Select our vpc we have made and hit create subnet 
- once created go to associate subnet with VPC
## step 4
- Creating a route table (RT)
- find route tables on the left side and clikc create route table 
- name it normnally with RT 
- select our VPC again
 - then select your rout table and sleect subnet associates and make sure it is associated with your subnet and also make sure that routes is local with destination 0.0.0.0 so everyone can use them. 

