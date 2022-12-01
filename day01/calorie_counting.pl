#!/usr/bin/env perl
use v5.36;
use List::Util qw(max sum);

my @calories;
my $elf;

while (<>) {
    chomp;
    if ($_) {
        $elf += $_;
    } else {
        push @calories, $elf;
        $elf = 0;
    }
}
push @calories, $elf;
say "Part 1: ", max(@calories);

@calories = sort {$b <=> $a} @calories;
say "Part 2: ", sum(@calories[0..2]);
