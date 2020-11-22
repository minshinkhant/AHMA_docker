# AHMA Vending Machine

## Running

The server is managed as a docker instance. Run it by `cd`ing to this
directory and then running:

    docker build -t ahma .
    docker run --rm -dp 80:80 ahma

It will take a bit of time the first time you run it. Then it will be
much faster to start. Remove the `--rm` if you want the container to
persist.

The webpage is then accessible on http://localhost and documentation
is on http://localhost/docs
