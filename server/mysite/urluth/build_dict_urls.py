from .data_urls import bigstring_urls


def build_dict_urls(bigstring_urls):

    final_urls_from_key_urls = {}
    for string_url in bigstring_urls.split("\n"):
        string_url = string_url.lstrip()
        key_url, space, final_url = string_url.partition(" ")
        if space and key_url.isalnum():
            final_url = final_url.strip()
            final_urls_from_key_urls[key_url] = final_url

    return final_urls_from_key_urls

final_urls_from_key_urls = build_dict_urls(bigstring_urls)


def main():
    print(final_urls_from_key_urls)

if __name__ == "__main__":
    # REC TODO : ne marchera pas à cause des imports bizarres en python, que
    # à chaque fois j'y comprends rien et je dois retrouver comment c'est fait.
    main()