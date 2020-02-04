import re
from pybtex.database import parse_file
from pybtex.utils import OrderedCaseInsensitiveDict


def obtain_replace_keys(bib_data):
    """
    Obtain Google Scholar style keys from parsed bibliography data.
    """
    keys, new_keys = [], []
    for key in bib_data.entries.keys():
        try:
            author_last_name = bib_data.entries[key].persons['author'][0].last_names[0].lower(
            )
        except:
            print(key)
        try:
            year = bib_data.entries[key].fields['year']
        except:
            year = ''
        title_first_word = re.search(
            r'\w+', bib_data.entries[key].fields['title']).group(0).lower()
        new_key = author_last_name + year + title_first_word
        keys.append(key)
        new_keys.append(new_key)
    return keys, new_keys


def update_arxiv_information(bib_data):
    """
    Include arxiv information in journal field.
    """
    for key, entry in bib_data.entries.items():
        if 'arxivid' in bib_data.entries[key].fields:
            bib_data.entries[key].fields['journal'] = 'arXiv preprint arXiv:{}'.format(
                bib_data.entries[key].fields['arxivid']
            )
    return bib_data


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
    bib_data = update_arxiv_information(bib_data)
    with open(output_file, 'w', encoding='utf-8') as ofile:
        bib_data.to_file(ofile)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, default='')
    parser.add_argument('output_file', type=str, default='')
    args = parser.parse_args()
    convert_bibtex_keys(args.input_file, args.output_file)
