from gsbib.scholar_bibtex_keys import convert_bibtex_keys

def main(*argv):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, default='')
    parser.add_argument('output_file', type=str, default='')
    args = parser.parse_args()
    convert_bibtex_keys(args.input_file, args.output_file)

if __name__ == '__main__':
    main()