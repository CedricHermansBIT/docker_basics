# Dockerfile basics

This repo contains the necessary files to run the example code from 8.2.9.1. Dockerfile basics

To run this docker container, clone the repository:

```bash
git clone https://github.com/CedricHermansBIT/docker_basics.git
cd docker_basics
```

Next build the container using

```bash
docker build -t testdocker .
```
*Note: the "." add the end is important, indicating you want to run it from the current directory!*

Finally, run the container using

```bash
docker run testdocker
```

If all went well, you should see:

$${\color{lightgreen}Hello \space \color{blue}World\color{green}!$$
