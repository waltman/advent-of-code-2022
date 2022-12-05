#!/usr/bin/env perl
use v5.36;

sub contains(@elf) {
    if ($elf[0] >= $elf[2] && $elf[1] <= $elf[3]) {
        return 1;
    } elsif ($elf[2] >= $elf[0] && $elf[3] <= $elf[1]) {
        return 1;
    } else {
        return 0;
    }
}

sub overlap(@elf) {
    if ($elf[2] <= $elf[0] <= $elf[3]) {
        return 1;
    } elsif ($elf[2] <= $elf[1] <= $elf[3]) {
        return 1;
    } elsif ($elf[0] <= $elf[2] <= $elf[1]) {
        return 1;
    } elsif ($elf[0] <= $elf[3] <= $elf[1]) {
        return 1;
    } else {
        return 0;
    }
}

my @elves;
while (<>) {
    chomp;
    push @elves, [split /[,\-]/];
}

my $contains_count;
my $overlap_count;
for my $elf (@elves) {
    $contains_count++ if contains(@$elf);
    $overlap_count++ if overlap(@$elf);
}

say "Part 1: $contains_count";
say "Part 2: $overlap_count";
