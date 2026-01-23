#!/usr/bin/env python3

from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ...")
    else:
        print("=== Player Score Analytics ===")
        try:
            score = [int(n) for n in argv[1:]]
        except Exception as e:
            print(f"Error: {e}")
        else:
            print(
                f"score processed: {str(score)}\n"
                f"Total players: {len(score)}\n"
                f"Total score: {sum(score)}\n"
                f"Average score: {round(sum(score)/len(score), 2)}\n"
                f"High score: {max(score)}\n"
                f"Low score: {min(score)}\n"
                f"Score range: {max(score) - min(score)}\n"
            )
