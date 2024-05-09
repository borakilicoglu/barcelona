from .screen import Application, Footballers, Stats
import argparse

def main():
    parser = argparse.ArgumentParser(description='Barcelona ClI')
    parser.add_argument('-squad', action='store_true', help='Barcelona Squad')
    parser.add_argument('-stats', action='store_true', help='Top Scorers')
    args = parser.parse_args()
    if args.squad is False and args.stats is False:
        try:
            screen = Application()
            screen.setup()
            screen.run()
        except KeyboardInterrupt:
            pass
        except Exception as ex:
            print(ex)

    if args.squad:
        try:
            screen = Footballers()
            screen.setup()
            screen.run()
        except KeyboardInterrupt:
            pass
        except Exception as ex:
            print(ex)

    if args.stats:
        try:
            screen = Stats()
            screen.setup()
            screen.run()
        except KeyboardInterrupt:
            pass
        except Exception as ex:
            print(ex)
