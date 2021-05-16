# SPARQL query reformulation helper

A small Python 3 script to make the Ontop query reformulation endpoint easier to use.

## How to use

The script requires a running Ontop instance to use.
Note that the Ontop instance must be running in dev mode in order for the reformulation endpoint to be available.
The script assumes that the endpoint is available locally at http://192.168.99.100:8080/ontop/reformulate

For information regarding Ontop configuration, 
see the [Ontop documentation](https://ontop-vkg.org/guide/cli.html#ontop-endpoint).

A file containing the SPARQL query is also required and must be specified using the `--targetfile` or `-f` parameter. 
Both relative and absolute paths should work, but Windows paths must be in quotes.

Script can be run from the command line with the command `python reformulate.py --targetfile=query.sparql`
