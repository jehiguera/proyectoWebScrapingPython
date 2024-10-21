import pytest
import subprocess

# Test to check if the arp -a command shows the IP 192.168.2.1
def test_arp_command():
    ip_to_check = "192.168.2.1"
    try:
        # Run the arp -a command
        result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE, text=True)
        
        # Check if the output contains the IP address
        if ip_to_check in result.stdout:
            assert True
        else:
            pytest.fail(f"IP address {ip_to_check} not found in ARP table")
    except Exception as e:
        pytest.fail(f"Failed to execute arp -a command: {str(e)}")
