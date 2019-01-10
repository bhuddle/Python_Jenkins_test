import subprocess, pytest
#test get system info and check versions
    
def test_getInfo():
    sysInfo = subprocess.Popen('systeminfo', stdout=subprocess.PIPE).communicate()[0].split('\n')
    for x in sysInfo:
        if 'Host Name' in x:
            hostname = x
        if 'OS Version' in x and 'BIOS' not in x:
            osver = x
        if 'BIOS Version' in x:
            biosver = x
        if 'Owner' in x:
            owner = x

    assert 'BENDERRODRIGUEZ' in hostname
    assert '10.0.17134 N/A Build 17134' in osver
    assert 'American Megatrends Inc. 4101   , 4/13/2011' in biosver
    assert 'Bender' in owner