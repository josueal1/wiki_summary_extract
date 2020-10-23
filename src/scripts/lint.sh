#!/bin/bash
# Linter are static code analysis tools that flags syntax errors, bugs, style

# Get list of all files that were Git Added
ARRAY=( $( git diff github.base_ref github.head_ref --name-only HEAD; ) )

# Get the number of Python files currently Git Added
NUM_PY_FILES=0
for i in "${ARRAY[@]}"
do
	if [[ "$i" == *".py"* ]]; then
		((NUM_PY_FILES++))
	fi
done

printf "\n"
printf "lint.sh: $NUM_PY_FILES python files git add'ed.\n\n"

# L
for filename in "${ARRAY[@]}"
do
	ERROR_CODES="E1101"
	if [[ "$filename" == *".py"* ]]; then

		pylint "$filename" --exit-zero --jobs=0 --score=y \
			--msg-template="{msg_id}: {category}: {path} {line}:{column} {msg}" \
			--disable=$ERROR_CODES		
	fi
done

printf "lint.sh: Done\n\n"
