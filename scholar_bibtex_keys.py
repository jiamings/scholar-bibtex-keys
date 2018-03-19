import re
from pybtex.database import parse_file
from pybtex.utils import OrderedCaseInsensitiveDict


def obtain_replace_keys(bib_data):
    """
    Obtain Google Scholar style keys from parsed bibliography data.
    """
    keys, new_keys = [], []
    for key in bib_data.entries.keys():
        author_last_name = bib_data.entries[key].persons['author'][0].last_names[0].lower()
        year = bib_data.entries[key].fields['year']
        title_first_word = re.search(r'\w+', bib_data.entries[key].fields['title']).group(0).lower()
        new_key = author_last_name + year + title_first_word
        keys.append(key)
        new_keys.append(new_key)
    return keys, new_keys


def convert_bibtex_keys(input_file: str, output_file: str):
    """
    Convert keys in a bibtex file to Google Scholar format.
    @input_file: string, input file name.
    @output_file: string, output file name.
    """
    bib_data = parse_file(input_file)
    keys, new_keys = obtain_replace_keys(bib_data)
    new_entries = OrderedCaseInsensitiveDict()
    for key, new_key in zip(keys, new_keys):
        new_entries[new_key] = bib_data.entries[key]
    bib_data.entries = new_entries
    with open(output_file, 'w') as ofile:
        bib_data.to_file(ofile)

