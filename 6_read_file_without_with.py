
file = open('port_scan_log.txt', 'a')
file.write('2020-07-01 12:00:00, port: 80, status: open\n')
file.flush()
file.close()

read_file = open('port_scan_log.txt', 'r')
print(read_file.read())
read_file.close()
