#!/bin/bash

# Step 1: Remove users with non-login shells
grep -Ev '(/sbin/nologin|/bin/false)$' problem-file.txt |

# Step 2: Update home directories from old path to new
sed 's|/home/user|/home/users|g' |

# Step 3: Sort by username (first field, colon-separated)
sort -t ':' -k1,1 > cleaned_users.txt
