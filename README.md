# Solar REST api

A RESTful api created to provide data to the Solar application\
\
The current api endpoint can be found at `api.solarnews.ga`

## Conventions

Some conventions to help the distribution and the usage of data. Both requests and responses are expected to be using those formats.

### DateTime

All datetimes must be converted in timestamps (milliseconds since epoch), in order to be easly convertible in every programming language.
Please specify datetimes in UTC, this is what the api expects.

### Urls

All urls, that are used for things as images and webcasts are checked using a regex and need to contain images or streams.

### Colors

Colors are stored as 6-digit hex values (ex. 'ff11ff')
