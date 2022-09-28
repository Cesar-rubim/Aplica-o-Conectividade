import argparse

def read_user_cli_args():
    parser = argparse.ArgumentParser(
        prog="site_checker", description="Teste a disponibilidade de uma URL"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="insira um ou mais URLs",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'O status da "{url}" é:', end=" ")
    if result:
        print('"Online!" ')
    else:
        print(f'"Offline?"  \n  Erro: "{error}"')