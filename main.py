"""Entry point for process."""

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="MMS", description="Process Mr Ms Smith")
    parser.add_argument(
        "what",
        type=str,
        default=None,
        help="what to do",
        choices=["migrate", "scrape-mms"],
    )
    parser.add_argument(
        "-nr",
        "--num-regions",
        type=int,
        dest="num_regions",
        default=None,
        help="num regions",
    )

    parser.add_argument(
        "-nd", "--num-dates", type=int, dest="num_dates", default=None, help="num dates"
    )
    parser.add_argument("-d", "--database", type=str,
                        help="database connection")

    args = parser.parse_args()

    if args.what == "scrape-mms":
        from scrapers import mms

        scrape = mms.Scraper(connection=args.database)

        mms.main(
            num_regions=args.num_regions,
            num_dates=args.num_dates,
            scraper=scrape,
        )
    elif args.what == "migrate":
        from scrapers import migrate

        migrate.upgrade_migrations(args.database)
