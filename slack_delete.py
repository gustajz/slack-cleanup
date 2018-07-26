import argparse
import requests
import time
import json
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

def main():
    """
    Entry point of the application
    :return: void
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", required=True, help="Specifies the OAuth token used for authentication, created at (https://api.slack.com/custom-integrations/legacy-tokens)")
    parser.add_argument("-d", "--days", type=int, default=30, help="Delete files older than x days (optional)")
    parser.add_argument("-c", "--count", type=int, default=1000, help="Max amount of files to delete at once (optional)")
    options = parser.parse_args()

    try:
        print ("[*] Fetching file list..")
        file_ids = list_file_ids(token=options.token, count=options.count, days=options.days)

        print ("[*] Deleting files..")
        delete_files(token=options.token, file_ids=file_ids)

        print ("[*] Done")

    except KeyboardInterrupt:
        print ("\b\b[-] Aborted")
        exit(1)


def calculate_days(days):
    """
    Calculate days to unix time
    :param days: int
    :return: int
    """
    return int(time.time()) - days * 24 * 60 * 60


def list_file_ids(token, count, days=None):
    """
    Get a list of all file id's
    :param token: string
    :param count: int
    :param days: int
    :return: list
    """
    if days:
        params = {'token': token, 'count': count, 'ts_to': calculate_days(days)}
    else:
        params = {'token': token, 'count': count}

    uri = 'https://slack.com/api/files.list'
    response = requests.get(uri, params=params)
    files = json.loads(response.text)['files']

    print ("[i]", len(files), "files found")
    toast = []
    space_saved = 0

    # save the starred and pinned items, toast the rest
    for f in files:
        if 'is_starred' in f:
          print (f['name'], "is starred!")
          continue

        if 'pinned_to' in f:
          print (f['name'], "is pinned!")
          continue

        toast.append(f)

        # calculate space savings
        space_saved += f['size']

    print ("[i]", len(toast), "files to toast, saving", locale.format_string("%d", space_saved, grouping=True), "bytes")
    return toast


def delete_files(token, file_ids):
    """
    Delete a list of files by id
    :param token: string
    :param file_ids: list
    :return: void
    """
    count = 0
    num_files = len(file_ids)
    for file_id in file_ids:
        count += 1
        params = {'token': token, 'file': file_id['id']}
        uri = 'https://slack.com/api/files.delete'
        response = json.loads(requests.get(uri, params=params).text)
        if response["ok"]:
            print ("[+] Deleted", count, "of", num_files, "-", file_id['name'], response["ok"])
        else:
            print ("[!] Unable to delete", count, "of", num_files, "-", file_id['name'] + ", reason:", response["error"])

if __name__ == '__main__':
    main()