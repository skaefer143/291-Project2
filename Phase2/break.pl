#!/usr/bin/perl

# ----
# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 2 - Perl script (Spit lines at :)
# Last Change By:
# Time Changed:
# ----

while (<STDIN>) {
  chomp;
  if (/^(.*?):(.*?)$/) {
    $key=$1; $rec=$2;
    # BDB treats backslash as a special character, and we would get rid of it!
    $rec =~ s/\\/&92;/g;
    print $key, "\n", $rec, "\n";
  }
}

