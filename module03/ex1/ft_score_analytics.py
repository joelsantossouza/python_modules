import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc: int = len(sys.argv) - 1
    if argc < 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores: list[int] = [None] * argc
        i: int = 0
        try:
            while (i < argc):
                scores[i] = int(sys.argv[i + 1])
                i += 1
        except Exception as e:
            print(f"[ERROR] - {e}")
        else:
            total_score: int = sum(scores)
            min_score: int = min(scores)
            max_score: int = max(scores)
            print(f"Scores processed: {scores}")
            print(f"Total players: {argc}")
            print(f"Total score: {total_score}")
            print(f"Average score: {total_score / argc}")
            print(f"High score: {max_score}")
            print(f"Low score: {min_score}")
            print(f"Score range: {max_score - min_score}")
