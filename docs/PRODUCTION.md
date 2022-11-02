# Deployment

## Docker
### Pre-Built Image
Releases are published to the [Morpheus636/rss-to-email](https://hub.docker.com/r/morpheus636/rss-to-email) Dockerhub page.

To pull the image from Dockerhub, run:
```bash
docker pull morpheus636/rss-to-email
```

### Custom Build
To build the docker container, run:
```bash
docker build .
```

### Configuration
#### `feeds.yml`
Defines the list of feeds for rss-to-email to monitor. See the sample `feeds.yml`
file in this repo for the schema and syntax.

This file needs to be provided to the container via a volume mounted at `/home/default/.config/rss-to-email`

#### Environment Variables
The following environment variables are used by rss-to-email for configuration and secrets
and must be specified at runtime.

- `GMAIL_USER` - The username of the gmail account to send emails as.
- `GMAIL_PASSWORD` - An app password for the gmail account to send emails as.
- `RECIPIENT_ADDRESS` - The email address to send emails to.

