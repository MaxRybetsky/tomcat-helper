# tomcat-helper
Helps me start/stop/build-and-restart tomcat server and move ready war package from work directory to "webapps" folder of root server directory in semi-automatic mode.

It works good when you have IntelliJ IDEA Community, want to create and debug Spring MVC Apps and don't want manually move war package to "webapps" folder and to start/stop TomCat Server every time you need to test your app.

Start this helper by command: <br>
<code>py main.py</code>

Also you can build <i>.exe</i> file by command:
<br>
<code>pyinstaller --onefile main.py</code>
