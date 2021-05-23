import os
import sys
import argparse
import requests
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--targetfile', help='Specify the SPARQL query file. Windows paths must be quoted',
                        metavar='FILE', required=True)
    args = parser.parse_args()
    infile = ''

    if os.path.isabs(args.targetfile):
        infile = args.targetfile
    else:
        infile = os.path.join(sys.path[0], args.targetfile)

    print('\n ### Reading file: {} \n'.format(infile))

    with open(infile, 'r', encoding='utf_8') as f:
        # Nolasam faila esoso vaicajumu
        text_in = f.read()

        print('\n ### SPARQL query from file: \n')
        print(text_in)

        # Attiram vaicajuma jaunas rindas simbolus
        text_in = re.sub(r'\r\n', ' ', text_in)
        text_in = re.sub(r'\n', ' ', text_in)

        # Sagatavojam un izpildam pieprasijumu Ontop tulkosanas galapunktam
        payload = {"query": text_in}
        response = requests.get(
            "http://192.168.99.100:8080/ontop/reformulate", params=payload
        )
        if response.status_code != 200:
            raise Exception(
                "Cannot get response (HTTP {0}): {1}".format(
                    response.status_code, response.text
                )
            )

        print('\n ### Translated query: \n')
        print(response.text)

