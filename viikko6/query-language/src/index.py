from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    m1 = (
    query
        .PlaysIn("PHI")
        .HasAtLeast(10, "assists")
        .HasFewerThan(5, "goals")
        .build()
    )

    m2 = (
    query
        .PlaysIn("EDM")
        .HasAtLeast(40, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
