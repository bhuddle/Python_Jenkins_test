import subprocess

def test_connectivity():
    cmd = 'ping -n 1 google.com'.split()
    ret = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    assert 'Reply' in ret