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
        choices=["migrate", "scrape-mms", "scrape-vir", "scrape-kiwi"],
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
        "-dbg",
        "--debug",
        default=None,
        action="store_true",
    )
    parser.add_argument(
        "-nd", "--num-dates", type=int, dest="num_dates", default=None, help="num dates"
    )
    parser.add_argument("-d", "--database", type=str,
                        help="database connection")

    args = parser.parse_args()

    if args.what == "scrape-mms":
        from scrapers import mms

        mms.main(
            num_regions=args.num_regions,
            num_dates=args.num_dates,
            connection=args.database,
        )
    elif args.what == "migrate":
        from scrapers import migrate

        migrate.upgrade_migrations(args.database)

    elif args.what == "scrape-vir":
        from scrapers import virt

        virt.main(connection=args.database,
                  lim=args.num_regions, debug=args.debug)
    elif args.what == "scrape-kiwi":
        from scrapers import kiwi

        kiwi.main(connection=args.database,
                  lim=args.num_regions, debug=args.debug)
