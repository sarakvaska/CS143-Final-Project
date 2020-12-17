# An Algorithm in Pursuit of Network Fairness: Bandwidth Allocation at Home in a Zoom World
CS143 Final Project by Sara Kvaska, Serena Davis, Gustavo Coutinho and Jenna Moustafa

## How to Run Our Code
Step 1: Set up the mininet environment and ensure that you can connect from the host PC to the guest VM via SSH.

Step 2: Once the environment is set up, open a terminal and run: ssh -X [user]@[Guest IP Here]. 
  - Replace [user] with the correct user name for your VM image (in our case, mininet). 
  - Replace [Guest IP Here] with the IP you noted from the VM (in our case, 192.168.56.101). 
  - When prompted, enter the password for the VM image (in our case, mininet). 
  
 Step 3: Start up an X terminal using '$ xterm' and a new terminal window should appear. 
  - If you get a 'xterm: DISPLAY is not set error', try running ssh -Y [user]@[Guest IP Here] instead of using -X.
  
 Step 4: Inside the xterm terminal, cd into '~/pox/pox/misc' directory, then run the command 'sudo fuser -k 6633/tcp'. This is to kill any controllers still running on the system. (When first running this command, there should not be any controllers running but we'll run the command just in case.)
  - Then, run 'sudo mn -c' to cleanup the configuration. We want to cleanup before running the topology. 
  
 Step 5: After completing steps 1-4 above, we are ready to run our topology. Make sure the topo.py file is inside the ~/pox/pox/misc directory, then run the command 'sudo mn --custom topo.py --topo custom'. A topology of 7 hosts, 7 switches, and 1 controller should be created, and the CLI should be started. 
 
 Step 6: Run the command 'xterm h1 h2 h3 h4 h5 h6 h7'. This will open separate terminals for all 7 hosts. 
  - Inside the 'Node: h1' terminal, run 'python user.py 1'. This will run the user.py file, and takes in 3 arguments: 
  destination IP, scrPort and app_type. Our destination IP is always 10.0.0.2, because host 2 will send the packets to their intended host (hosts 3 through 7, depending on the app type). Our srcPort is always 1234, and the app_type argument is a number ranging from 1 through 5. 
  - Inside the 'Node: h2' terminal, run 'python intermediary.py'.  
  - Inside the 'Node: h3', 'Node: h4', 'Node: h5', 'Node: h6', and 'Node: h7' terminals, run 'python application.py'. 

Step 7: Now that the topology is set up and we can run our code to send and receive packets for each host, we can run the commands by different app type.
  - The command 'python user.py 1' sends app_type 1 (which is Zoom), to h2. Host 2 then forwards this to h3, which prints out the app type it receives, the host address it received it from, and the app type name. It sends a packet with app type 'User App' back to h1 once this information is received from h2.
  - The command 'python user.py 2' sends app_type 2 (which is Skype), to h2. Host 2 then forwards this to h4, which (as above) prints out the information it's received, and sends a packet with app type 'User App' back to h1.
  - The command 'python user.py 3' does the same as above, except app_type 3 is Email. Host 2 forwards this to h5, and the same steps are repeated.
  - The command 'python user.py 4' does the same as above, except app_type 4 is Netflix. Host 2 forwards this to h6, and the same steps are repeated.
  - The command 'python user.py 5' does the same as above, except app_type 5 is Hulu. Host 2 forwards this to h7, and the same steps are repeated. 
  
## Methodology

This section explains how our topology was created and what our code is doing. 

Our code was written with the intention of providing a better way of allocating bandwidth, one that's dependent on the applications people in the home are using. In our implementation, we use time delays to replicate bandwidth allocation. This slows down the time between when packets are sent so that higher priority packets are sent faster than lower priority packets and packets to/from applications with higher bandwidth requirements are sent faster than packets to/from applications with lower bandwidth requirements.

To get started, we created a topology consisting of 7 hosts, 7 switches, and 1 controller. We assign hosts different tasks: the first host (h1) sends a packet for each type of application (Zoom, Skype, Email, Netflix or Hulu) to host 2 (h2), which then decides where to send the information based on the application type. We have 5 hosts for each application type: host 3 is for Zoom; host 4 is for Skype; host 5 is for Email; host 6 is for Netflix; host 7 is for Hulu. Within intermediary.py (the code for h2), we created a dictionary called 'app_type_to_upload_bandwidth'. This is what determines the delay each packet will experience before being sent to the relevant application from h2. Within this dictionary, we assigned the time taken based on the real bandwidth requirements for upload speeds listed on the application websites (except for email, Netflix, and Hulu, which we estimated would take a low amount of bandwidth to upload since they don't require user video sharing.) 

To replicate upload/download speed, we created our topology and the send/receive files such that they run both ways. h1 going to h2 and h2 going to its destination is upload speed, and the destination host going back to h2 and then back to h1 is download speed. In our application.py file, we created a dictionary called 'app_type_to_download_bandwidth'. As in the upload bandwidth dictionary, this assigns delay times based on the download speeds required listed on the application websites.

Lastly, our formula for assigning delay times is: 1 / app_type_to_bandwidth[app_type] * app_type_to_priority[app_type]^2. Our app_type_to_priority dictionary is where we assign priority by application type. Zoom and Skype have the highest priority (1), Email is lower priority (2), and Netflix and Hulu are lowest priority (3). Our formula then determines delay time based on the bandwidth required per application type multiplied by application priority^2. We square the application priority while keeping the relationship between delay and bandwidth required inversely linear, because we deemed the "priority" of the application (e.g. the relative importance to the user) to be a more important factor than the bandwidth recommendations provided by these applications.

## Read our Final Report
