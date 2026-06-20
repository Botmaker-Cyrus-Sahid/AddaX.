complete -c sqv -l keyring -d 'A keyring' -r -F
complete -c sqv -l not-after -d 'Consider signatures created after TIMESTAMP as invalid. If a date is given, 23:59:59 is used for the time. [default: now]' -r
complete -c sqv -l not-before -d 'Consider signatures created before TIMESTAMP as invalid. If a date is given, 00:00:00 is used for the time. [default: no constraint]' -r
complete -c sqv -s n -l signatures -d 'The number of valid signatures to return success' -r
complete -c sqv -s v -l verbose -d 'Be verbose'
complete -c sqv -s h -l help -d 'Print help'
complete -c sqv -s V -l version -d 'Print version'
