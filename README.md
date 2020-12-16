# Bandwidth Allocation in the Home via Zoom
CS143 Final Project by Sara Kvaska, Serena Davis, Gustavo Coutinho and Jenna Moustafa

## How to Run Our Code
Step 1: Set up the mininet environment and ensure that you can connect from the host PC to the guest VM via SSH.

Step 2: Once the environment is set up, open a terminal and run: ssh -X [user]@[Guest IP Here]. 
  - Replace [user] with the correct user name for your VM image (in our case, mininet). 
  - Replace [Guest IP Here] with the IP you noted from the VM (in our case, 192.168.56.101). 
  - When prompted, enter the password for the VM image (in our case, mininet). 
  
 Step 3: Start up an X terminal using '$ xterm' and a new terminal window should appear. 
  - If you get a 'xterm: DISPLAY is not set error', try running ssh -Y [user]@[Guest IP Here] instead of using -X.
  
 Step 4: Inside the xterm terminal, cd into '~/pox/pox/misc' directory, then run the command 'sudo fuser -k 6633/tcp'. This is to kill any controllers still running on the system. (When first running this there should not be, but just in case.)
  - Then, run 'sudo mn -c' to cleanup the configuration. We want to cleanup before running the topology. 
  
 Step 5: After completing steps 1-4 above, we are ready to run our topology. Make sure the topo.py file is inside the ~/pox/pox/misc directory, then run the command 'sudo mn --custom topo3.py --topo custom'. A topology of 7 hosts, 7 switches, and 1 controller should be created, and the CLI should be started. 
 
 Step 6: Run the command 'xterm h1 h2 h3 h4 h5 h6 h7'. This will open separate terminals for all 7 hosts. 
  - Inside the 'Node: h1' terminal, run 'python send_sluice4.py 10.0.0.2 1234 1'. This will run the send_sluice4.py file, and takes in 3 arguments: <destination IP> <scrPort> <app_type>. Our destination IP is always 10.0.0.2, because host 2 will send the packets to their intended host (hosts 3 through 7, depending on the app type). Our srcPort is always 1234, and the app_type argument is a number ranging from 1 through 5. 
  - Inside the 'Node: h2' terminal, run 'python receive_sluice5.py'.  
  - Inside the 'Node: h3', 'Node: h4', 'Node: h5', 'Node: h6', and 'Node: h7' terminals, run 'python receive_sluice_back1.py'. 

Step 7: Now that the topology set up and we can run our send and receive files, we can run the commands by different app type.
  - The command 'python send_sluice4.py 10.0.0.2 1234 1' sends app_type 1 (which is Zoom), to h2. Host 2 then forwards this to h3, which prints out the app type it receives, the host address it received it from, and the app type name. It sends an application type 'User App' back to h1 once this information is received from h2.
  - The command 'python send_sluice4.py 10.0.0.2 1234 2' sends app_type 2 (which is Skype), to h2. Host 2 then forwards this to h4, which (as above) prints out the information its received, and sends an application 'User App' back to h1.
  - The command 'python send_sluice4.py 10.0.0.2 1234 3' does the same as above, except app_type 3 is Email. Host 2 forwards this to h5, and the same steps are repeated.
  - The command 'python send_sluice4.py 10.0.0.2 1234 4' does the same as above, except app_type 4 is Netflix. Host 2 forwards this to h6, and the same steps are repeated.
  - The command 'python send_sluice4.py 10.0.0.2 1234 5' does the same as above, except app_type 5 is Hulu. Host 2 forwards this to h7, and the same steps are repeated. 
  
## Methodology
