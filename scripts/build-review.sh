#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
review_output="${1:-$project_root/dist}"
hugo --source "$project_root" --environment review --destination "$review_output" --baseURL "https://zonge-international.github.io/zonge-design-review-2027/" --minify
# Review hosting must never claim the production domain.
rm -f "$review_output/CNAME"
touch "$review_output/.nojekyll"
