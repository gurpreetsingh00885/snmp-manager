import os, time

while(1):
	os.system("""snmptrap -v 2c -c public localhost '' 1.3.6.1.4.1.8072.2.3.0.1 1.3.6.1.2.1.2.2.1.6 s '54:52:55:53:54:54'""")
	time.sleep(1)
