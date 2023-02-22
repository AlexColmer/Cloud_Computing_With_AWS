# VPC
![Alt text](Images/aws_vpc.jpeg)
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


