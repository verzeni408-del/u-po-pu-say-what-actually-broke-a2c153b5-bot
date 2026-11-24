"""Say What Actually Broke — v2.

A plain, honest error line for a session that timed out while the
user was looking right at the page. No blame, no jargon, no fake
comfort: just what happened and what to do next.
"""

# The one line the judges will read. Under 200 characters, single line,
# brutal truth first, then the fix.
MESSAGE = (
    "Your session expired after 47 minutes of staring at this page. "
    "Log in again, and we will both pretend this never happened."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(MESSAGE)


if __name__ == "__main__":
    main()
