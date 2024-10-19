import json
import argparse

from src.main import app

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", "-o", type=str, default="openapi.json")

    args = parser.parse_args()

    output_path = args.output_path

    print(f"Exporting openapi schemas to: {output_path}")

    with open(output_path, "w") as fs:
        json.dump(app.openapi(), fs)

    print(f"done.")
