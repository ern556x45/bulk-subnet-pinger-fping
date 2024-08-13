<h1>Bulk Subnet Pinger - Fping</h1>

This script will use a source txt document and run fping -g | grep alive for each inserted subnet.

The output of this script will only show Alive IPs, no ICMP host timeouts or other data will be displayed.

<h2> Operational instructions </h2>

<ol>
<li> Open subnets.txt and insert the subnets you wish to check. Accepted format is <b> New line, Subnet, New line, Subnet.</b> </li>
<li> Make sure it's saved by pressint CTRL + S (May vary on text editor) </li>
<li> Open a terminal and run python check_alive_hosts.py </li>
<li> Results will be added to "alive_hosts.txt". </li>
</ol>

<h2> Dependencies </h2>

A <b>Linux Terminal</b> (Native or WSL)

<b>Fping</b> - Can be installed via this command on Ubuntu:

>sudo apt install fping

<b>Python</b>. or the </b>Python3</b> package - Can be installed via this command on Ubuntu:

>sudo apt install python

OR

>sudo apt install python3

If there are any adjustments or neccesary changes, please let me know.