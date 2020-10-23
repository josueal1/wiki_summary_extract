#!/bin/bash
# Linter are static code analysis tools that flags syntax errors, bugs, style

# Get list of all files that were Git Added (passed down for github)
if [[ $# > 1 ]];then
	ARRAY=( "$@" )
	last_idx=$(( ${#ARRAY[@]} - 1 ))
	unset array[$last_idx]

	echo "LINT.SH array contains:"
	printf "%s\n" "${ARRAY[@]}"
else
	current_branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p');
	ARRAY=($(git diff origin/master $current_branch --name-only HEAD));
	printf "\nFollowing files are differnet between 'origin/master' and '${current_branch}':\n\n"
	printf "%s\n" "${ARRAY[@]}"
fi


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
