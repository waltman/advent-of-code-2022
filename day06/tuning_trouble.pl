#!/usr/bin/env perl
use v5.36;

sub marker_pos($buf, $len) {
    my @buf = split //, $buf;
    for my $i (0..$#buf-$len) {
        my %chars = map {$_ => 1} @buf[$i..$i+$len-1];
        return $i+$len if keys %chars == $len;
    }
    return -1;
}

while (<>) {
    say "Part 1: ", marker_pos($_, 4);
    say "Part 2: ", marker_pos($_, 14);
}
