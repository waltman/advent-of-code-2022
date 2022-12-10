#!/usr/bin/env perl
use v5.36;
use Path::Tiny;

my @cmds = path($ARGV[0])->lines({chomp => 1});

my $X = 1;
my $cycle = 1;
my $ip = 0;
my $skip = 1;
my $strengths = 0;
my @crt = (' ') x 240;

while (1) {
    $strengths += $cycle * $X if $cycle % 40 == 20;
    $crt[$cycle-1] = '#' if $X-1 <= ($cycle-1) % 40 <= $X+1;
    my @cmd = split ' ', $cmds[$ip];
    if ($cmd[0] eq 'addx') {
        if ($skip) {
            $ip--;
            $skip = 0;
        } else {
            $X += $cmd[1];
            $skip = 1;
        }
    }
    $cycle++;
    $ip++;
    last if $ip >= @cmds;
}

say "Part 1 $strengths";
say "Part 2";
for (my $i = 0; $i < 240; $i += 40) {
    say @crt[$i..$i+39];
}
