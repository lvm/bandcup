# bandcamp-downloader front end

## what

A clone of my other project named [vackup](https://github.com/lvm/vackup).

> An over-engineered solution to download _movies_ from Youtube (and the other platforms supported by `youtube-dl`) directly to my raspberry-pi, because I found tiresome to `ssh` to it to download something when using my phone.

Pretty much that, but downloads from bandcamp instead.


## components

* flask app, listening on port 5000
* celery
* redis
* flower (to monitor tasks), listening on port 5555

### bandcamp-downloader

[tasks.py] has a custom _downloader_ that can be useful for those who wonder how to use [bandcamp-downloader](https://github.com/iheanyi/bandcamp-dl) from a script instead of the cli app.

## how to run

Make sure you've modified `docker-compose.yml` to match your directory where you store your videos, then:

```
git clone https://github.com/lvm/bandcup \
    && cd bandcup \
    && docker-compose up --build -d
```

Yes, you need to have docker (18.09+) and docker-compose (1.24+).

## now what

Once it's running, point your browser to `http://your-raspi.local:5000/` and submit a video, it'll start downloading soon.
The UI is really basic (front-end is not my thing) but you'll see these two status:

* 🙆‍ if the task was created fine (with a link to it)
* 🙅‍ if the task failed


## something's not working...

* you can check what's going on here with your tasks here: `http://your-raspi.local:5555/`
* or you can look at the logs by ssh-ing to your raspi and run `docker-compose logs -f $service`

Note: `$service` represents one of the services listed in the `docker-compose.yml` file (`flask`, `queue`, `monitor`, `redis`)

## license

yes.
