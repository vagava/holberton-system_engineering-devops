# 0x0C. Web server

## Concepts

- [DNS]()
- [Web Server]()
- [CI/CD]()
- [Docker]()
- [Web stack debugging]()
- [What is a Child Process?]()
- [DevOps]()
- [System Administration]()
- [Site Reliability Engineering]()

 if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`

 ```
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
 ```

## Resources

- [How the web works]()
- [Nginx]()
- [How to Configure Nginx]()
- [Child process concept page]()
- [Root and sub domain]()
- [HTTP requests]()
- [HTTP redirection]()
- [Not found HTTP response code]()
- [Logs files on Linux]()

### For reference:

- [RFC 7231 (HTTP/1.1)]()
- [RFC 7540 (HTTP/2)]()
### man or help:

- `scp`
- `curl`
