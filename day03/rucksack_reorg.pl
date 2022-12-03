#!/usr/bin/env perl
use v5.36;
use Set::Scalar;

sub priority($c) {
    return 'a' le $c le 'z' ? ord($c) - ord('a') + 1 : ord($c) - ord('A') + 27;
}

sub common_item($c1, $c2) {
    return (Set::Scalar->new(@$c1) * Set::Scalar->new(@$c2))->[0];
}

sub group_badge($rucks) {
    my $common = Set::Scalar->new($rucks->[0]->@*);
    for my $i (1..$#$rucks) {
        $common *= Set::Scalar->new($rucks->[$i]->@*);
    }
    return $common->[0];
}

my $score;
my $group_score;
my @rucks;

while (<>) {
    chomp;
    my @c = split //;
    my $middle = @c / 2;
    my $common = common_item([@c[0..$middle-1]], [@c[$middle..$#c]]);
    $score += priority($common);
    push @rucks, \@c;
    if (@rucks == 3) {
        my $badge = group_badge(\@rucks);
        $group_score += priority($badge);
        @rucks = ();
    }
}

say "Part 1: ", $score;
say "Part 2: ", $group_score;
