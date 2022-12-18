
def execute():
    
    # We need to write the module from the page www.fib.upc.edu where there is the certificate information
    module = "9D:B2:C7:CA:34:D4:0C:97:E6:70:AC:3A:98:0C:22:EE:51:67:3F:B1:5A:1B:9E:B1:78:DB:CB:21:7D:60:A7:87:D7:98:62:34:5D:C3:8B:B8:B1:99:A7:AF:7E:D6:BA:8C:6C:31:3B:55:D0:0F:E9:5C:D6:CE:62:04:6A:54:19:03:34:E7:FC:94:7E:7E:49:EE:E1:E1:0C:10:00:B4:3E:76:A0:1D:25:49:AC:A3:DB:D6:F4:48:CE:09:C8:74:B8:4F:DE:FE:B6:20:3F:FD:7E:69:D7:34:A7:44:B7:49:2F:E7:08:6A:1A:B8:1E:8E:C2:3C:F9:E9:76:6C:15:A1:ED:80:F7:64:C3:76:1D:6C:1A:52:37:0F:19:87:99:67:FF:4B:44:93:4F:BD:21:0A:72:8F:89:72:90:A5:8C:7D:3B:8A:B7:04:08:FE:1A:BB:E5:8C:BA:3C:FA:BB:3E:B4:7B:CD:47:59:9B:A6:21:D3:12:86:94:24:39:9E:2D:89:C6:94:AA:F7:20:89:91:0B:2C:0A:25:69:F1:09:E1:85:BB:03:B1:29:29:A2:F2:93:5C:40:CC:36:45:D2:42:30:C5:18:52:1F:C3:8C:C6:ED:E3:88:19:1A:C3:15:EE:1C:A4:DA:E4:F8:B3:7A:34:E1:54:5A:B3:EC:61:D2:E6:3D:0D:97:A6:73:CB:49:B7:0E:D3:F8:D4:DB:35:3A:5F:0D:97:3F:FE:AF:B7:56:CC:2C:DE:FE:DB:1A:FD:9D:5E:67:C6:2B:F5:13:8A:1A:53:21:0E:1B:8F:1E:D0:F6:83:6A:01:39:1B:B2:03:1C:F8:01:DF:A5:14:13:4A:30:C5:D3:23:AA:DB:2D:07:7B:1A:2E:C9:4E:6C:69:0D:92:F3:69:1B:45:8E:68:5B:F7:43:42:3B:C8:98:80:9B:AC:59:3D:AB:1C:73:6A:83:A2:20:31:1F:20:02:16:DF:28:2F:84:4A:72:C3:F1:23:8F:FD:FC:AA:32:92:1E:C2:18:D9:13:29:B6:A2:CC:5F:AC:CD:EB:A5:48:AE:6A:80:8B:47:06:41:D3:6D:BE:80:B6:5A:7C:86:3E:39:DA:65:FF:78:C8:3C:53:D6:BD:A2:27:AF:94:DD:CE:C2:05:FD:A9:EB:63:DD:ED:4E:A1:17:8E:4F:57:98:4B:B2:F4:2E:B5:DD:5C:38:AE:39:94:3A:3D:FF:03:00:15:92:B3:5E:7E:BF:25:A1:E8:D0:D3:13:B4:99:79:80:93:60:E5:42:4B:1E:A8:DF:7B:7A:B5:B0:55:07:7E:E4:C7:6A:7D:4D:01:E9:6E:D9:76:02:71:8A:DD:58:E3:4E:1E:E7:45:C7:EF:C8:18:A3:77"

    newM = ""
    for x in module:
        if x != ":":
            newM = newM + x
   
    # Hexadecimal module value 
    print("El modul en hexadecimal es: " + newM)

    # Decimal module value
    modDec = int(newM, 16)
    print("el modul en decimal es:\n")
    print(modDec)

    # The number of digits in the module 
    print(len(str(modDec)))

    # We start reading the CRL and counting the number of revoked certificates in the Certificate Revocation List 
    file = open("infoCRL.txt", "r")
    lines = file.read()
    print("El nombre de certificats revocats es " + str(lines.count("Serial Number")))


# Main
if __name__ == "__main__":
    execute()