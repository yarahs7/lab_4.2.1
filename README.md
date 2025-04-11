# Lab 4.2.1 - Playing with HTML and CSS

## How to run manually (dynamic reloading)

In the terminal, use `cd` to change into the project directory (where this README is).
```shell
cd unit-4-lab-2-flask
```

Run the script to start the Flask server. This command will install dependencies
and start a server that will watch for changes. You only need to run this once, make
changes, and reload your local webpage to see your changes.

```shell
./run-flask.sh
```

If you run into a permissions error, run the following command then try again.
```shell
chmod 777 run-flask.sh
```


## How to run using Docker

In the terminal, use `cd` to change into the project directory (where this README is).
```shell
cd unit-4-lab-2-flask
```

Build the Docker container image.
```shell
docker build -t flask-wiki .
```

Run the Docker container image. You will need to re-run the `docker run` command after making your changes.

```shell
docker run -p 8080:8080 flask-wiki
```

Open the link or the web preview on the correct port and you should see the app!

