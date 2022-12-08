#!/usr/bin/env perl
use v5.36;

package Dir;
use List::Util qw(sum0);

sub new($package, $name, $parent) {
    my $self = {};
    bless $self, $package;

    $self->{name} = $name;
    $self->{parent} = $parent;
    $self->{files_size} = 0;
    $self->{children} = ();

    return $self;
}

sub size($self) {
    return $self->{files_size} + sum0 map {$_->size()} values $self->{children}->%*;
}

my $root = Dir->new('/', undef);
my $pwd = $root;

while (<>) {
    chomp;
    my @toks = split ' ';
    if ($toks[0] eq '$') {
        if ($toks[1] eq 'cd') {
            if ($toks[2] eq '/') {
                $pwd = $root;
            } elsif ($toks[2] eq "..") {
                $pwd = $pwd->{parent};
            } else {
                $pwd = $pwd->{children}{$toks[2]};
            }
        } elsif ($toks[1] eq "dir") {
        }
    } else {
        if ($toks[0] eq "dir") {
            $pwd->{children}{$toks[1]} = Dir->new($toks[1], $pwd);
        } else {
            $pwd->{files_size} += $toks[0];
        }
    }
}

my $part1_sum;
my @queue = ($root);
my $TOTAL_SPACE = 70000000;
my $NEEDED_SPACE = 30000000;
my $unused = $TOTAL_SPACE - $root->size();
my $target = $NEEDED_SPACE - $unused;
my $min_target = 1e300;

while (@queue) {
    my $subdir = pop @queue;
    my $size = $subdir->size();
    if ($size <= 100000) {
        $part1_sum += $size;
    }
    if ($size >= $target) {
        $min_target = $size if $size < $min_target;
    }
    for my $child (values %{$subdir->{children}}) {
        push @queue, $child;
    }
}

say "Part 1: ", $part1_sum;
say "Part 2: ", $min_target;
