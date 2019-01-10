import subprocess

def test_jenkins():
    cmd = 'sc query jenkins'.split()
    ret = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    assert 'RUNNING' in ret
