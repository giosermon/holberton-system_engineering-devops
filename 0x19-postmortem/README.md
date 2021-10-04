<h1>0x19-postmortem</h1>
Postmortem

Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

<h1>issue Summary</h1>
On October 03 , 2021, at approximately 08:52  until 9:30 , an outage occurred on an isolated Ubuntu 20.04.3 LTS container running an Apache web server. When running GET requests on the server, that led to a500 Internal Server Error

Timeline
08:52 - 500 error showing in server
08:55 - Check status of server and shows its OK
08:57 - Used strace to find issue by connecting Child process for Apache
09:10 - Found issue in the wp-settings.php showing that file missing
09:12 - Found file being misspelled in the settings file .phpp
09:14 - Fixed file by changing the typo to .php
09:15 - Restarte Apache
09:26 - Server now running normally

<h1>Root Cause and Resolution</h1>
The issue was found by trying to access the server by curl into it but the response was shooting out 500 error. By checking the server using strace and connecting the PID that is associated with the child process of the Apache service, the main cause of the server issue was the misspelling in the wp-setting file. In the file there was a call to /class-wp-locale.phpp witch is misspelled because the file it was trying to call is the /class-wp-locale.php file and due to this misspelling the strace shows that the file doesn’t exist when it is trying to call it. Than I changed the .phpp to .php by using puppet to replace any files that are named .phpp to be replaced to .php to fix all the other possible misspelling issues that might have occurred in the file/. After restarting the Apache service the server started to operate normally.

<h1>Corrective and Preventative Measures</h1>
To make thing better in the future the server should be tested before deploying. Because of this small misspelling issue, the service went down, and customers cannot access the service.
Another way to prevent from this happening, we should enable error logging to find issues quicker by looking at error logs in the assigned server there where no error logs enabled so to find the issue we needed to enable the error log to find issue.
