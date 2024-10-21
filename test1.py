import pytest
import socket

# Test to check if the IP address is reachable
def test_ip_reachable():
    ip_address = "192.168.1.44"
    try:
        socket.gethostbyname(ip_address)
        assert True
    except socket.error:
        pytest.fail(f"IP address {ip_address} is not reachable")
